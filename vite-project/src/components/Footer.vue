<template>
  <footer class="main-footer">
    <div class="footer-container">
      <div class="footer-info">
        <h3 class="footer-logo">⚡ TechStore</h3>
        <p>Tu rincón tecnológico con los mejores componentes, smartphones y sistemas de audio del país.</p>
      </div>
      <div class="footer-links">
        <h4>Navegación</h4>
        <ul>
          <li><a href="#" @click.prevent="$emit('cambiar-categoria', 'inicio')">Inicio</a></li>
          <li><a href="#" @click.prevent="$emit('cambiar-categoria', 'ofertas')">Ofertas Especiales</a></li>
          <li><a href="#">Términos y Condiciones</a></li>
        </ul>
      </div>
      <div class="footer-copy">
        <p>&copy; 2026 TechStore S.R.L. Todos los derechos reservados.</p>
        <p class="author-tag">Desarrollado con Vue.js</p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style scoped>
.main-footer {
  background: #0f172a;
  color: #94a3b8;
  padding: 40px 20px 20px 20px;
  margin-top: 60px;
  border-top: 4px solid #1e293b;
  font-family: sans-serif;
  font-size: 0.85rem;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  text-align: left;
}

.footer-logo {
  color: white;
  margin: 0 0 10px 0;
  font-size: 1.2rem;
}

.footer-links h4 {
  color: white;
  margin: 0 0 12px 0;
  font-size: 0.95rem;
}

.footer-links ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-links li {
  margin-bottom: 8px;
}

.footer-links a {
  color: #94a3b8;
  text-decoration: none;
  transition: color 0.2s;
}

.footer-links a:hover {
  color: #f59e0b;
}

.footer-copy {
  grid-column: 1 / -1;
  border-top: 1px solid #1e293b;
  padding-top: 20px;
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  font-size: 0.78rem;
}
.footer-copy p { margin: 0; }
.author-tag { color: #64748b; }
</style>