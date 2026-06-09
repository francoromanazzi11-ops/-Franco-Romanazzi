<template>
  <div class="grid-section">
    <div class="grid-container">
      <h3 class="section-title">{{ tituloSeccion }}</h3>
      
      <div class="products-layout" v-if="productosFiltrados.length > 0">
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
      </div>

      <div class="empty-state" v-else>
        <p>No encontramos productos que coincidan con tu selección.</p>
      </div>
    </div>

    <ProductDetailWindow 
      :isOpen="modalAbierto" 
      :product="productoSeleccionado" 
      @close="cerrarDetalle" 
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
      modalAbierto: false,
      productoSeleccionado: null,
      todosLosProductos: [
        { id: 1, category: 'computadoras', title: 'Notebook ASUS Vivobook 15 OLED AMD Ryzen 7', price: 849000, discount: 15, vendor: 'MEGA HARDWARE', img: 'https://images.unsplash.com/photo-1593642632823-8f785ba67e45?q=80&w=400' },
        { id: 6, category: 'computadoras', title: 'MacBook Air 13 M2 8GB 256GB SSD Liquid Retina', price: 1850000, discount: null, vendor: 'APPLE OFFICIAL', img: 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=400' },
        { id: 7, category: 'computadoras', title: 'Notebook Lenovo IdeaPad Slim 3 Intel Core i5', price: 620000, discount: 10, vendor: 'MUNDO DIGITAL', img: 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?q=80&w=400' },
        { id: 8, category: 'computadoras', title: 'PC Armada Intel i7 16GB RAM SSD 1TB Rtx 4060', price: 1250000, discount: 5, vendor: 'MEGA HARDWARE', img: 'https://images.unsplash.com/photo-1587202372775-e229f172b9d7?q=80&w=400' },
        { id: 2, category: 'celulares', title: 'ZTE Blade A56 Pro Gray Cargador+Auri+Funda De Regalo', price: 223196, discount: 25, vendor: 'MUNDO DIGITAL', img: 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=400' },
        { id: 5, category: 'celulares', title: 'Motorola Edge 40 Neo 128GB Negro Absoluto Libre', price: 460000, discount: null, vendor: 'GIGA COMPUTACIÓN', img: 'https://images.unsplash.com/photo-1598327105666-5b89351aff97?q=80&w=400' },
        { id: 9, category: 'celulares', title: 'iPhone 15 Pro Max 256GB Titanium Natural Libre', price: 2450000, discount: null, vendor: 'APPLE OFFICIAL', img: 'https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?q=80&w=400' },
        { id: 10, category: 'celulares', title: 'Samsung Galaxy S24 Ultra 512GB Titanium Black', price: 1980000, discount: 12, vendor: 'MUNDO DIGITAL', img: 'https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?q=80&w=400' },
        { id: 3, category: 'audio', title: 'Auriculares Sony WH-1000XM4 Noise Cancelling ANC', price: 399000, discount: 20, vendor: 'MEGA HARDWARE', img: 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=400' },
        { id: 11, category: 'audio', title: 'Parlante Portátil JBL Flip 6 Bluetooth Impermeable', price: 185000, discount: null, vendor: 'MUNDO DIGITAL', img: 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?q=80&w=400' },
        { id: 12, category: 'audio', title: 'Auriculares In-Ear Apple AirPods Pro 2da Generación', price: 420000, discount: 8, vendor: 'APPLE OFFICIAL', img: 'https://images.unsplash.com/photo-1588444837495-c6cfeb53f32d?q=80&w=400' },
        { id: 13, category: 'audio', title: 'Home Theater Soundbar Samsung T450 200W Subwoofer', price: 310000, discount: 18, vendor: 'GIGA COMPUTACIÓN', img: 'https://images.unsplash.com/photo-1545454675-3531b543be5d?q=80&w=400' },
        { id: 4, category: 'gaming', title: 'Teclado Mecánico Giga RGB Switch Red Pro Layout', price: 74500, discount: 10, vendor: 'GIGA COMPUTACIÓN', img: 'https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?q=80&w=400' },
        { id: 14, category: 'gaming', title: 'Consola PlayStation 5 Slim 1TB con Joystick DualSense', price: 1150000, discount: null, vendor: 'MEGA HARDWARE', img: 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?q=80&w=400' },
        { id: 15, category: 'gaming', title: 'Mouse Gamer Logitech G502 Hero 25K Alta Precisión', price: 68000, discount: 30, vendor: 'GIGA COMPUTACIÓN', img: 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?q=80&w=400' },
        { id: 16, category: 'gaming', title: 'Monitor Gamer Samsung Odyssey G4 24" IPS 240Hz 1ms', price: 495000, discount: 15, vendor: 'MEGA HARDWARE', img: 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?q=80&w=400' }
      ]
    }
  },
  computed: {
    tituloSeccion() {
      if (this.search) return `Resultados para "${this.search}"`;
      if (this.category === 'inicio') return 'Inspirado en tus favoritos';
      if (this.category === 'ofertas') return '🔥 Grandes Ofertas y Descuentos';
      return `Catálogo de ${this.category.charAt(0).toUpperCase() + this.category.slice(1)}`;
    },
    productosFiltrados() {
      let lista = this.todosLosProductos;
      if (this.search) {
        return lista.filter(p => p.title.toLowerCase().includes(this.search.toLowerCase()));
      }
      if (this.category === 'ofertas') {
        return lista.filter(p => p.discount !== null && p.discount > 0);
      }
      if (this.category !== 'inicio' && this.category !== '') {
        return lista.filter(p => p.category === this.category);
      }
      return lista.slice(0, 8);
    }
  },
  methods: {
    abrirDetalle(producto) {
      this.productoSeleccionado = producto;
      this.modalAbierto = true;
    },
    cerrarDetalle() {
      this.modalAbierto = false;
      this.productoSeleccionado = null;
    },
    reenviarAlPadre(producto) {
      // Dispara el evento exacto que tu App.vue original está escuchando
      this.$emit('add-to-cart', producto);
    }
  }
}
</script>

<style scoped>
.grid-section {
  width: 100%;
  box-sizing: border-box;
}

.grid-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  text-align: left;
  box-sizing: border-box;
}

.section-title {
  font-size: 1.5rem;
  font-weight: 400;
  color: #333333;
  margin-bottom: 25px;
}

.products-layout {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 20px;
}

.product-card {
  background-color: #ffffff;
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid #ededed;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  height: 390px;
  transition: transform 0.2s cubic-bezier(0.215, 0.610, 0.355, 1), box-shadow 0.2s;
}

.product-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.08);
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
  margin-top: auto;
  margin-bottom: 8px;
}

.card-price {
  font-size: 1.4rem;
  color: #333333;
  font-weight: 400;
}

.card-discount {
  font-size: 0.8rem;
  color: #00a650;
  font-weight: 600;
  background-color: rgba(0, 166, 80, 0.1);
  padding: 2px 6px;
  border-radius: 4px;
}

.card-shipping {
  font-size: 0.78rem;
  color: #00a650;
  font-weight: 600;
  margin: 0;
}

.empty-state {
  text-align: center;
  padding: 80px 20px;
  background: #fff;
  border-radius: 6px;
  border: 1px solid #ededed;
  color: #666;
  font-size: 1.1rem;
}
</style>