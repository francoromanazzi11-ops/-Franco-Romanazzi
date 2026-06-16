<template>
  <div id="app">
    <HeaderComponent 
      :cart-items="carrito" 
      @execute-search="actualizarBusqueda" 
      @go-home="irAlHome" 
      @increase-qty="incrementarCantidad"
      @decrease-qty="decrementarCantidad"
      @execute-checkout="procesarCompra"
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
      carrito: [] 
    }
  },
  methods: {
    agregarAlCarrito(producto) {
      const itemExiste = this.carrito.find(item => item.id === producto.id);
      if (itemExiste) {
        itemExiste.cantidad++;
      } else {
        this.carrito.push({ ...producto, cantidad: 1 });
      }
    },
    incrementarCantidad(id) {
      const producto = this.carrito.find(item => item.id === id);
      if (producto) producto.cantidad++;
    },
    decrementarCantidad(id) {
      const index = this.carrito.findIndex(item => item.id === id);
      if (index !== -1) {
        if (this.carrito[index].cantidad > 1) {
          this.carrito[index].cantidad--;
        } else {
          this.carrito.splice(index, 1); // Si baja de 1, se remueve
        }
      }
    },
    procesarCompra() {
      alert("¡Redireccionando a la pasarela de pago para completar tu compra!");
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
        if (elementoGrid) elementoGrid.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 50);
    }
  }
}
</script>

<style>
html, body { margin: 0; padding: 0; width: 100%; background-color: #ededed; font-family: sans-serif; }
#app { display: flex; flex-direction: column; min-height: 100vh; }
.main-content { flex: 1; max-width: 1200px; width: 100%; margin: 0 auto; padding: 20px; box-sizing: border-box; }
</style>