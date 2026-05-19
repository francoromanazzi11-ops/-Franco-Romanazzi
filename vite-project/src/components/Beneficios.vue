<template>
  <section class="beneficios-section">
    <div class="beneficios-card">
      <div v-for="(item, idx) in items" :key="idx" class="beneficio-item" @click="clickBeneficio(item.titulo)">
        <div class="beneficio-icon">{{ item.icon }}</div>
        <div class="beneficio-info">
          <h4>{{ item.titulo }}</h4>
          <span>{{ item.subtitulo }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Beneficios',
  data() {
    return {
      items: [
        { icon: '💳', titulo: 'Tarjeta de crédito', subtitulo: 'Ver promociones bancarias' },
        { icon: '💵', titulo: 'Efectivo o Débito', subtitulo: 'Pagos al instante en tu moneda' },
        { icon: '🚚', titulo: 'Envíos Rápidos Full', description: 'Garantía de entrega express' },
        { icon: '🛡️', titulo: 'Compra Protegida', subtitulo: '100% de devolución asegurada' }
      ]
    }
  },
  methods: {
    clickBeneficio(titulo) {
      alert(`Abriendo ventana de información detallada sobre: "${titulo}".`);
    }
  }
}
</script>

<style scoped>
.beneficios-section {
  max-width: 1200px;
  margin: -30px auto 20px auto; /* Flota levemente arriba del banner */
  position: relative;
  z-index: 20;
  padding: 0 20px;
}

.beneficios-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.06);
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
  border: 1px solid #e5e7eb;
}

.beneficio-item {
  display: flex;
  align-items: center;
  gap: 15px;
  cursor: pointer;
  padding: 10px;
  border-radius: 6px;
  transition: background 0.2s;
}

.beneficio-item:hover {
  background: #f9fafb;
}

.beneficio-icon {
  font-size: 2rem;
}

.beneficio-info h4 {
  margin: 0;
  font-size: 0.95rem;
  color: #1f2937;
}

.beneficio-info span {
  font-size: 0.78rem;
  color: #2563eb;
  font-weight: 500;
}
</style>