<template>
  <div id="app">
    <!-- Header principal expandido -->
    <HeaderComponent @execute-search="actualizarBusqueda" @go-home="irAlHome" />

    <!-- Barra de Marcas destacadas expandida -->
    <MarcasComponent />

    <!-- Sub-Header / Menú expandido -->
    <MenuComponent @change-category="cambiarCategoria" />

    <!-- Carrusel y Beneficios expandidos de fondo -->
    <div v-if="categoriaSeleccionada === 'inicio' && !terminoBusqueda" class="hero-section">
      <PublicidadComponent />
      <BeneficiosComponent />
    </div>

    <!-- Hub de Categorías (Centrado pero en contenedor fluido) -->
    <HubCategorias :currentCategory="categoriaSeleccionada" @change-category="cambiarCategoria" />

    <!-- Grilla de Productos Dinámica -->
    <main class="main-content">
      <ProductGrid :category="categoriaSeleccionada" :search="terminoBusqueda" />
    </main>

    <!-- Pie de página expandido -->
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from './components/Header.vue';
import MarcasComponent from './components/Marcas.vue';
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
    MarcasComponent,
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
      terminoBusqueda: ''
    }
  },
  methods: {
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
  overflow-x: hidden; /* Clave absoluta para evitar desbordes laterales */
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

a, button {
  transition: all 0.2s ease;
}

::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: #f1f1f1;
}
::-webkit-scrollbar-thumb {
  background: #c1c1c1;
  border-radius: 4px;
}
</style>