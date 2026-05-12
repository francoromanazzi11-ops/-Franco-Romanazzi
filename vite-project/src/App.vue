<script setup>
import { ref } from 'vue'
import Navbar from './components/napbar.vue'
import ProductGrid from './components/ProductGrid.vue'
import Publicidad from './components/Publicidad.vue'
import Footer from './components/Footer.vue'

const paginaActual = ref('inicio')
const ayudaActiva = ref(false)
const textoBusqueda = ref('')
const footerRef = ref(null)

const navegar = (seccion) => {
  // Al navegar, reseteamos la búsqueda
  textoBusqueda.value = '';
  
  if (seccion === 'ayuda') {
    ayudaActiva.value = true;
    setTimeout(() => {
      if (footerRef.value) footerRef.value.$el.scrollIntoView({ behavior: 'smooth' });
    }, 100);
    setTimeout(() => { ayudaActiva.value = false }, 3000);
  } else {
    paginaActual.value = seccion;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

const realizarBusqueda = (termino) => {
  if (termino.trim() !== '') {
    paginaActual.value = 'busqueda';
    textoBusqueda.value = termino.toLowerCase();
  } else {
    paginaActual.value = 'inicio';
    textoBusqueda.value = '';
  }
}
</script>

<template>
  <div id="app" :class="{ 'modo-ayuda': ayudaActiva }">
    <Navbar @cambiar-pagina="navegar" @buscar="realizarBusqueda" />

    <main class="main-content">
      <Publicidad v-if="paginaActual === 'inicio' && !textoBusqueda" />
      
      <ProductGrid 
        :category="paginaActual" 
        :search="textoBusqueda" 
      />
    </main>

    <Footer 
      ref="footerRef" 
      :expandir="ayudaActiva" 
      @cambiar-pagina="navegar" 
    />
  </div>
</template>

<style>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  padding-bottom: 50px;
  transition: filter 0.5s ease;
}

.modo-ayuda .main-content, 
.modo-ayuda .main-header {
  filter: blur(5px) grayscale(100%);
  pointer-events: none;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f4f4f4;
}
</style>