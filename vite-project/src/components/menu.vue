<template>
  <nav class="nav-menu">
    <div class="menu-inner">
      
      <!-- Bloque Izquierdo: Ubicación y Links rápidos -->
      <div class="menu-left">
        <div class="location-badge">
          <span class="pin-icon">📍</span>
          <div class="location-text">
            <span class="loc-label">Enviar a</span>
            <span class="loc-dest">Capital Federal</span>
          </div>
        </div>

        <ul class="nav-links">
          <li><a href="#" @click.prevent="seleccionarCat('inicio')">Inicio</a></li>
          <li><a href="#" @click.prevent="seleccionarCat('computadoras')">Computadoras</a></li>
          <li><a href="#" @click.prevent="seleccionarCat('celulares')">Celulares</a></li>
          <li><a href="#" @click.prevent="seleccionarCat('audio')">Audio</a></li>
          <li><a href="#" @click.prevent="seleccionarCat('gaming')">Gaming</a></li>
          <li><a href="#" @click.prevent="seleccionarCat('ofertas')" class="highlight-link">Ofertas</a></li>
        </ul>
      </div>

      <!-- Bloque Derecho: Gestión de cuenta y Carrito -->
      <div class="menu-right">
        <ul class="user-links">
          <li><a href="#">Creá tu cuenta</a></li>
          <li><a href="#">Ingresá</a></li>
        </ul>
        <div class="cart-icon-wrapper">
          <span class="cart-icon">🛒</span>
          <span class="cart-badge">0</span>
        </div>
      </div>

    </div>
  </nav>
</template>

<script>
export default {
  name: 'MenuComponent',
  methods: {
    seleccionarCat(catId) {
      this.$emit('change-category', catId);
    }
  }
}
</script>

<style scoped>
.nav-menu {
  width: 100%;
  background-color: #0d223f; /* Azul un toque más claro que el header principal */
  padding: 8px 0;
  box-sizing: border-box;
  border-bottom: 1px solid #0a1b33;
}

.menu-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box;
}

.menu-left {
  display: flex;
  align-items: center;
  gap: 35px;
}

.location-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
}

.pin-icon {
  font-size: 1.1rem;
  color: #ff4757;
}

.location-text {
  display: flex;
  flex-direction: column;
  text-align: left;
  line-height: 1.2;
}

.loc-label {
  font-size: 0.65rem;
  color: #a0aec0;
}

.loc-dest {
  font-size: 0.75rem;
  color: #ffffff;
  font-weight: 600;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 18px;
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-links li a {
  font-size: 0.85rem;
  color: #cbd5e0;
  text-decoration: none;
}
.nav-links li a:hover {
  color: #ffffff;
}

.nav-links li a.highlight-link {
  color: #2ecc71; /* Verde llamativo para Ofertas */
  font-weight: 700;
}

.menu-right {
  display: flex;
  align-items: center;
  gap: 20px;
}

.user-links {
  display: flex;
  gap: 14px;
  list-style: none;
  padding: 0;
  margin: 0;
}

.user-links li a {
  font-size: 0.8rem;
  color: #cbd5e0;
  text-decoration: none;
}
.user-links li a:hover {
  color: #ffffff;
}

.cart-icon-wrapper {
  position: relative;
  cursor: pointer;
}

.cart-icon {
  font-size: 1.1rem;
  color: #ffffff;
}

.cart-badge {
  position: absolute;
  top: -6px;
  right: -8px;
  background-color: #3483fa;
  color: #fff;
  font-size: 0.6rem;
  font-weight: bold;
  padding: 1px 5px;
  border-radius: 10px;
}

@media (max-width: 768px) {
  .nav-links, .menu-right {
    display: none;
  }
}
</style>