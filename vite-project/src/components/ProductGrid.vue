<template>
  <div class="grid-section">
    <div class="grid-container">
      <h3 class="section-title">{{ tituloSeccion }}</h3>
      
      <transition-group name="grid-fade" tag="div" class="products-layout" v-if="productosFiltrados.length > 0">
        <div 
          v-for="prod in productosFiltrados" 
          :key="prod.id" 
          class="product-card"
          @click="abrirDetalle(prod)"
        >
          <div class="card-image-wrapper">
            <img :src="prod.img" :alt="prod.title" />
          </div>
          
          <div class="card-info">
            <p class="card-vendor">Vendido por: {{ prod.vendor }}</p>
            <h4 class="card-title">{{ prod.title }}</h4>
            
            <div class="card-price-row">
              <span class="card-price">${{ prod.price.toLocaleString('es-AR') }}</span>
              <span v-if="prod.discount" class="card-discount">{{ prod.discount }}% OFF</span>
            </div>
            
            <p class="card-shipping">⚡ Envío gratis FULL</p>
          </div>
        </div>
      </transition-group>

      <div class="empty-state" v-else>
        <p>No encontramos productos que coincidan con tu selección.</p>
      </div>
    </div>

    <ProductDetailWindow 
      :isOpen="mostrarDetalle"
      :product="productoSeleccionado"
      @close="mostrarDetalle = false"
      @add-to-cart="reenviarAlPadre"
    />
  </div>
</template>

<script>
import ProductDetailWindow from './ProductDetailWindow.vue';

export default {
  name: 'ProductGrid',
  components: {
    ProductDetailWindow
  },
  props: {
    category: {
      type: String,
      default: 'inicio'
    },
    search: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      mostrarDetalle: false,
      productoSeleccionado: null,
      productos: [
        { id: 1, category: 'computadoras', vendor: 'LOGITECH CO', title: 'Teclado Mecánico RGB Logitech G Pro X Teclas Azules Switch Clicky', price: 145999, discount: 15, img: 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?q=80&w=400' },
        { id: 2, category: 'celulares', vendor: 'SAMSUNG CORP', title: 'Samsung Galaxy S24 Ultra 512GB Titanium Gray con Inteligencia Artificial', price: 2149999, discount: 10, img: 'https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?q=80&w=400' },
        { id: 3, category: 'audio', vendor: 'SONY STORE', title: 'Auriculares Inalámbricos Sony WH-1000XM5 Con Cancelación de Ruido', price: 549999, discount: null, img: 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=400' },
        { id: 4, category: 'componentes', vendor: 'ASUS OFFICIAL', title: 'Tarjeta de Video ASUS ROG Strix GeForce RTX 4070 Ti SUPER O16G', price: 1689000, discount: 5, img: 'https://images.unsplash.com/photo-1591488320449-011701bb6704?q=80&w=400' },
        { id: 5, category: 'gaming', vendor: 'RAZER ARG', title: 'Mouse Gaming Inalámbrico Razer DeathAdder V3 Pro Ultra-liviano 63g', price: 189999, discount: 20, img: 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?q=80&w=400' },
        { id: 6, category: 'smart-tv', vendor: 'LG FACTORY', title: 'Smart TV LG OLED evo C3 65 pulgadas 4K UHD Procesador Alpha 9 Gen6', price: 3299999, discount: 12, img: 'https://images.unsplash.com/photo-1593305841991-05c297ba4575?q=80&w=400' }
      ]
    }
  },
  computed: {
    tituloSeccion() {
      if (this.search) return `Resultados para: "${this.search}"`;
      if (this.category === 'inicio') return 'Productos destacados para vos';
      if (this.category === 'ofertas') return '🔥 Ofertas imperdibles del día';
      return `Catálogo de ${this.category}`;
    },
    productosFiltrados() {
      let lista = this.productos;
      if (this.category !== 'inicio' && this.category !== 'ofertas' && !this.search) {
        lista = lista.filter(p => p.category === this.category);
      }
      if (this.category === 'ofertas') {
        lista = lista.filter(p => p.discount !== null);
      }
      if (this.search) {
        const query = this.search.toLowerCase();
        lista = lista.filter(p => p.title.toLowerCase().includes(query) || p.vendor.toLowerCase().includes(query));
      }
      return lista;
    }
  },
  methods: {
    abrirDetalle(prod) {
      this.productoSeleccionado = prod;
      this.mostrarDetalle = true;
    },
    reenviarAlPadre(prod) {
      this.$emit('add-to-cart', prod);
    }
  }
}
</script>

<style scoped>
.grid-section {
  width: 100%;
  margin-top: 30px;
}

.grid-container {
  width: 100%;
  text-align: left;
}

.section-title {
  font-size: 1.6rem;
  color: #333333;
  margin-bottom: 20px;
  font-weight: 400;
}

.products-layout {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 20px;
  width: 100%;
}

.product-card {
  background-color: #ffffff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 2px rgba(0,0,0,0.1);
  cursor: pointer;
  display: flex;
  flex-direction: column;
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s ease;
}

/* Efecto hover suave y elástico en las tarjetas */
.product-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.08);
}

.card-image-wrapper {
  width: 100%;
  height: 200px;
  padding: 20px;
  box-sizing: border-box;
  background-color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  border-bottom: 1px solid #f2f2f2;
}

.card-image-wrapper img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.card-info {
  padding: 15px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.card-vendor {
  font-size: 0.65rem;
  color: #999999;
  text-transform: uppercase;
  margin: 0 0 6px 0;
  font-weight: 700;
  letter-spacing: 0.5px;
}

.card-title {
  font-size: 0.88rem;
  color: #333333;
  font-weight: 400;
  margin: 0 0 12px 0;
  line-height: 1.4;
  height: 2.8em; 
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-price-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}

.card-price {
  font-size: 1.4rem;
  color: #333333;
  font-weight: 400;
}

.card-discount {
  font-size: 0.82rem;
  color: #00a650;
  font-weight: 600;
}

.card-shipping {
  font-size: 0.82rem;
  color: #00a650;
  font-weight: 600;
  margin: auto 0 0 0;
}

.empty-state {
  background: white;
  padding: 40px;
  border-radius: 8px;
  text-align: center;
  color: #666;
  box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}

/* Animación fade up secuencial para los elementos de la grilla */
.grid-fade-enter-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.grid-fade-enter-from {
  opacity: 0;
  transform: translateY(30px);
}
.grid-fade-move {
  transition: transform 0.4s ease;
}
</style>