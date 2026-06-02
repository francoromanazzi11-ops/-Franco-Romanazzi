<template>
  <section class="hub-section">
    <div class="hub-container">
      
      <!-- Encabezado del Hub alineado con el layout global -->
      <div class="hub-header">
        <h2 class="hub-title">Explorá nuestras categorías principales</h2>
        <a href="#" class="hub-link" @click.prevent="seleccionarCat('ofertas')">
          Ver todas las ofertas <span class="arrow">›</span>
        </a>
      </div>

      <!-- Grilla horizontal de categorías optimizada -->
      <div class="categories-grid">
        <div 
          v-for="cat in categorias" 
          :key="cat.id" 
          class="category-card"
          :class="{ active: currentCategory === cat.id }"
          @click="seleccionarCat(cat.id)"
        >
          <div class="image-circle">
            <img :src="cat.img" :alt="cat.title" />
          </div>
          <div class="card-content">
            <h3 class="category-name">{{ cat.title }}</h3>
            <p class="products-count">{{ cat.count }} productos activos</p>
            <span class="catalog-action">Ir al catálogo →</span>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>

<script>
export default {
  name: 'HubCategorias',
  props: {
    currentCategory: {
      type: String,
      default: 'inicio'
    }
  },
  data() {
    return {
      categorias: [
        { id: 'computadoras', title: 'Computadoras', count: 124, img: 'https://images.unsplash.com/photo-1593642632823-8f785ba67e45?q=80&w=150' },
        { id: 'celulares', title: 'Celulares & Smartphones', count: 89, img: 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=150' },
        { id: 'audio', title: 'Audio & Sonido Pro', count: 45, img: 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=150' },
        { id: 'gaming', title: 'Consolas & Gaming', count: 62, img: 'https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?q=80&w=150' }
      ]
    }
  },
  methods: {
    seleccionarCat(catId) {
      this.$emit('change-category', catId);
    }
  }
}
</script>

<style scoped>
/* Contenedor padre de borde a borde */
.hub-section {
  width: 100%;
  padding: 40px 0 20px 0;
  box-sizing: border-box;
}

/* Zona segura de contenido centrada (1200px igual al Header y Banner) */
.hub-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  box-sizing: border-box;
}

/* Fila de título y link de ofertas */
.hub-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 20px;
}

.hub-title {
  font-size: 1.6rem;
  font-weight: 600;
  color: #333333;
  margin: 0;
  text-align: left;
}

.hub-link {
  font-size: 0.95rem;
  color: #3483fa;
  text-decoration: none;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 4px;
}
.hub-link:hover {
  color: #2968c8;
}
.hub-link .arrow {
  font-size: 1.2rem;
  line-height: 0;
  position: relative;
  top: -1px;
}

/* ¡El cambio clave! Grid horizontal de 4 columnas iguales en vez de vertical */
.categories-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 4 columnas que ocupan el mismo espacio */
  gap: 20px;
}

/* Tarjeta estilizada con dimensiones controladas */
.category-card {
  background-color: #ffffff;
  border-radius: 8px;
  padding: 24px 15px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  border: 1px solid #ffffff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.category-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.08);
}

.category-card.active {
  border-color: #3483fa;
  box-shadow: 0 0 0 1px #3483fa;
}

/* Círculo de la foto achicado para mantener la elegancia */
.image-circle {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  background-color: #f7f7f7;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  margin-bottom: 16px;
  border: 1px solid #eaeaea;
}

.image-circle img {
  width: 75%;
  height: 75%;
  object-fit: contain;
}

.card-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
}

.category-name {
  font-size: 1rem;
  font-weight: 600;
  color: #333333;
  margin: 0 0 6px 0;
  line-height: 1.3;
}

.products-count {
  font-size: 0.8rem;
  color: #999999;
  margin: 0 0 16px 0;
}

.catalog-action {
  font-size: 0.85rem;
  color: #3483fa;
  font-weight: 600;
  margin-top: auto; /* Empuja el link al fondo de la tarjeta si los títulos varían en largo */
}
.category-card:hover .catalog-action {
  color: #2968c8;
}

/* Adaptación para pantallas medianas o celulares */
@media (max-width: 992px) {
  .categories-grid {
    grid-template-columns: repeat(2, 1fr); /* 2 filas de 2 columnas en tablets */
  }
  .hub-title {
    font-size: 1.3rem;
  }
}

@media (max-width: 480px) {
  .categories-grid {
    grid-template-columns: 1fr; /* 1 sola columna en celulares chicos */
  }
  .hub-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
}
</style>