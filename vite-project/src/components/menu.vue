<template>
  <div>
    <div 
      class="sidebar-overlay" 
      :class="{ 'activo': abierto }" 
      @click="$emit('cerrar')"
    ></div>

    <div class="sidebar-menu" :class="{ 'abierto': abierto }">
      <div class="sidebar-header">
        <h3>Menú de Navegación</h3>
        <button class="close-btn" @click="$emit('cerrar')">✕</button>
      </div>
      
      <ul class="sidebar-links">
        <li><button @click="seleccionarEnlace('inicio')">🏠 Inicio</button></li>
        <li><button @click="seleccionarEnlace('computadoras')">💻 Computadoras</button></li>
        <li><button @click="seleccionarEnlace('celulares')">📱 Celulares</button></li>
        <li><button @click="seleccionarEnlace('ofertas')">🔥 Ofertas</button></li>
        <li><button @click="seleccionarEnlace('ayuda')">❓ Ayuda</button></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuLateral',
  props: {
    abierto: { type: Boolean, default: false }
  },
  methods: {
    seleccionarEnlace(seccion) {
      this.$emit('cambiar-pagina', seccion);
      this.$emit('cerrar');
    }
  }
}
</script>

<style scoped>
.sidebar-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 199;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}

.sidebar-overlay.activo { opacity: 1; pointer-events: auto; }

.sidebar-menu {
  position: fixed;
  top: 0;
  right: -300px;
  width: 300px;
  height: 100vh;
  background-color: white;
  box-shadow: -5px 0 15px rgba(0, 0, 0, 0.1);
  z-index: 200;
  display: flex;
  flex-direction: column;
  transition: right 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.sidebar-menu.abierto { right: 0; }

.sidebar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  border-bottom: 1px solid #eee;
}

.sidebar-header h3 { margin: 0; color: #333; font-size: 1.1rem; }

.close-btn { background: none; border: none; font-size: 1.3rem; cursor: pointer; color: #888; }

.sidebar-links { list-style: none; padding: 0; margin: 0; }

.sidebar-links li { border-bottom: 1px solid #f5f5f5; }

.sidebar-links button {
  width: 100%;
  background: none;
  border: none;
  text-align: left;
  padding: 16px 24px;
  font-size: 1rem;
  color: #444;
  cursor: pointer;
}

.sidebar-links button:hover {
  background-color: #fcfcfc;
  color: #007bff;
}
</style>