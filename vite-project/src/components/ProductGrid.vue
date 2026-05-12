<template>
  <section class="container">
    <h2 class="section-title">
      {{ search ? 'Resultados para: "' + search + '"' : (category === 'inicio' ? 'Productos Destacados' : category.toUpperCase()) }}
    </h2>

    <div v-if="filteredProducts.length > 0" class="product-grid">
      <div v-for="product in filteredProducts" :key="product.id" class="product-card">
        <div v-if="product.discount" class="discount-badge">{{ product.discount }}% OFF</div>
        
        <div class="product-image">
          <div class="img-placeholder">IMAGEN PRODUCTO</div>
        </div>

        <div class="product-info">
          <h3 class="product-name">{{ product.name }}</h3>
          <div v-if="product.discount" class="price-container">
            <p class="current-price">{{ calcularDescuento(product.price, product.discount) }}</p>
            <p class="original-price">{{ product.price }}</p>
          </div>
          <p v-else class="current-price">{{ product.price }}</p>
        </div>
      </div>
    </div>

    <div v-else class="no-results">
      <div class="warning-icon">⚠️</div>
      <p>No se encontró ningún artículo relacionado con <strong>"{{ search }}"</strong>.</p>
      <span>Intenta con palabras como "computadora", "celular" o "monitor".</span>
    </div>
  </section>
</template>

<script>
export default {
  props: ['category', 'search'],
  data() {
    return {
      products: [
        { id: 1, name: 'Laptop Pro X', price: '$ 850.000', category: 'computadoras', mostrarEnInicio: true, discount: 40, tags: ['pc', 'computadora', 'laptop'] },
        { id: 2, name: 'Smartphone Z', price: '$ 420.000', category: 'celulares', mostrarEnInicio: true, discount: 40, tags: ['celular', 'telefono', 'movil'] },
        { id: 3, name: 'PC Desktop Gamer', price: '$ 1.200.000', category: 'computadoras', mostrarEnInicio: true, tags: ['pc', 'gamer', 'escritorio'] },
        { id: 4, name: 'MacBook Air M2', price: '$ 2.500.000', category: 'computadoras', mostrarEnInicio: true, tags: ['apple', 'laptop', 'mac'] },
        { id: 5, name: 'iPhone 15 Pro', price: '$ 1.800.000', category: 'celulares', mostrarEnInicio: true, tags: ['apple', 'iphone', 'celular'] },
        { id: 6, name: 'Samsung Galaxy S24', price: '$ 1.650.000', category: 'celulares', mostrarEnInicio: true, tags: ['samsung', 'celular', 'android'] },
        { id: 7, name: 'Auriculares Hi-Fi', price: '$ 45.000', category: 'otros', mostrarEnInicio: true, discount: 40, tags: ['audio', 'musica', 'auricular'] },
        { id: 8, name: 'Monitor 4K 27"', price: '$ 180.000', category: 'computadoras', mostrarEnInicio: true, tags: ['monitor', 'pantalla', '4k'] },
        { id: 9, name: 'Teclado Mecánico RGB', price: '$ 35.000', category: 'otros', mostrarEnInicio: false, tags: ['teclado', 'gamer'] },
        { id: 10, name: 'Mouse Gamer Wireless', price: '$ 22.000', category: 'otros', mostrarEnInicio: false, tags: ['mouse', 'gamer'] }
      ]
    }
  },
  computed: {
    filteredProducts() {
      let list = this.products;

      // Si el usuario está buscando algo por texto
      if (this.search) {
        return list.filter(p => {
          const s = this.search.toLowerCase();
          return p.name.toLowerCase().includes(s) || 
                 p.category.toLowerCase().includes(s) || 
                 p.tags.some(t => t.includes(s));
        });
      }

      // Si el usuario navega por categorías
      if (this.category === 'inicio') return list.filter(p => p.mostrarEnInicio);
      if (this.category === 'ofertas') return list.filter(p => p.discount);
      
      return list.filter(p => p.category === this.category);
    }
  },
  methods: {
    calcularDescuento(precioStr, descuento) {
      const precio = parseInt(precioStr.replace(/[^0-9]/g, ''));
      const final = precio * (1 - descuento / 100);
      return '$ ' + final.toLocaleString('es-AR');
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.section-title {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

/* GRID QUE SE AJUSTA SOLO PARA NO DEJAR HUECOS */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 25px;
}

.product-card {
  background: white;
  border-radius: 8px;
  padding: 15px;
  border: 1px solid #eee;
  position: relative;
  transition: transform 0.3s ease;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.img-placeholder {
  width: 100%;
  height: 180px;
  background: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #aaa;
  font-size: 0.8rem;
  border-radius: 4px;
}

.discount-badge {
  position: absolute;
  top: 10px;
  left: 10px;
  background: #00a650;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-weight: bold;
  font-size: 0.8rem;
  z-index: 10;
}

.product-info {
  margin-top: 15px;
  text-align: center;
}

.product-name {
  font-size: 1.1rem;
  color: #333;
  margin: 10px 0;
}

.current-price {
  font-size: 1.3rem;
  font-weight: bold;
  color: #222;
  margin: 0;
}

.original-price {
  font-size: 0.9rem;
  color: #999;
  text-decoration: line-through;
}

/* ESTILOS DE NO RESULTADOS */
.no-results {
  text-align: center;
  padding: 60px 20px;
  color: #666;
}

.warning-icon {
  font-size: 3.5rem;
  margin-bottom: 15px;
}

.no-results p {
  font-size: 1.2rem;
  margin-bottom: 5px;
}
</style>