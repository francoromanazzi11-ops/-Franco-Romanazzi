<template>
  <div class="modal-overlay" v-if="isOpen" @click.self="$emit('close')">
    <div class="detail-box">
      <button class="close-btn" @click="$emit('close')">✕</button>

      <div class="detail-columns" v-if="product">
        <div class="image-column">
          <div class="main-img-wrapper">
            <img :src="product.img" :alt="product.title" />
          </div>
        </div>

        <div class="info-column">
          <p class="product-condition">Nuevo | +100 vendidos</p>
          <h2 class="product-title">{{ product.title }}</h2>
          <p class="product-vendor">Vendido por <span class="vendor-highlight">{{ product.vendor }}</span></p>

          <div class="price-section">
            <div class="price-row">
              <span class="current-price">${{ product.price.toLocaleString('es-AR') }}</span>
              <span v-if="product.discount" class="discount-badge">{{ product.discount }}% OFF</span>
            </div>
            <p class="payment-info">en 12x de ${{ Math.round((product.price * 1.15) / 12).toLocaleString('es-AR') }} pagando con Mercado Pago</p>
          </div>

          <div class="shipping-benefit-box">
            <span class="truck-icon">⚡</span>
            <div class="shipping-text">
              <p class="green-text">Envío gratis a todo el país con FULL</p>
              <p class="sub-text">Llega mañana de forma segura a tu domicilio</p>
            </div>
          </div>

          <div class="actions-section">
            <button class="buy-now-btn" @click="comprarDirecto">
              Comprar ahora
            </button>
            <button class="add-to-cart-btn" @click="agregarAlCarrito">
              Agregar al carrito
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductDetailWindow',
  props: {
    isOpen: {
      type: Boolean,
      default: false
    },
    product: {
      type: Object,
      default: null
    }
  },
  methods: {
    agregarAlCarrito() {
      if (this.product) {
        // Emitimos el evento que va a viajar al grid y luego a App.vue
        this.$emit('add-to-cart', this.product);
        this.$emit('close');
      }
    },
    comprarDirecto() {
      if (this.product) {
        alert(`Procediendo a la compra rápida de: ${this.product.title}`);
        this.$emit('close');
      }
    }
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 4000;
  padding: 20px;
  box-sizing: border-box;
}

.detail-box {
  background-color: #ffffff;
  width: 100%;
  max-width: 860px;
  border-radius: 8px;
  position: relative;
  padding: 30px;
  box-sizing: border-box;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  animation: fadeIn 0.2s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}

.close-btn {
  position: absolute;
  top: 15px;
  right: 15px;
  background: none;
  border: none;
  font-size: 1.2rem;
  color: #666;
  cursor: pointer;
  z-index: 10;
}

.detail-columns {
  display: flex;
  gap: 30px;
}

.image-column {
  flex: 1.2;
  display: flex;
  align-items: center;
  justify-content: center;
}

.main-img-wrapper {
  width: 100%;
  max-height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #f0f0f0;
  border-radius: 4px;
  padding: 15px;
}

.main-img-wrapper img {
  max-width: 100%;
  max-height: 350px;
  object-fit: contain;
}

.info-column {
  flex: 1;
  display: flex;
  flex-direction: column;
  text-align: left;
}

.product-condition {
  font-size: 0.75rem;
  color: #666;
  margin: 0 0 5px 0;
}

.product-title {
  font-size: 1.4rem;
  font-weight: 600;
  color: #333;
  margin: 0 0 8px 0;
  line-height: 1.3;
}

.product-vendor {
  font-size: 0.82rem;
  color: #666;
  margin: 0 0 20px 0;
}

.vendor-highlight {
  color: #3483fa;
  font-weight: 500;
}

.price-section {
  border-top: 1px solid #f0f0f0;
  padding-top: 15px;
  margin-bottom: 20px;
}

.price-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.current-price {
  font-size: 2rem;
  color: #333;
  font-weight: 300;
}

.discount-badge {
  font-size: 0.88rem;
  color: #00a650;
  font-weight: 600;
}

.payment-info {
  font-size: 0.82rem;
  color: #666;
  margin: 4px 0 0 0;
}

.shipping-benefit-box {
  background-color: #f6f6f6;
  border-radius: 6px;
  padding: 12px 15px;
  display: flex;
  gap: 12px;
  align-items: flex-start;
  margin-bottom: 25px;
}

.truck-icon {
  font-size: 1.3rem;
  color: #00a650;
}

.shipping-text p {
  margin: 0;
}

.shipping-text .green-text {
  font-size: 0.88rem;
  color: #00a650;
  font-weight: 600;
}

.shipping-text .sub-text {
  font-size: 0.78rem;
  color: #666;
  margin-top: 2px;
}

.actions-section {
  margin-top: auto;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.buy-now-btn {
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

.buy-now-btn:hover {
  background-color: #1f6cd7;
}

.add-to-cart-btn {
  width: 100%;
  background-color: rgba(65, 137, 230, 0.15);
  color: #3483fa;
  border: none;
  padding: 14px;
  font-size: 0.95rem;
  font-weight: 600;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s, color 0.2s;
}

.add-to-cart-btn:hover {
  background-color: #3483fa;
  color: #ffffff;
}
</style>