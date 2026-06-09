<template>
  <nav class="sub-header-nav">
    <div class="nav-container">
      
      <div class="left-nav-meta">
        <div class="geo-picker">
          <span class="pin-icon">📍</span>
          <div class="geo-text">
            <span>Enviar a</span>
            <span class="main-city">Capital Federal</span>
          </div>
        </div>
      </div>

      <ul class="categories-list">
        <li><a href="#" @click.prevent="$emit('change-category', 'inicio')">Inicio</a></li>
        <li><a href="#" @click.prevent="$emit('change-category', 'computadoras')">Computadoras</a></li>
        <li><a href="#" @click.prevent="$emit('change-category', 'celulares')">Celulares</a></li>
        <li><a href="#" @click.prevent="$emit('change-category', 'audio')">Audio</a></li>
        <li><a href="#" @click.prevent="$emit('change-category', 'componentes')">Componentes</a></li>
        <li><a href="#" @click.prevent="$emit('change-category', 'gaming')">Gaming</a></li>
        <li><a href="#" @click.prevent="$emit('change-category', 'smart-tv')">Smart TV</a></li>
        <li><a href="#" @click.prevent="$emit('change-category', 'ofertas')" class="highlight-offers">Ofertas</a></li>
      </ul>

      <div class="right-user-meta">
        <a href="#" class="user-link">Creá tu cuenta</a>
        <a href="#" class="user-link">Ingresá</a>
      </div>

    </div>
  </nav>
</template>

<script>
export default {
  name: 'MenuComponent'
}
</script>

<style scoped>
.sub-header-nav {
  width: 100%;
  background-color: #0c2340;
  padding: 8px 0 12px 0;
  box-sizing: border-box;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
}

.left-nav-meta {
  display: flex;
  align-items: center;
}

.geo-picker {
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
}

.pin-icon {
  font-size: 1.1rem;
}

.geo-text {
  display: flex;
  flex-direction: column;
  text-align: left;
}

.geo-text span:first-child {
  font-size: 0.65rem;
  color: rgba(255, 255, 255, 0.6);
}

.geo-text .main-city {
  font-size: 0.78rem;
  color: #ffffff;
  font-weight: 500;
}

.categories-list {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: 18px;
}

.categories-list a {
  font-size: 0.82rem;
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  transition: color 0.15s;
  font-weight: 400;
}

.categories-list a:hover {
  color: #ffffff;
}

.categories-list .highlight-offers {
  color: #00a650;
  font-weight: 700;
}
.categories-list .highlight-offers:hover {
  color: #00cc62;
}

.right-user-meta {
  display: flex;
  align-items: center;
  gap: 15px;
}

.user-link {
  font-size: 0.82rem;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
}
.user-link:hover {
  color: #ffffff;
}
</style>