<template>
  <header class="main-header">
    <div class="header-top">
      <form class="search-form" @submit.prevent="$emit('buscar', searchQuery)">
        <input 
          type="text" 
          placeholder="¿Qué estás buscando?" 
          v-model="searchQuery" 
        />
        <button type="submit" class="search-btn">🔍</button>
      </form>

      <div class="user-actions">
        <button class="icon-btn">👤</button>
        <button class="icon-btn">☰</button>
      </div>
    </div>

    <nav class="main-nav">
      <ul>
        <li><button @click="$emit('cambiar-pagina', 'inicio')">INICIO</button></li>
        <li><button @click="$emit('cambiar-pagina', 'computadoras')">COMPUTADORAS</button></li>
        <li><button @click="$emit('cambiar-pagina', 'celulares')">CELULARES</button></li>
        <li><button @click="$emit('cambiar-pagina', 'ofertas')">OFERTAS</button></li>
        <li><button @click="$emit('cambiar-pagina', 'ayuda')">AYUDA</button></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  data() {
    return { searchQuery: '' }
  }
}
</script>

<style scoped>
.main-header {
  background: white;
  border-bottom: 1px solid #ddd;
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-top {
  display: flex;
  align-items: center;
  padding: 10px 20px;
  gap: 20px;
}

.search-form {
  flex: 1;
  display: flex;
  max-width: 700px;
}

.search-form input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px 0 0 4px;
  outline: none;
}

.search-btn {
  padding: 0 15px;
  background: #eee;
  border: 1px solid #ccc;
  border-left: none;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
}

.user-actions {
  display: flex;
  gap: 10px;
}

.icon-btn {
  background: none;
  border: none;
  font-size: 1.4rem;
  cursor: pointer;
}

.main-nav {
  background: #fff;
  border-top: 1px solid #eee;
}

.main-nav ul {
  display: flex;
  justify-content: center;
  list-style: none;
  margin: 0;
  padding: 10px;
}

.main-nav button {
  background: none;
  border: none;
  font-weight: 600;
  padding: 5px 15px;
  cursor: pointer;
  color: #555;
}

.main-nav button:hover {
  color: #007bff;
}
</style>