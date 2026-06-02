<template>
  <transition name="modal-fade">
    <div v-if="isOpen" class="modal-overlay" @click.self="cerrar">
      <div class="modal-window">
        <button class="close-btn" @click="cerrar">✕</button>

        <div class="modal-body" v-if="product">
          <div class="gallery-side">
            <div class="thumbnails">
              <div class="thumb-box active">
                <img :src="product.img" :alt="product.title" />
              </div>
              <div class="thumb-box" v-for="n in 2" :key="n"></div>
            </div>
            <div class="main-image-container">
              <img :src="product.img" :alt="product.title" class="main-img" />
            </div>
          </div>

          <div class="info-side">
            <span class="product-status">Nuevo | +25 vendidos</span>
            <h1 class="product-title">{{ product.title }}</h1>
            
            <div class="rating-box">
              <span class="stars">★★★★★</span>
              <span class="rating-text">4.8 (186 opiniones)</span>
            </div>

            <div class="price-section">
              <span v-if="product.discount" class="old-price">
                ${{ Math.round(product.price * 1.2).toLocaleString('es-AR') }}
              </span>
              <div class="current-price-row">
                <span class="price-value">${{ product.price.toLocaleString('es-AR') }}</span>
                <span v-if="product.discount" class="discount-badge">{{ product.discount }}% OFF</span>
              </div>
              <p class="installments">Mismo precio en 6 cuotas de ${{ Math.round(product.price / 6).toLocaleString('es-AR') }}</p>
            </div>

            <div class="shipping-info">
              <p class="shipping-green">
                <span class="icon">⚡</span> Llega gratis mañana <span class="subtext">por ser tu primera compra</span>
              </p>
              <p class="stock-status">Stock disponible</p>
              <p class="vendor-text">Vendido por: <span class="vendor-name">{{ product.vendor }}</span></p>
            </div>

            <div class="actions-box">
              <button class="btn-primary" @click="comprar">Comprar ahora</button>
              <button class="btn-secondary">Agregar al carrito</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
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
    cerrar() {
      this.$emit('close');
    },
    comprar() {
      alert(`Procediendo a la compra de: ${this.product.title}`);
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
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
  backdrop-filter: blur(2px);
}

.modal-window {
  background-color: #ffffff;
  width: 90%;
  max-width: 1000px;
  max-height: 90vh;
  border-radius: 8px;
  position: relative;
  overflow-y: auto;
  box-shadow: 0 10px 30px rgba(0,0,0,0.3);
  padding: 30px;
  box-sizing: border-box;
}

.close-btn {
  position: absolute;
  top: 15px;
  right: 20px;
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #666;
  cursor: pointer;
  z-index: 10;
}
.close-btn:hover { color: #000; }

.modal-body {
  display: flex;
  gap: 40px;
}

/* GALERÍA IZQUIERDA */
.gallery-side {
  flex: 1.2;
  display: flex;
  gap: 15px;
}

.thumbnails {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.thumb-box {
  width: 50px;
  height: 50px;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
  overflow: hidden;
}
.thumb-box.active, .thumb-box:hover {
  border-color: #3483fa;
  box-shadow: 0 0 0 1px #3483fa;
}
.thumb-box img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.main-image-container {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #f0f0f0;
  border-radius: 4px;
  padding: 10px;
  background: #fff;
}

.main-img {
  max-width: 100%;
  max-height: 380px;
  object-fit: contain;
}

/* INFORMACIÓN DERECHA */
.info-side {
  flex: 1;
  text-align: left;
  display: flex;
  flex-direction: column;
}

.product-status {
  font-size: 0.8rem;
  color: #666;
}

.product-title {
  font-size: 1.4rem;
  font-weight: 600;
  color: #333;
  margin: 8px 0;
  line-height: 1.2;
}

.rating-box {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 15px;
}
.stars { color: #3483fa; font-size: 0.9rem; }
.rating-text { font-size: 0.8rem; color: #666; }

.price-section {
  border-top: 1px solid #f0f0f0;
  padding-top: 15px;
  margin-bottom: 20px;
}

.old-price {
  font-size: 0.9rem;
  color: #999;
  text-decoration: line-through;
}

.current-price-row {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 2px;
}

.price-value {
  font-size: 2.2rem;
  font-weight: 300;
  color: #333;
}

.discount-badge {
  font-size: 0.85rem;
  color: #00a650;
  font-weight: 600;
}

.installments {
  font-size: 0.85rem;
  color: #00a650;
  margin: 4px 0 0 0;
}

.shipping-info {
  background-color: #f6f6f6;
  border-radius: 6px;
  padding: 14px;
  margin-bottom: 20px;
}

.shipping-green {
  font-size: 0.9rem;
  color: #00a650;
  font-weight: 600;
  margin: 0 0 4px 0;
}
.shipping-green .subtext { color: #666; font-weight: 400; }

.stock-status { font-size: 0.9rem; font-weight: 600; color: #333; margin: 8px 0 4px 0; }
.vendor-text { font-size: 0.8rem; color: #666; margin: 0; }
.vendor-name { color: #3483fa; font-weight: 500; }

.actions-box {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: auto;
}

.btn-primary, .btn-secondary {
  width: 100%;
  padding: 14px;
  font-size: 0.95rem;
  font-weight: 600;
  border-radius: 6px;
  cursor: pointer;
  border: none;
}

.btn-primary {
  background-color: #3483fa;
  color: #ffffff;
}
.btn-primary:hover { background-color: #2968c8; }

.btn-secondary {
  background-color: rgba(65, 137, 245, 0.15);
  color: #3483fa;
}
.btn-secondary:hover { background-color: rgba(65, 137, 245, 0.25); }

/* Animaciones */
.modal-fade-enter-active, .modal-fade-leave-active { transition: opacity 0.3s; }
.modal-fade-enter, .modal-fade-leave-to { opacity: 0; }

@media (max-width: 768px) {
  .modal-body { flex-direction: column; }
  .gallery-side { flex-direction: column-reverse; }
  .thumbnails { flex-direction: row; }
}
</style>