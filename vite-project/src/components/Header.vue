<template>
  <header class="main-header">
    <div class="header-inner">
      <!-- Logo e Identidad -->
      <div class="logo-area" @click="$emit('go-home')">
        <span class="lightning-icon">⚡</span>
        <div class="brand-text">
          <span class="brand-title">TECHSTORE</span>
          <span class="brand-subtitle">E-COMMERCE</span>
        </div>
      </div>

      <!-- Barra de Buscador Global -->
      <div class="search-container">
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Buscar productos, marcas y más..." 
          @keyup.enter="buscar"
        />
        <button class="search-btn" @click="buscar">🔍</button>
      </div>

      <!-- Tag de Suscripción Premium -->
      <div class="premium-tag">
        <span>👑 Suscribite a Tech+ por $2.999</span>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'HeaderComponent',
  data() {
    return {
      searchQuery: ''
    }
  },
  methods: {
    buscar() {
      this.$emit('execute-search', this.searchQuery);
    }
  }
}
</script>

<style scoped>
.main-header {
  width: 100%;
  background-color: #0b1a30; /* El azul oscuro de tu captura */
  padding: 14px 0;
  box-sizing: border-box;
  border-bottom: 1px solid #071120;
}

.header-inner {
  max-width: 1200px; /* Ancho máximo de la zona segura de contenido */
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 30px;
  box-sizing: border-box;
}

.logo-area {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
}

.lightning-icon {
  font-size: 1.8rem;
  color: #ff9f43;
}

.brand-text {
  display: flex;
  flex-direction: column;
  text-align: left;
}

.brand-title {
  font-size: 1.3rem;
  font-weight: 800;
  color: #ffffff;
  letter-spacing: 1px;
}

.brand-subtitle {
  font-size: 0.65rem;
  font-weight: 600;
  color: #3483fa;
  letter-spacing: 2px;
}

.search-container {
  flex: 1;
  max-width: 550px;
  display: flex;
  background-color: #ffffff;
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 1px 2px rgba(0,0,0,0.2);
}

.search-container input {
  flex: 1;
  border: none;
  padding: 10px 15px;
  font-size: 0.9rem;
  outline: none;
  color: #333;
}

.search-btn {
  background: none;
  border: none;
  padding: 0 15px;
  cursor: pointer;
  background-color: #f5f5f5;
  border-left: 1px solid #e6e6e6;
  font-size: 0.9rem;
}
.search-btn:hover {
  background-color: #e8e8e8;
}

.premium-tag {
  background-color: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 8px 16px;
  border-radius: 20px;
  color: #ffffff;
  font-size: 0.8rem;
  font-weight: 500;
  cursor: pointer;
}
.premium-tag:hover {
  background-color: rgba(255, 255, 255, 0.15);
}

@media (max-width: 768px) {
  .header-inner {
    flex-direction: column;
    gap: 15px;
  }
  .premium-tag {
    display: none;
  }
  .search-container {
    width: 100%;
  }
}
</style>