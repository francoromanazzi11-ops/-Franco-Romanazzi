<template>
  <div class="cart-modal-overlay" v-if="isOpen" @click.self="$emit('close')">
    <div class="cart-modal-box">
      <div class="cart-modal-header">
        <h3>Tu Carrito ({{ totalItems }})</h3>
        <button class="close-cart-btn" @click="$emit('close')">✕</button>
      </div>

      <div class="cart-modal-body" v-if="items.length > 0">
        <div v-for="item in items" :key="item.id" class="cart-item-row">
          <div class="cart-item-img">
            <img :src="item.img" :alt="item.title" />
          </div>
          <div class="cart-item-info">
            <h4>{{ item.title }}</h4>
            <p class="cart-item-vendor">Por: {{ item.vendor }}</p>
            <div class="cart-item-pricing">
              <span class="cart-item-qty">Cant: {{ item.cantidad }}</span>
              <span class="cart-item-subtotal">${{ (item.price * item.cantidad).toLocaleString('es-AR') }}</span>
            </div>
          </div>
        </div>
      </div>

      <div class="cart-modal-empty" v-else>
        <span class="empty-icon">🛒</span>
        <p>Tu carrito está vacío.</p>
        <p class="empty-sub text-green">¡Agregá productos de nuestro catálogo!</p>
      </div>

      <div class="cart-modal-footer" v-if="items.length > 0">
        <div class="total-row">
          <span>Total estimado:</span>
          <span class="total-price">${{ totalPrecio.toLocaleString('es-AR') }}</span>
        </div>
        <button class="checkout-btn" @click="finalizarCompra">Continuar compra</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CartSidebar',
  props: {
    isOpen: {
      type: Boolean,
      default: false
    },
    items: {
      type: Array,
      default: () => []
    }
  },
  computed: {
    totalItems() {
      return this.items.reduce((total, item) => total + item.cantidad, 0);
    },
    totalPrecio() {
      return this.items.reduce((total, item) => total + (item.price * item.cantidad), 0);
    }
  },
  methods: {
    finalizarCompra() {
      alert('¡Redireccionando a la pasarela de pago seguro!');
      this.$emit('close');
    }
  }
}
</script>

<style scoped>
.cart-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
  display: flex;
  justify-content: flex-end;
  z-index: 3000;
}

.cart-modal-box {
  background-color: #ffffff;
  width: 100%;
  max-width: 420px;
  height: 100vh;
  display: flex;
  flex-direction: column;
  box-shadow: -5px 0 25px rgba(0,0,0,0.15);
  animation: slideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideIn {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}

.cart-modal-header {
  padding: 20px;
  border-bottom: 1px solid #eeeeee;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #f9f9f9;
}
.cart-modal-header h3 { margin: 0; font-size: 1.15rem; color: #333333; font-weight: 600; }
.close-cart-btn { background: none; border: none; font-size: 1.1rem; color: #666; cursor: pointer; }

.cart-modal-body { flex: 1; overflow-y: auto; padding: 15px; display: flex; flex-direction: column; gap: 15px; }

.cart-item-row {
  display: flex;
  gap: 12px;
  padding-bottom: 15px;
  border-bottom: 1px solid #f2f2f2;
  align-items: center;
  text-align: left;
}
.cart-item-img {
  width: 65px;
  height: 65px;
  padding: 5px;
  border: 1px solid #eaeaea;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff;
}
.cart-item-img img { max-width: 100%; max-height: 100%; object-fit: contain; }

.cart-item-info { flex: 1; display: flex; flex-direction: column; }
.cart-item-info h4 {
  margin: 0 0 4px 0;
  font-size: 0.85rem;
  color: #333;
  font-weight: 500;
  line-height: 1.3;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.cart-item-vendor { margin: 0 0 6px 0; font-size: 0.72rem; color: #999; text-transform: uppercase; }

.cart-item-pricing { display: flex; justify-content: space-between; align-items: center; margin-top: auto; }
.cart-item-qty { font-size: 0.8rem; color: #666; background: #f0f0f0; padding: 2px 8px; border-radius: 12px; }
.cart-item-subtotal { font-size: 0.95rem; color: #333; font-weight: 600; }

.cart-modal-empty { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px; color: #666; }
.empty-icon { font-size: 3.5rem; margin-bottom: 15px; opacity: 0.4; }
.empty-sub { font-size: 0.82rem; margin-top: 5px; font-weight: 500; }
.text-green { color: #00a650; }

.cart-modal-footer { padding: 20px; border-top: 1px solid #eeeeee; background: #f9f9f9; box-sizing: border-box; }
.total-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; font-size: 1rem; color: #333; font-weight: 500; }
.total-price { font-size: 1.4rem; color: #333; font-weight: 600; }

.checkout-btn {
  width: 100%;
  background-color: #3483fa;
  color: #ffffff;
  border: none;
  padding: 14px;
  font-size: 0.95rem;
  font-weight: 600;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s;
}
.checkout-btn:hover { background-color: #1f6cd7; }
</style>