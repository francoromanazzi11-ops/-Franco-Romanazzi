<template>
  <header class="main-header">
    <div class="header-top">
      <div class="logo-container" @click="$emit('cambiar-categoria', 'inicio')">
        <span class="logo-icon">⚡</span>
        <div class="logo-text-group">
          <span class="logo-text">TECH<span class="logo-highlight">STORE</span></span>
          <span class="logo-sub">E-Commerce</span>
        </div>
      </div>

      <div class="search-form">
        <input 
          type="text" 
          placeholder="Buscar productos, marcas y más..." 
          v-model="searchQuery" 
          @input="$emit('actualizar-busqueda', searchQuery)"
        />
        <button class="search-btn">🔍</button>
      </div>

      <div class="header-banner">
        <span class="banner-emoji">👑</span> Suscríbete a Tech+ por $2.999
      </div>
    </div>

    <div class="header-bottom">
      <div class="envio-container">
        <span class="geo-icon">📍</span>
        <div class="envio-text">
          <span class="envio-sub">Enviar a</span>
          <span class="envio-main">Capital Federal</span>
        </div>
      </div>

      <nav class="main-nav">
        <ul>
          <li><a href="#" @click.prevent="$emit('cambiar-categoria', 'inicio')">Inicio</a></li>
          <li><a href="#" @click.prevent="$emit('cambiar-categoria', 'computadoras')">Computadoras</a></li>
          <li><a href="#" @click.prevent="$emit('cambiar-categoria', 'celulares')">Celulares</a></li>
          <li><a href="#" @click.prevent="$emit('cambiar-categoria', 'audio')">Audio</a></li>
          <li><a href="#" @click.prevent="$emit('cambiar-categoria', 'componentes')">Componentes</a></li>
          <li><a href="#" @click.prevent="$emit('cambiar-categoria', 'perifericos')">Gaming</a></li>
          <li><a href="#" @click.prevent="$emit('cambiar-categoria', 'televisores')">Smart TV</a></li>
          <li><a href="#" @click.prevent="$emit('cambiar-categoria', 'ofertas')" class="oferta-link">Ofertas</a></li>
        </ul>
      </nav>

      <div class="user-menu-actions">
        <span class="user-nav-btn">Creá tu cuenta</span>
        <span class="user-nav-btn">Ingresá</span>
        <span class="cart-nav-btn">🛒 <span class="cart-badge">0</span></span>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      searchQuery: ''
    }
  }
}
</script>

<style scoped>
.main-header {
  width: 100%;
  background: #0f172a;
  border-bottom: 3px solid #1e293b;
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  flex-direction: column;
  font-family: sans-serif;
}

.header-top { display: flex; align-items: center; justify-content: space-between; padding: 12px 40px 6px 40px; gap: 30px; }
.logo-container { display: flex; align-items: center; gap: 10px; cursor: pointer; }
.logo-icon { font-size: 1.8rem; }
.logo-text-group { display: flex; flex-direction: column; text-align: left; }
.logo-text { font-weight: 800; font-size: 1.3rem; color: white; }
.logo-highlight { color: #3b82f6; }
.logo-sub { font-size: 0.7rem; color: #94a3b8; font-weight: 600; text-transform: uppercase; }

.search-form { flex-grow: 1; display: flex; max-width: 550px; border-radius: 6px; overflow: hidden; background: white; }
.search-form input { width: 100%; padding: 10px 15px; border: none; outline: none; font-size: 0.9rem; }
.search-btn { padding: 0 18px; background: #f1f5f9; border: none; cursor: pointer; color: #334155; }

.header-banner { font-size: 0.8rem; font-weight: 600; color: #94a3b8; background: #1e293b; padding: 8px 14px; border-radius: 20px; border: 1px solid #334155; }

.header-bottom { display: flex; align-items: center; justify-content: space-between; padding: 6px 40px 10px 40px; background: #0f172a; }
.envio-container { display: flex; align-items: center; gap: 6px; text-align: left; }
.geo-icon { font-size: 1.1rem; color: #94a3b8; }
.envio-text { display: flex; flex-direction: column; }
.envio-sub { font-size: 0.65rem; color: #64748b; }
.envio-main { font-size: 0.8rem; color: #94a3b8; font-weight: 500; }

.main-nav ul { display: flex; list-style: none; padding: 0; margin: 0; gap: 18px; }
.main-nav a { text-decoration: none; color: #94a3b8; font-size: 0.85rem; font-weight: 500; transition: color 0.2s; }
.main-nav a:hover { color: white; }
.main-nav a.oferta-link { color: #22c55e; font-weight: bold; }

.user-menu-actions { display: flex; align-items: center; gap: 15px; font-size: 0.85rem; color: #94a3b8; }
.user-nav-btn { cursor: pointer; }
.user-nav-btn:hover { color: white; }
.cart-nav-btn { position: relative; cursor: pointer; font-size: 1.05rem; }
.cart-badge { position: absolute; top: -6px; right: -8px; background: #3b82f6; color: white; font-size: 0.65rem; font-weight: bold; border-radius: 50%; width: 15px; height: 15px; display: flex; align-items: center; justify-content: center; }
</style>