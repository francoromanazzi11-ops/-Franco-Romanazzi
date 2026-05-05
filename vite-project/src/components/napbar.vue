<template>
  <div class="layout-container">
    <!-- HEADER -->
    <header class="main-header">
      <div class="header-top">
  
        <form class="search-form" @submit.prevent="handleSearch">
          <input type="text" placeholder="¿Qué estás buscando?" v-model="searchQuery" />
          <button type="submit" class="search-btn">🔍</button>
        </form>

  
        <div class="user-actions">
          <button class="icon-btn" title="Mi Cuenta">👤</button>
          <button class="icon-btn menu-hamburger" title="Menú">☰</button>
        </div>
      </div>

      <nav class="main-nav">
        <ul>
          <li><button @click="navigate('inicio')">INICIO</button></li>
          <li><button @click="navigate('computadoras')">COMPUTADORAS</button></li>
          <li><button @click="navigate('celulares')">CELULARES</button></li>
          <li><button @click="navigate('ofertas')">OFERTAS</button></li>
          <li><button @click="navigate('ayuda')">AYUDA</button></li>
        </ul>
      </nav>
    </header>


    <main class="content-spacer">
      <p style="text-align: center; padding: 40px; color: #666;">
        Contenido de la página
      </p>
    </main>


  </div>
</template>

<script>
export default {
  name: 'MainLayout',
  data() {
    return {
      searchQuery: ''
    };
  },
  methods: {
    handleSearch() {
      if (this.searchQuery.trim()) {
        console.log("Buscando:", this.searchQuery);
      }
    },
    navigate(route) {
      console.log("Navegando a:", route);
    }
  }
}
</script>

<style scope>

.layout-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  font-family: sans-serif;
}

.content-spacer {
  flex: 1;
}


.main-header {
  width: 100%;
  border-bottom: 1px solid #ccc;
}

.header-top {
  display: flex;
  align-items: center;
  justify-content: flex-start; 
  padding: 15px 25px; 
  gap: 20px;
}

.search-form {
  flex-grow: 1;
  display: flex;
  max-width: 800px; 
}

.search-form input {
  width: 100%;
  padding: 12px 15px; 
  font-size: 1rem;
  border: 1px solid #aaa;
  border-radius: 6px 0 0 6px;
  outline: none;
}

.search-form input:focus {
  border-color: #007bff;
}

.search-btn {
  padding: 0 20px;
  font-size: 1.2rem;
  background: #f0f0f0;
  border: 1px solid #aaa;
  border-left: none;
  border-radius: 0 6px 6px 0;
  cursor: pointer;
  transition: background 0.2s;
}

.search-btn:hover {
  background: #e0e0e0;
}

.user-actions {
  display: flex;
  gap: 15px;
  margin-left: auto; 
}

.icon-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 5px;
  border-radius: 50%;
  transition: background 0.2s;
}

.icon-btn:hover {
  background: #f0f0f0;
}


.main-nav {
  background-color: #f8f8f8;
  border-top: 1px solid #ddd;
}

.main-nav ul {
  display: flex;
  justify-content: center;
  list-style: none;
  margin: 0;
  padding: 12px 0;
}

.main-nav li {
  margin: 0 15px;
}

.main-nav button {
  background: none;
  border: none;
  font-weight: bold;
  text-transform: uppercase;
  cursor: pointer;
  color: #333;
  font-size: 0.9rem;
}

.main-nav button:hover {
  color: #007bff;
}
@media (max-width: 768px) {
  .header-top {
    flex-direction: column;
    gap: 15px;
  }
  .search-form {
    max-width: 100%;
  }
  .user-actions {
    margin-left: 0;
  }
}
</style>