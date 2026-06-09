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
        <form @submit.prevent="enviarBusqueda" class="search-form">
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
    />
  </header>
</template>

<script>
// Importamos el componente independiente
import CartSidebar from './CartSidebar.vue';

export default {
  name: 'HeaderComponent',
  components: {
    CartSidebar
  },
  props: {
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
      return this.cartItems.reduce((total, item) => total + item.cantidad, 0);
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
.main-header {
  width: 100%;
  background-color: #0c2340;
  padding: 12px 0;
  box-sizing: border-box;
  border-bottom: 1px solid rgba(255,255,255,0.1);
  position: relative;
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
}

.logo-area {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}

.logo-icon { font-size: 1.8rem; }
.logo-text h1 { font-size: 1.3rem; color: #ffffff; margin: 0; font-weight: 800; letter-spacing: 0.5px; }
.logo-text span { font-size: 0.65rem; color: #3483fa; font-weight: 700; display: block; letter-spacing: 1px; }

.search-area { flex: 1; max-width: 550px; margin: 0 30px; }
.search-form { display: flex; background-color: #ffffff; border-radius: 4px; overflow: hidden; box-shadow: 0 1px 2px rgba(0,0,0,0.1); }
.search-input { flex: 1; border: none; padding: 10px 15px; font-size: 0.88rem; outline: none; color: #333333; }
.search-button { background: none; border: none; padding: 0 15px; cursor: pointer; font-size: 0.95rem; border-left: 1px solid #e6e6e6; }

.actions-area { display: flex; align-items: center; gap: 25px; }
.promo-badge { color: #ffffff; font-size: 0.8rem; background-color: rgba(255,255,255,0.08); padding: 6px 12px; border-radius: 20px; font-weight: 500; }

.cart-hub { position: relative; cursor: pointer; display: flex; align-items: center; }
.cart-icon { font-size: 1.5rem; }
.cart-badge {
  position: absolute; top: -6px; right: -10px; background-color: #3483fa; color: #ffffff;
  font-size: 0.72rem; font-weight: 700; border-radius: 10px; padding: 2px 6px; min-width: 12px;
  text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.3);
}
</style>