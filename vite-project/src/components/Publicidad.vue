<template>
  <div class="carousel-container">
    <!-- Slider Wrapper fluido -->
    <div class="carousel-slider" :style="{ transform: `translateX(-${activeIndex * 100}%)` }">
      <div 
        v-for="(banner, index) in banners" 
        :key="index" 
        class="carousel-slide"
        :style="{ backgroundColor: banner.bgColor }"
      >
        <!-- Caja central fija -->
        <div class="slide-content">
          <div class="text-side">
            <span class="badge-tag">{{ banner.badge }}</span>
            <h2 class="slide-title">{{ banner.title }}</h2>
            <p class="slide-subtitle">{{ banner.subtitle }}</p>
            <button class="slide-btn">Comprar ahora</button>
          </div>
          <div class="image-side">
            <img :src="banner.imgUrl" :alt="banner.title" class="banner-img" />
          </div>
        </div>
      </div>
    </div>

    <!-- Controles en los extremos absolutos -->
    <button class="control-btn prev-btn" @click="prevSlide">‹</button>
    <button class="control-btn next-btn" @click="nextSlide">›</button>

    <!-- Indicadores -->
    <div class="carousel-indicators">
      <span 
        v-for="(banner, index) in banners" 
        :key="'dot-' + index" 
        class="dot"
        :class="{ active: index === activeIndex }"
        @click="goToSlide(index)"
      ></span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PublicidadComponent',
  data() {
    return {
      activeIndex: 0,
      timer: null,
      banners: [
        {
          badge: 'NUEVO INGRESO',
          title: 'Lanzamiento Especial Smartphones',
          subtitle: 'Financiación exclusiva en hasta 12 cuotas fijas sin interés y beneficios Tech Store.',
          imgUrl: 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=600',
          bgColor: '#164293' // El color azul del banner de tu imagen
        },
        {
          badge: 'LOGÍSTICA FULL',
          title: 'Componentes de PC con Envío Gratis',
          subtitle: 'Armá tu setup ideal con las placas y procesadores más rápidos del mercado hoy mismo.',
          imgUrl: 'https://images.unsplash.com/photo-1593642632823-8f785ba67e45?q=80&w=600',
          bgColor: '#112240'
        }
      ]
    }
  },
  mounted() {
    this.startAutoPlay();
  },
  beforeDestroy() {
    this.stopAutoPlay();
  },
  methods: {
    startAutoPlay() {
      this.timer = setInterval(() => { this.nextSlide(); }, 6000);
    },
    stopAutoPlay() {
      if (this.timer) clearInterval(this.timer);
    },
    nextSlide() {
      this.activeIndex = (this.activeIndex + 1) % this.banners.length;
    },
    prevSlide() {
      this.activeIndex = (this.activeIndex - 1 + this.banners.length) % this.banners.length;
    },
    goToSlide(index) {
      this.activeIndex = index;
      this.stopAutoPlay();
      this.startAutoPlay();
    }
  }
}
</script>

<style scoped>
.carousel-container {
  width: 100%;
  height: 380px;
  position: relative;
  overflow: hidden;
}

.carousel-slider {
  display: flex;
  width: 100%;
  height: 100%;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.carousel-slide {
  min-width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.slide-content {
  width: 100%;
  max-width: 1200px;
  height: 100%;
  padding: 0 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
}

.text-side {
  flex: 1.2;
  text-align: left;
  color: #ffffff;
}

.badge-tag {
  background: #0084ff;
  color: #ffffff;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 5px 10px;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 15px;
}

.slide-title {
  font-size: 2.4rem;
  font-weight: 700;
  margin: 0 0 12px 0;
  line-height: 1.2;
}

.slide-subtitle {
  font-size: 1.05rem;
  color: #e2e8f0;
  margin: 0 0 28px 0;
  line-height: 1.5;
  max-width: 520px;
}

.slide-btn {
  background-color: #ffffff;
  color: #164293;
  border: none;
  padding: 12px 28px;
  font-size: 0.9rem;
  font-weight: 700;
  border-radius: 6px;
  cursor: pointer;
}
.slide-btn:hover {
  background-color: #f7fafc;
  transform: translateY(-1px);
}

.image-side {
  flex: 0.8;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.banner-img {
  max-height: 300px;
  max-width: 100%;
  object-fit: contain;
  border-radius: 12px;
}

.control-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.15);
  border: none;
  color: white;
  font-size: 2.5rem;
  width: 45px;
  height: 65px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
}
.control-btn:hover {
  background: rgba(0, 0, 0, 0.3);
}

.prev-btn { left: 0; border-radius: 0 8px 8px 0; }
.next-btn { right: 0; border-radius: 8px 0 0 8px; }

.carousel-indicators {
  position: absolute;
  bottom: 20px;
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
}

.dot.active {
  background: #ffffff;
  width: 20px;
  border-radius: 4px;
}

@media (max-width: 768px) {
  .image-side { display: none; }
  .slide-title { font-size: 1.8rem; }
}
</style>