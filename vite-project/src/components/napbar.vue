<template>
  <header class="main-header">
    <div class="header-top">
      <div class="logo-container" @click="$emit('cambiar-pagina', 'inicio')">
        <span class="logo-icon">⚡</span>
        <div class="logo-text-group">
          <span class="logo-text">TECH<span class="logo-highlight">STORE</span></span>
          <span class="logo-sub">E-Commerce</span>
        </div>
      </div>

      <form class="search-form" @submit.prevent="$emit('buscar', searchQuery)">
        <input 
          type="text" 
          placeholder="Buscar productos, marcas y más..." 
          v-model="searchQuery" 
        />
        <button type="submit" class="search-btn">🔍</button>
      </form>

      <div class="header-banner" @click="accionBoton('Suscripción Tech Plus')">
        <span class="banner-emoji">👑</span> Suscríbete a Tech+ por $2.999
      </div>
    </div>

    <div class="header-bottom">
      <div class="envio-container" @click="accionBoton('Código Postal')">
        <span class="geo-icon">📍</span>
        <div class="envio-text">
          <span class="envio-sub">Enviar a</span>
          <span class="envio-main">Capital Federal</span>
        </div>
      </div>

      <nav class="main-nav">
        <ul>
          <li class="dropdown-trigger" @mouseleave="menuCategorias = false">
            <button @mouseenter="menuCategorias = true" @click="menuCategorias = !menuCategorias">
              Categorías ▾
            </button>
            <ul v-if="menuCategorias" class="nav-dropdown">
              <li><button @click="irASeccion('computadoras')">🖥️ Computadoras</button></li>
              <li><button @click="irASeccion('celulares')">📱 Celulares</button></li>
              <li><button @click="irASeccion('audio')">🎧 Audio & Sonido</button></li>
              <li><button @click="irASeccion('ofertas')">🔥 Ofertas Relámpago</button></li>
            </ul>
          </li>
          <li><button @click="$emit('cambiar-pagina', 'inicio')">Inicio</button></li>
          <li><button @click="irASeccion('ofertas')">Ofertas</button></li>
          <li><button @click="accionBoton('Cupones')">Cupones</button></li>
          <li><button @click="$emit('cambiar-pagina', 'ayuda')">Ayuda</button></li>
        </ul>
      </nav>

      <div class="user-menu-actions">
        <button @click="accionBoton('Crear Cuenta')" class="user-nav-btn">Creá tu cuenta</button>
        <button @click="accionBoton('Iniciar Sesión')" class="user-nav-btn">Ingresá</button>
        <button @click="accionBoton('Favoritos')" class="user-nav-btn">Favoritos ❤️</button>
        <button @click="accionBoton('Carrito')" class="cart-nav-btn">
          🛒 <span class="cart-badge">0</span>
        </button>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      searchQuery: '',
      menuCategorias: false
    };
  },
  methods: {
    irASeccion(cat) {
      this.$emit('cambiar-pagina', cat);
      this.menuCategorias = false;
    },
    accionBoton(nombre) {
      alert(`Función de "${nombre}" conectada. ¡Pronto estará lista la base de datos!`);
    }
  }
}
</script>

<style scoped>
.main-header {
  width: 100%;
  background: white;
  border-bottom: 1px solid #e5e7eb;
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  flex-direction: column;
}

.header-top {
  display: flex;
  align-items: center;
  justify-content: space-between; 
  padding: 12px 40px 6px 40px;
  gap: 30px;
}

.logo-container { display: flex; align-items: center; gap: 10px; cursor: pointer; }
.logo-icon { font-size: 2rem; }
.logo-text-group { display: flex; flex-direction: column; }
.logo-text { font-family: sans-serif; font-weight: 800; font-size: 1.4rem; color: #1f2937; }
.logo-highlight { color: #007bff; }
.logo-sub { font-size: 0.75rem; color: #6b7280; font-weight: 600; text-transform: uppercase; }

.search-form { flex-grow: 1; display: flex; max-width: 600px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); border-radius: 6px; }
.search-form input { width: 100%; padding: 11px 15px; border: 1px solid #d1d5db; border-radius: 6px 0 0 6px; outline: none; }
.search-btn { padding: 0 22px; background: #f3f4f6; border: 1px solid #d1d5db; border-left: none; border-radius: 0 6px 6px 0; cursor: pointer; color: #4b5563; }

.header-banner { font-size: 0.85rem; font-weight: 600; color: #374151; background: #f0f7ff; padding: 8px 14px; border-radius: 20px; cursor: pointer; border: 1px solid #bfdbfe; }

.header-bottom { display: flex; align-items: center; justify-content: space-between; padding: 4px 40px 10px 40px; }
.envio-container { display: flex; align-items: center; gap: 6px; cursor: pointer; }
.geo-icon { font-size: 1.2rem; color: #4b5563; }
.envio-text { display: flex; flex-direction: column; }
.envio-sub { font-size: 0.7rem; color: #9ca3af; }
.envio-main { font-size: 0.82rem; color: #4b5563; }

.main-nav ul { display: flex; list-style: none; padding: 0; margin: 0; gap: 6px; position: relative; }
.main-nav button { background: none; border: none; color: #6b7280; font-size: 0.88rem; font-weight: 500; padding: 6px 10px; cursor: pointer; border-radius: 4px; }
.main-nav button:hover { color: #007bff; background: #f0f7ff; }

.dropdown-trigger { position: relative; }
.nav-dropdown { position: absolute; top: 100%; left: 0; background: white; min-width: 190px; border: 1px solid #e5e7eb; border-radius: 6px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); padding: 5px 0; display: flex; flex-direction: column; z-index: 1000; }
.nav-dropdown li { width: 100%; }
.nav-dropdown button { width: 100%; text-align: left; padding: 10px 15px !important; color: #374151 !important; border-radius: 0; }
.nav-dropdown button:hover { background: #f3f4f6 !important; }

.user-menu-actions { display: flex; align-items: center; gap: 8px; }
.user-nav-btn { background: none; border: none; color: #374151; font-size: 0.88rem; cursor: pointer; padding: 6px 10px; }
.cart-nav-btn { background: none; border: none; font-size: 1.2rem; cursor: pointer; position: relative; padding: 4px 8px; }
.cart-badge { position: absolute; top: -2px; right: -2px; background: #007bff; color: white; font-size: 0.68rem; font-weight: bold; border-radius: 50%; width: 16px; height: 16px; display: flex; align-items: center; justify-content: center; }
</style>