<template>
  <section class="brands-section">
    <div class="brands-container">
      <h3 class="brands-title">Tiendas Oficiales Destacadas</h3>
      <div class="brands-row">
        <div v-for="brand in marcas" :key="brand.nombre" class="brand-logo-box" @click="filtrarMarca(brand.nombre)">
          <span class="brand-stub">{{ brand.emoji }} {{ brand.nombre }}</span>
        </div>
      </div>
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
}

.brands-container {
  background: white;
  border-radius: 8px;
  padding: 20px;
  border: 1px solid #e5e7eb;
}

.brands-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #222;
  margin-bottom: 20px;
  text-align: left;
}

.brands-row {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
}

.brand-logo-box {
  background: white;
  border: 1px solid #e5e7eb;
  padding: 15px 30px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
  color: #4b5563;
  transition: background 0.2s, border-color 0.2s;
}

.brand-logo-box:hover {
  background: #f0f7ff;
  border-color: #007bff;
  color: #007bff;
}
</style>