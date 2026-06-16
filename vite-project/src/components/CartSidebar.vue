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
            <h4 class="cart-item-title">{{ item.title }}</h4>
            <p class="cart-item-vendor">Por: {{ item.vendor }}</p>
            
            <div class="cart-item-pricing">
              <div class="quantity-controls">
                <button class="qty-btn" @click="$emit('decrease-qty', item.id)">-</button>
                <span class="cart-item-qty">{{ item.cantidad }} u.</span>
                <button class="qty-btn" @click="$emit('increase-qty', item.id)">+</button>
              </div>
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
          <span>Total:</span>
          <span class="total-price">${{ totalPrecio.toLocaleString('es-AR') }}</span>
        </div>
        <button class="buy-btn" @click="$emit('checkout')">Continuar compra</button>
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
      return this.items.reduce((acc, current) => acc + current.cantidad, 0);
    },
    totalPrecio() {
      return this.items.reduce((acc, current) => acc + (current.price * current.cantidad), 0);
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
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(2px);
  z-index: 9999; /* Asegura que flote por encima de todo */
}

.cart-modal-box {
  position: absolute;
  top: 0;
  right: 0;
  background-color: #ffffff;
  width: 100%;
  max-width: 440px;
  height: 100%;
  box-shadow: -5px 0 25px rgba(0,0,0,0.2);
  display: flex;
  flex-direction: column;
}

.cart-modal-header {
  padding: 20px;
  border-bottom: 1px solid #eeeeee;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f9f9f9;
}

.cart-modal-header h3 {
  margin: 0;
  font-size: 1.2rem;
  color: #333333;
  font-weight: 600;
}

.close-cart-btn {
  background: none;
  border: none;
  font-size: 1.4rem;
  color: #666;
  cursor: pointer;
  padding: 5px 10px;
  transition: color 0.2s ease;
}

.close-cart-btn:hover {
  color: #000000;
}

.cart-modal-body {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}

.cart-item-row {
  display: flex;
  align-items: center;
  gap: 15px;
  border-bottom: 1px solid #f0f0f0;
  padding-bottom: 15px;
  margin-bottom: 15px;
}

.cart-item-img {
  width: 75px;
  height: 75px;
  border: 1px solid #ededed;
  border-radius: 6px;
  padding: 5px;
  background: white;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.cart-item-img img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.cart-item-info {
  flex: 1;
  text-align: left;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 75px;
}

.cart-item-title {
  margin: 0 0 4px 0;
  font-size: 0.9rem;
  color: #333333;
  font-weight: 500;
  line-height: 1.3;
}

.cart-item-vendor {
  margin: 0 0 8px 0;
  font-size: 0.72rem;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.cart-item-pricing {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Panel de Controles de Cantidad (+ / -) */
.quantity-controls {
  display: flex;
  align-items: center;
  background-color: #f3f4f6;
  border-radius: 6px;
  border: 1px solid #e5e7eb;
  overflow: hidden;
}

.qty-btn {
  background: none;
  border: none;
  width: 28px;
  height: 28px;
  font-size: 1rem;
  font-weight: 600;
  color: #4b5563;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.15s ease;
}

.qty-btn:hover {
  background-color: #e5e7eb;
  color: #111111;
}

.cart-item-qty {
  font-size: 0.82rem;
  font-weight: 600;
  color: #374151;
  min-width: 32px;
  text-align: center;
}

.cart-item-subtotal {
  font-size: 1rem;
  color: #333;
  font-weight: 600;
}

/* Estado de carrito vacío */
.cart-modal-empty {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px;
  color: #666;
}

.empty-icon {
  font-size: 3.5rem;
  margin-bottom: 15px;
  opacity: 0.4;
}

.empty-sub {
  font-size: 0.85rem;
  margin-top: 5px;
  font-weight: 500;
}

.text-green {
  color: #00a650;
}

/* Pie del modal */
.cart-modal-footer {
  padding: 20px;
  border-top: 1px solid #eeeeee;
  background-color: #f9f9f9;
}

.total-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 15px;
  color: #333;
}

.total-price {
  color: #111111;
}

.buy-btn {
  width: 100%;
  background-color: #3483fa;
  color: #ffffff;
  border: none;
  padding: 15px;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.buy-btn:hover {
  background-color: #1f6cd7;
}
</style>