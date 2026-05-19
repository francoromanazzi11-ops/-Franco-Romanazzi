<template>
  <div class="carousel-container">
    <div class="carousel-track" :style="{ transform: `translateX(-${slideActual * 100}%)` }">
      <div v-for="(banner, index) in banners" :key="index" class="carousel-slide" :style="{ backgroundColor: banner.bgColor }">
        <div class="slide-content">
          <span class="slide-tag">{{ banner.tag }}</span>
          <h2 class="slide-title">{{ banner.titulo }}</h2>
          <p class="slide-desc">{{ banner.descripcion }}</p>
          <button class="slide-btn" @click="clickBanner(banner.titulo)">{{ banner.btnTexto }}</button>
        </div>
        <div class="slide-visual">
          <img :src="banner.imgUrl" :alt="banner.titulo" class="visual-mockup-img" />
        </div>
      </div>
    </div>

    <button class="control-btn prev" @click="moverSlide(-1)">❮</button>
    <button class="control-btn next" @click="moverSlide(1)">❯</button>

    <div class="carousel-dots">
      <span 
        v-for="(banner, index) in banners" 
        :key="index" 
        class="dot" 
        :class="{ 'activo': index === slideActual }"
        @click="slideActual = index"
      ></span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Publicidad',
  data() {
    return {
      slideActual: 0,
      banners: [
        {
          titulo: 'Semana de la Computación',
          descripcion: 'Hasta 40% OFF en Laptops Pro, setups gamer y accesorios con envío prioritario.',
          tag: 'OFERTA IMPERDIBLE',
          btnTexto: 'Ver productos',
          bgColor: '#0f172a',
          imgUrl: 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?q=80&w=500&auto=format&fit=crop'
        },
        {
          titulo: 'Lanzamiento Especial Smartphones',
          descripcion: 'Financiación exclusiva en hasta 12 cuotas fijas sin interés y beneficios Tech Store.',
          tag: 'NUEVO INGRESO',
          btnTexto: 'Comprar ahora',
          bgColor: '#1e3a8a',
          imgUrl: 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=500&auto=format&fit=crop'
        },
        {
          titulo: 'Equipá tu Zona de Juegos',
          descripcion: 'Monitores 4K, teclados mecánicos RGB y mouses inalámbricos con descuentos del 25%.',
          tag: 'SETUP GAMER',
          btnTexto: 'Explorar periféricos',
          bgColor: '#4c1d95',
          imgUrl: 'https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=500&auto=format&fit=crop'
        }
      ]
    };
  },
  methods: {
    moverSlide(direccion) {
      this.slideActual += direccion;
      if (this.slideActual < 0) {
        this.slideActual = this.banners.length - 1;
      } else if (this.slideActual >= this.banners.length) {
        this.slideActual = 0;
      }
    },
    clickBanner(titulo) {
      alert(`Redireccionando a la campaña especial: "${titulo}".`);
    }
  },
  mounted() {
    this.intervalo = setInterval(() => {
      this.moverSlide(1);
    }, 6000);
  },
  unmounted() {
    clearInterval(this.intervalo);
  }
}
</script>

<style scoped>
.carousel-container {
  width: 100%;
  height: 340px;
  position: relative;
  overflow: hidden;
  background: #ddd;
}

.carousel-track {
  display: flex;
  width: 100%;
  height: 100%;
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.carousel-slide {
  min-width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 10%;
  box-sizing: border-box;
  color: white;
}

.slide-content {
  max-width: 50%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
}

.slide-tag {
  background: #007bff;
  font-size: 0.75rem;
  font-weight: bold;
  padding: 4px 10px;
  border-radius: 4px;
  letter-spacing: 0.5px;
}

.slide-title {
  font-size: 2.2rem;
  margin: 0;
  font-weight: 800;
  line-height: 1.2;
}

.slide-desc {
  font-size: 1.05rem;
  margin: 0;
  opacity: 0.9;
  line-height: 1.4;
}

.slide-btn {
  background: white;
  color: #111827;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  font-weight: bold;
  cursor: pointer;
  margin-top: 8px;
  transition: background 0.2s, transform 0.2s;
}

.slide-btn:hover {
  background: #f3f4f6;
  transform: translateY(-1px);
}

.slide-visual {
  width: 40%;
  height: 80%;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  border-radius: 12px;
  box-shadow: 0 20px 25px -5px rgba(0,0,0,0.3);
}

.visual-mockup-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  animation: float 4s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

.control-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0,0,0,0.2);
  color: white;
  border: none;
  font-size: 1.5rem;
  width: 45px;
  height: 45px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
}

.control-btn:hover { background: rgba(0,0,0,0.5); }
.control-btn.prev { left: 20px; }
.control-btn.next { right: 20px; }

.carousel-dots {
  position: absolute;
  bottom: 15px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
  z-index: 10;
}

.dot { width: 9px; height: 9px; background: rgba(211, 211, 211, 0.5); border-radius: 50%; cursor: pointer; }
.dot.activo { background: white; width: 20px; border-radius: 10px; }

@media (max-width: 768px) {
  .slide-content { max-width: 100%; }
  .slide-visual { display: none; }
  .slide-title { font-size: 1.6rem; }
}
</style>