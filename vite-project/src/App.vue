<template>
  <div class="app-layout">
    <Header 
      @cambiar-categoria="manejarCambioCategoria" 
      @actualizar-busqueda="textoBusqueda = $event" 
    />
    
    <main class="main-content">
      <Publicidad v-if="categoriaActual === 'inicio' && !textoBusqueda" />
      
      <HubCategorias 
        v-if="categoriaActual === 'inicio' && !textoBusqueda" 
        @seleccionar-categoria="manejarCambioCategoria" 
      />
      
      <ProductGrid 
        :category="categoriaActual" 
        :search="textoBusqueda" 
      />
    </main>
    
    <Footer @cambiar-categoria="manejarCambioCategoria" />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Publicidad from './components/Publicidad.vue'
import HubCategorias from './components/HubCategorias.vue'
import ProductGrid from './components/ProductGrid.vue'
import Footer from './components/Footer.vue'

export default {
  components: { Header, Publicidad, HubCategorias, ProductGrid, Footer },
  data() {
    return {
      categoriaActual: 'inicio',
      textoBusqueda: ''
    }
  },
  methods: {
    manejarCambioCategoria(cat) {
      this.categoriaActual = cat;
      this.textoBusqueda = ''; // Resetea el buscador al cambiar de sección
    }
  }
}
</script>

<style>
/* Estilos globales básicos de reseteo */
body {
  margin: 0;
  background-color: #f8fafc;
  font-family: system-ui, -apple-system, sans-serif;
}
.app-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.main-content {
  flex-grow: 1;
}
</style>