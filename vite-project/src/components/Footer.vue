<template>
  <footer class="main-footer" :class="{ 'footer-expandido': expandir }">
    <div class="footer-container">
      <div class="footer-section">
        <h3>NOSOTROS</h3>
        <button @click="$emit('cambiar-pagina', 'nosotros')">Quiénes somos</button>
      </div>
      <div class="footer-section">
        <h3>SOPORTE</h3>
        <div class="footer-row">
          <button @click="$emit('cambiar-pagina', 'ayuda')">Ayuda</button>
          <button @click="$emit('cambiar-pagina', 'soporte')">Técnico</button>
        </div>
      </div>
      <div class="footer-section">
        <h3>CONTACTO</h3>
        <button @click="$emit('cambiar-pagina', 'redes')">Redes Sociales</button>
      </div>
    </div>
    <div class="footer-bottom">© 2026 Franco Romanazzi</div>
  </footer>
</template>

<script>
export default { props: { expandir: Boolean } }
</script>

<style scoped>
.main-footer { background-color: #585757; color: white; padding: 30px 0; transition: all 0.6s ease; }
.footer-expandido { transform: scale(1.05); padding: 50px 0; background-color: #444; box-shadow: 0 -10px 30px rgba(0,0,0,0.5); }
.footer-container { display: flex; justify-content: space-around; max-width: 1000px; margin: 0 auto; }
.footer-section h3 { color: #007bff; font-size: 0.9rem; }
.footer-section button { background: none; border: none; color: #ccc; cursor: pointer; display: block; margin: 5px 0; }
.footer-bottom { text-align: center; margin-top: 20px; border-top: 1px solid #666; padding-top: 10px; font-size: 0.8rem; }
</style>