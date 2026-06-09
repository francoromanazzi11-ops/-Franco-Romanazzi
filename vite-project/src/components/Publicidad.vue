<template>
  <section class="carousel-section">
    <div class="carousel-container">
      <button class="control-btn prev-btn" @click="prevSlide">‹</button>

      <div class="carousel-slider" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
        
        <div class="carousel-slide slide-dark-blue">
          <div class="slide-content">
            <div class="text-side">
              <span class="badge-tag tag-blue">NUEVO INGRESO</span>
              <h2 class="slide-title">Lanzamiento Especial Smartphones</h2>
              <p class="slide-subtitle">Financiación exclusiva en hasta 12 cuotas fijas sin interés y beneficios Tech Store.</p>
              <button class="slide-btn btn-white">Comprar ahora</button>
            </div>
            <div class="image-side">
              <img src="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=400" alt="Smartphones" class="banner-img" />
            </div>
          </div>
        </div>

        <div class="carousel-slide slide-dark-blue">
          <div class="slide-content">
            <div class="text-side">
              <span class="badge-tag tag-full">LOGÍSTICA FULL</span>
              <h2 class="slide-title">Componentes de PC con Envío Gratis</h2>
              <p class="slide-subtitle">Armá tu setup ideal con las placas y procesadores más rápidos del mercado hoy mismo.</p>
              <button class="slide-btn btn-blue">Comprar ahora</button>
            </div>
            <div class="image-side">
              <img src="https://images.unsplash.com/photo-1593642632823-8f785ba67e45?q=80&w=400" alt="Componentes" class="banner-img" />
            </div>
          </div>
        </div>

      </div>

      <button class="control-btn next-btn" @click="nextSlide">›</button>

      <div class="carousel-indicators">
        <span 
          v-for="(slide, index) in 2" 
          :key="index" 
          class="dot" 
          :class="{ active: currentSlide === index }"
          @click="goToSlide(index)"
        ></span>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'PublicidadComponent',
  data() {
    return {
      currentSlide: 0
    }
  },
  methods: {
    nextSlide() {
      this.currentSlide = this.currentSlide === 1 ? 0 : 1;
    },
    prevSlide() {
      this.currentSlide = this.currentSlide === 0 ? 1 : 0;
    },
    goToSlide(index) {
      this.currentSlide = index;
    }
  }
}
</script>

<style scoped>
/* Espaciado superior sutil para que no choque con el menú secundario */
.carousel-section {
  width: 100%;
  padding-top: 10px;
  box-sizing: border-box;
}

.carousel-container {
  width: 100%;
  height: 340px;
  position: relative;
  overflow: hidden;
}

.carousel-slider {
  display: flex;
  width: 100%;
  height: 100%;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Fondo azul oscuro premium uniforme para ambos banners */
.carousel-slide {
  min-width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #0c2340; /* El color exacto de la previsualización */
}

.slide-content {
  width: 100%;
  max-width: 1200px;
  height: 100%;
  padding: 0 80px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
}

.text-side {
  flex: 1.2;
  text-align: left;
}

/* Títulos y subtítulos limpios en color blanco */
.slide-title {
  font-size: 2.4rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0 0 12px 0;
  line-height: 1.2;
}

.slide-subtitle {
  font-size: 1.05rem;
  color: #dae4f0;
  margin: 0 0 24px 0;
  line-height: 1.4;
  max-width: 500px;
}

/* Badges estilizados */
.badge-tag {
  font-size: 0.7rem;
  font-weight: 700;
  padding: 4px 8px;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 12px;
  letter-spacing: 0.5px;
}
.tag-blue { background: #0084ff; color: #ffffff; }
.tag-full { background: #222222; color: #ffffff; }

/* Botones de acción */
.slide-btn {
  border: none;
  padding: 12px 28px;
  font-size: 0.9rem;
  font-weight: 700;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s, transform 0.1s;
}
.slide-btn:hover {
  transform: translateY(-1px);
}

/* Variante Botón Blanco (Banner 1) */
.btn-white { background-color: #ffffff; color: #0c2340; }
.btn-white:hover { background-color: #f0f4f8; }

/* Variante Botón Azul (Banner 2) */
.btn-blue { background-color: #3483fa; color: #ffffff; }
.btn-blue:hover { background-color: #1f6cd7; }

/* Contenedor de Imagen */
.image-side {
  flex: 0.8;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.banner-img {
  max-height: 260px;
  max-width: 100%;
  object-fit: contain;
  border-radius: 8px;
}

/* Flechas de navegación laterales */
.control-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: #ffffff;
  font-size: 2.2rem;
  width: 40px;
  height: 60px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
  transition: background-color 0.2s;
}
.control-btn:hover { background: rgba(255, 255, 255, 0.25); }

.prev-btn { left: 0; border-radius: 0 6px 6px 0; }
.next-btn { right: 0; border-radius: 6px 0 0 6px; }

/* Puntos indicadores inferiores */
.carousel-indicators {
  position: absolute;
  bottom: 15px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
  z-index: 10;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.4);
  cursor: pointer;
  transition: background-color 0.2s, width 0.2s;
}
.dot.active {
  background: #ffffff;
  width: 18px;
  border-radius: 4px;
}

@media (max-width: 768px) {
  .image-side { display: none; }
  .slide-title { font-size: 1.7rem; }
  .slide-content { padding: 0 40px; }
}
</style>