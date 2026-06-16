<template>
  <div class="modal-root">
    <transition name="fade">
      <div class="modal-overlay" v-if="isOpen" @click.self="$emit('close')"></div>
    </transition>

    <transition name="zoom">
      <div class="detail-box" v-if="isOpen">
        <button class="close-btn" @click="$emit('close')">✕</button>

        <div class="detail-columns" v-if="product">
          <div class="image-column">
            <div class="main-img-wrapper">
              <img :src="product.img" :alt="product.title" class="product-image" />
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
                <p class="green-text">Envío gratis FULL</p>
                <p class="sub-text">Te llega mañana de forma express</p>
              </div>
            </div>

            <div class="actions-wrapper">
              <button class="action-btn buy-now-btn">Comprar ahora</button>
              <button class="action-btn add-to-cart-btn" @click="$emit('add-to-cart', product)">
                Agregar al carrito
              </button>
            </div>
          </div>
        </div>
      </div>
    </transition>
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
  }
}
</script>

<style scoped>
.modal-root {
  position: relative;
  z-index: 6000;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(3px);
}

.detail-box {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #ffffff;
  width: 90%;
  max-width: 860px;
  max-height: 90vh;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.2);
  padding: 30px;
  box-sizing: border-box;
  overflow-y: auto;
}

.close-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  background: none;
  border: none;
  font-size: 1.3rem;
  color: #666666;
  cursor: pointer;
  transition: transform 0.2s ease, color 0.2s ease;
  z-index: 10;
}
.close-btn:hover {
  transform: rotate(90deg);
  color: #333333;
}

.detail-columns {
  display: flex;
  gap: 40px;
  margin-top: 10px;
}

/* Columna de Imagen */
.image-column {
  flex: 1.2;
  display: flex;
  align-items: center;
  justify-content: center;
}

.main-img-wrapper {
  width: 100%;
  height: 380px;
  border: 1px solid #ededed;
  border-radius: 8px;
  padding: 20px;
  box-sizing: border-box;
  background: white;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.product-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.main-img-wrapper:hover .product-image {
  transform: scale(1.05);
}

/* Columna de Información */
.info-column {
  flex: 1;
  text-align: left;
  display: flex;
  flex-direction: column;
}

.product-condition {
  font-size: 0.78rem;
  color: #666666;
  margin: 0 0 8px 0;
}

.product-title {
  font-size: 1.4rem;
  color: #333333;
  margin: 0 0 8px 0;
  font-weight: 600;
  line-height: 1.3;
}

.product-vendor {
  font-size: 0.85rem;
  color: #666666;
  margin: 0 0 20px 0;
}

.vendor-highlight {
  color: #3483fa;
  font-weight: 500;
}

/* Sección de Precios */
.price-section {
  border-top: 1px solid #eee;
  padding-top: 15px;
  margin-bottom: 20px;
}

.price-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.current-price {
  font-size: 2.2rem;
  color: #333333;
  font-weight: 300;
}

.discount-badge {
  font-size: 0.95rem;
  color: #00a650;
  font-weight: 600;
}

.payment-info {
  font-size: 0.82rem;
  color: #666666;
  margin: 6px 0 0 0;
}

/* Beneficios */
.shipping-benefit-box {
  background-color: #f6f6f6;
  border-radius: 8px;
  padding: 14px 16px;
  display: flex;
  gap: 12px;
  align-items: flex-start;
  margin-bottom: 30px;
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
  color: #666666;
  margin-top: 2px;
}

/* Contenedor de Botones Rediseñados */
.actions-wrapper {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: auto; /* Empuja los botones al fondo de la columna */
}

.action-btn {
  width: 100%;
  padding: 14px;
  font-size: 0.95rem;
  font-weight: 600;
  border-radius: 6px;
  cursor: pointer;
  border: none;
  transition: background-color 0.2s ease, transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  box-sizing: border-box;
}

.action-btn:hover {
  transform: translateY(-2px);
}

.action-btn:active {
  transform: translateY(0);
}

/* Botón Comprar Ahora (Azul Sólido Estilo ML) */
.buy-now-btn {
  background-color: #3483fa;
  color: #ffffff;
}

.buy-now-btn:hover {
  background-color: #2968c8;
}

/* Botón Agregar al Carrito (Azul Claro / Transparente) */
.add-to-cart-btn {
  background-color: rgba(65, 137, 245, 0.15);
  color: #3483fa;
}

.add-to-cart-btn:hover {
  background-color: rgba(65, 137, 245, 0.25);
}

/* ==========================================================================
   ANIMACIONES DE ENTRADA Y SALIDA
   ========================================================================== */

/* Fondo oscuro (Fade) */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

/* Caja del modal (Zoom In / Out Elástico) */
.zoom-enter-active {
  transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.zoom-leave-active {
  transition: all 0.25s cubic-bezier(0.4, 0, 1, 1);
}
/* Reutilizamos el translate original para que no se desfase de la pantalla */
.zoom-enter-from {
  opacity: 0;
  transform: translate(-50%, -40%) scale(0.85);
}
.zoom-leave-to {
  opacity: 0;
  transform: translate(-50%, -50%) scale(0.9);
}

/* Responsive simple para pantallas chicas */
@media (max-width: 768px) {
  .detail-columns {
    flex-direction: column;
    gap: 20px;
  }
  .main-img-wrapper {
    height: 250px;
  }
}
</style>