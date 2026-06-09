<template>
  <div id="app">
    <HeaderComponent 
      :cart-count="totalItemsCarrito" 
      @execute-search="actualizarBusqueda" 
      @go-home="irAlHome" 
    />

    <MenuComponent @change-category="cambiarCategoria" />

    <div v-if="categoriaSeleccionada === 'inicio' && !terminoBusqueda" class="hero-section">
      <PublicidadComponent />
      <BeneficiosComponent />
    </div>

    <HubCategorias :currentCategory="categoriaSeleccionada" @change-category="cambiarCategoria" />

    <main class="main-content">
      <ProductGrid 
        :category="categoriaSeleccionada" 
        :search="terminoBusqueda" 
        @add-to-cart="agregarAlCarrito"
      />
    </main>

    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from './components/Header.vue';
import MenuComponent from './components/menu.vue';
import PublicidadComponent from './components/Publicidad.vue';
import BeneficiosComponent from './components/Beneficios.vue';
import HubCategorias from './components/HubCategorias.vue';
import ProductGrid from './components/ProductGrid.vue';
import FooterComponent from './components/Footer.vue';

export default {
  name: 'App',
  components: {
    HeaderComponent,
    MenuComponent,
    PublicidadComponent,
    BeneficiosComponent,
    HubCategorias,
    ProductGrid,
    FooterComponent
  },
  data() {
    return {
      categoriaSeleccionada: 'inicio',
      terminoBusqueda: '',
      // Array donde se guardan los productos agregados
      carrito: []
    }
  },
  computed: {
    // Suma dinámicamente las cantidades de todos los productos en el carrito
    totalItemsCarrito() {
      return this.carrito.reduce((total, item) => total + item.cantidad, 0);
    }
  },
  methods: {
    agregarAlCarrito(producto) {
      // Verificamos si el producto ya estaba en el carrito
      const itemExiste = this.carrito.find(item => item.id === producto.id);
      
      if (itemExiste) {
        // Si ya existe, incrementamos su cantidad
        itemExiste.cantidad++;
      } else {
        // Si es nuevo, lo agregamos esparciendo sus propiedades junto a cantidad: 1
        this.carrito.push({
          ...producto,
          cantidad: 1
        });
      }
      console.log('Contenido del carrito actual:', this.carrito);
    },
    cambiarCategoria(catId) {
      this.categoriaSeleccionada = catId;
      this.terminoBusqueda = ''; 
      this.hacerScrollAlCatalogo();
    },
    actualizarBusqueda(query) {
      this.terminoBusqueda = query;
      this.categoriaSeleccionada = ''; 
      this.hacerScrollAlCatalogo();
    },
    irAlHome() {
      this.categoriaSeleccionada = 'inicio';
      this.terminoBusqueda = '';
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },
    hacerScrollAlCatalogo() {
      setTimeout(() => {
        const elementoGrid = document.querySelector('.main-content');
        if (elementoGrid) {
          elementoGrid.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }, 50);
    }
  }
}
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  background-color: #ededed;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  min-height: 100vh;
  overflow-x: hidden;
}

#app {
  width: 100%;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.hero-section {
  width: 100%;
}

.main-content {
  flex: 1;
  width: 100%;
  box-sizing: border-box;
  padding-bottom: 50px;
  margin-top: 20px;
}
</style>