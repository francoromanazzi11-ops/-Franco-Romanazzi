<template>
  <section class="hub-container">
    <div class="hub-header">
      <h2 class="hub-title">Explorá nuestras categorías principales</h2>
      <button class="explorar-btn" @click="irAOfertas">
        Ver todas las ofertas <span class="arrow-icon">❯</span>
      </button>
    </div>
    
    <div class="hub-grid">
      <div 
        v-for="(cat, idx) in categorias" 
        :key="idx" 
        class="hub-card" 
        @click="$emit('seleccionar-categoria', cat.id)"
      >
        <div class="hub-image-wrapper">
          <img :src="cat.imgUrl" :alt="cat.nombre" class="hub-category-img" />
        </div>
        <h3>{{ cat.nombre }}</h3>
        <p>{{ cat.items }} productos activos</p>
        <span class="hub-link-text">Ir al catálogo ➔</span>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HubCategorias',
  data() {
    return {
      categorias: [
        { id: 'computadoras', nombre: 'Computadoras', items: '124', imgUrl: 'https://images.unsplash.com/photo-1593642632823-8f785ba67e45?q=80&w=300&auto=format&fit=crop' },
        { id: 'celulares', nombre: 'Celulares & Smartphones', items: '89', imgUrl: 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=300&auto=format&fit=crop' },
        { id: 'audio', nombre: 'Audio & Sonido Pro', items: '45', imgUrl: 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=300&auto=format&fit=crop' },
        { id: 'consolas', nombre: 'Consolas & Gaming', items: '62', imgUrl: 'https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?q=80&w=300&auto=format&fit=crop' },
        { id: 'ofertas', nombre: 'Liquidación & Ofertas', items: '31', imgUrl: 'https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?q=80&w=300&auto=format&fit=crop' }
      ]
    }
  },
  methods: {
    irAOfertas() {
      alert("Redireccionando al panel completo de liquidación.");
      this.$emit('seleccionar-categoria', 'ofertas');
    }
  }
}
</script>

<style scoped>
.hub-container {
  max-width: 1200px;
  margin: 40px auto 10px auto;
  padding: 0 20px;
}

.hub-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
}

.hub-title {
  font-size: 1.4rem;
  font-weight: 600;
  color: #222;
  margin: 0;
}

.explorar-btn {
  background: none;
  border: none;
  color: #007bff;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
}

.explorar-btn:hover { text-decoration: underline; }
.arrow-icon { font-size: 1.1rem; }

.hub-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 20px;
}

.hub-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 25px 20px;
  text-align: center;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.hub-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px -10px rgba(0,0,0,0.15);
  border-color: #007bff;
}

.hub-image-wrapper {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  overflow: hidden;
  margin-bottom: 15px;
  border: 2px solid #f3f4f6;
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
}

.hub-category-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.hub-card:hover .hub-category-img {
  transform: scale(1.1);
}

.hub-card h3 {
  margin: 0;
  font-size: 1.05rem;
  color: #1f2937;
  font-weight: 600;
}

.hub-card p {
  margin: 6px 0 15px 0;
  font-size: 0.8rem;
  color: #9ca3af;
}

.hub-link-text {
  font-size: 0.85rem;
  color: #007bff;
  font-weight: 600;
  margin-top: auto;
}
</style>