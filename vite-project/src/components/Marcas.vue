<template>
  <section class="brands-section">
    <div class="brands-container">
      <h3 class="brands-title">Tiendas Oficiales Destacadas</h3>
      
      <transition-group name="brands-fade" tag="div" class="brands-row" appear>
        <div 
          v-for="brand in marcas" 
          :key="brand.nombre" 
          class="brand-logo-box" 
          @click="filtrarMarca(brand.nombre)"
        >
          <div class="brand-card-content">
            <span class="brand-emoji-wrapper">{{ brand.emoji }}</span>
            <span class="brand-stub">{{ brand.nombre }}</span>
          </div>
          <div class="hover-glow"></div>
        </div>
      </transition-group>
    </div>
  </section>
</template>

<script>
export default {
  name: 'MarcasDestacadas',
  data() {
    return {
      marcas: [
        { nombre: 'Asus Pro', emoji: '⚡' },
        { nombre: 'Samsung Global', emoji: '✨' },
        { nombre: 'Apple Store', emoji: '🍏' },
        { nombre: 'Logitech Tech', emoji: '🕹️' },
        { nombre: 'Intel Core', emoji: '💻' }
      ]
    }
  },
  methods: {
    filtrarMarca(marca) {
      alert(`Filtrando catálogo completo de la tienda oficial: "${marca}".`);
    }
  }
}
</script>

<style scoped>
.brands-section {
  max-width: 1200px;
  margin: 10px auto 30px auto;
  padding: 0 20px;
  box-sizing: border-box;
}

.brands-container {
  background: white;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  border: 1px solid #e5e7eb;
}

.brands-title {
  font-size: 1.15rem;
  color: #333333;
  margin: 0 0 18px 0;
  font-weight: 600;
  text-align: left;
}

.brands-row {
  display: flex;
  gap: 16px;
  justify-content: space-between;
  flex-wrap: wrap;
}

.brand-logo-box {
  flex: 1;
  min-width: 160px;
  background-color: #f7f7f7;
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  padding: 16px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), 
              background-color 0.3s ease, 
              border-color 0.3s ease,
              box-shadow 0.3s ease;
}

.brand-card-content {
  display: flex;
  align-items: center;
  gap: 10px;
  z-index: 2;
  position: relative;
}

.brand-emoji-wrapper {
  font-size: 1.2rem;
  transition: transform 0.3s ease;
}

.brand-stub {
  font-size: 0.9rem;
  color: #4b5563;
  font-weight: 500;
  white-space: nowrap;
}

/* ==========================================================================
   EFECTOS HOVER (ESTILOS VISUALES DINÁMICOS)
   ========================================================================== */

.brand-logo-box:hover {
  transform: translateY(-4px);
  background-color: #ffffff;
  border-color: #3483fa;
  box-shadow: 0 8px 16px rgba(52, 131, 250, 0.08);
}

.brand-logo-box:hover .brand-emoji-wrapper {
  transform: scale(1.2) rotate(6deg);
}

.brand-logo-box:hover .brand-stub {
  color: #3483fa;
}

/* Efecto de pulso reflectivo al hacer click activo */
.brand-logo-box:active {
  transform: translateY(-1px) scale(0.98);
}

/* Glow decorativo de fondo */
.hover-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 120%;
  height: 120%;
  background: radial-gradient(circle, rgba(54, 131, 250, 0.04) 0%, transparent 70%);
  transform: translate(-50%, -50%) scale(0);
  transition: transform 0.4s ease;
  z-index: 1;
}

.brand-logo-box:hover .hover-glow {
  transform: translate(-50%, -50%) scale(1);
}

/* ==========================================================================
   ANIMACIÓN DE ENTRADA (TRANSITION GROUP)
   ========================================================================== */

.brands-fade-enter-active {
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Animación en cascada fluida con desfase sutil */
.brands-fade-enter-from {
  opacity: 0;
  transform: translateY(15px);
}

/* Ajuste responsive básico */
@media (max-width: 640px) {
  .brands-row {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }
  .brand-logo-box {
    min-width: unset;
  }
}
</style>