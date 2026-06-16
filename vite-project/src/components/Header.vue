<template>
  <header class="main-header">
    <div class="header-container">
      
      <div class="logo-area" @click="$emit('go-home')">
        <div class="logo-icon">⚡</div>
        <div class="logo-text">
          <h1>TECHSTORE</h1>
          <span>E-COMMERCE</span>
        </div>
      </div>

      <div class="search-area">
        <form @submit.prevent="enviarBusqueda" class=\"search-form\">
          <input 
            type="text" 
            v-model="query" 
            placeholder="Buscar productos, marcas y más..." 
            class="search-input"
          />
          <button type="submit" class="search-button">🔍</button>
        </form>
      </div>

      <div class="actions-area">
        <div class="promo-badge">
          👑 Suscribite a Tech+ por $2.999
        </div>
        
        <div class="cart-hub" @click="mostrarModalCarrito = true">
          <span class="cart-icon">🛒</span>
          <span class="cart-badge">{{ totalItems }}</span>
        </div>
      </div>

    </div>

    <CartSidebar 
      :isOpen="mostrarModalCarrito" 
      :items="cartItems" 
      @close="mostrarModalCarrito = false" 
      @increase-qty="$emit('increase-qty', $event)"
      @decrease-qty="$emit('decrease-qty', $event)"
      @checkout="$emit('execute-checkout')"
    />
  </header>
</template>

<script>
import CartSidebar from './CartSidebar.vue';

export default {
  name: 'HeaderComponent',
  components: {
    CartSidebar
  },
  props: {
    // Recibimos la lista completa de productos del carrito desde App.vue
    cartItems: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      query: '',
      mostrarModalCarrito: false
    }
  },
  computed: {
    totalItems() {
      return this.cartItems.reduce((acc, current) => acc + current.cantidad, 0);
    }
  },
  methods: {
    enviarBusqueda() {
      this.$emit('execute-search', this.query);
    }
  }
}
</script>

<style scoped>
.main-header { background-color: #0c2340; padding: 12px 0; color: white; position: sticky; top: 0; z-index: 5000; }
.header-container { max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; align-items: center; justify-content: space-between; }
.logo-area { display: flex; align-items: center; gap: 10px; cursor: pointer; }
.logo-icon { font-size: 1.8rem; }
.logo-text h1 { font-size: 1.3rem; margin: 0; font-weight: 800; }
.logo-text span { font-size: 0.65rem; color: #3483fa; display: block; }
.search-area { flex: 1; max-width: 550px; margin: 0 30px; }
.search-form { display: flex; background: white; border-radius: 4px; overflow: hidden; }
.search-input { flex: 1; border: none; padding: 10px; outline: none; }
.search-button { background: none; border: none; padding: 0 15px; cursor: pointer; }
.actions-area { display: flex; align-items: center; gap: 20px; }
.promo-badge { font-size: 0.85rem; background: rgba(255,255,255,0.1); padding: 6px 12px; border-radius: 20px; }
.cart-hub { position: relative; cursor: pointer; font-size: 1.4rem; }
.cart-badge { position: absolute; top: -5px; right: -10px; background: #3483fa; font-size: 0.75rem; padding: 2px 6px; border-radius: 50%; font-weight: 700; }
</style>