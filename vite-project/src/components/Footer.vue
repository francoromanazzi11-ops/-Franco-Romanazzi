<script>
export default {name: "Footer"};
</script>

<template>    
    <footer class="main-footer">
      <div class="footer-container">
        <div class="footer-section">
          <h3>NOSOTROS</h3>
          <button @click="navigate('Nosotros')">Quiénes somos</button>
        </div>

        <div class="footer-section">
          <h3>SOPORTE</h3>
          <div class="footer-row">
            <button @click="navigate('ayuda')">Ayuda</button>
            <button @click="navigate('Soporte')">Técnico</button>
            <button @click="navigate('Fallos')">Fallos</button>
          </div>
        </div>

        <div class="footer-section">
          <h3>CONTACTO</h3>
          <div class="footer-row">
            <button @click="navigate('Locaciones')">Tiendas</button>
            <button @click="navigate('Redes Sociales')">Redes</button>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <span>&copy; 2026 Franco Romanazzi</span>
      </div>
    </footer>
</template>

<style scope>
.main-footer {
  background-color: #585757;
  color: #fff;
  padding: 25px 0 15px 0;
}

.footer-container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  max-width: 1000px;
  margin: 0 auto;
  gap: 20px;
}

.footer-section h3 {
  font-size: 0.85rem;
  margin-bottom: 10px;
  color: #007bff;
  letter-spacing: 1px;
}

.footer-section button {
  background: none;
  border: none;
  color: #ccc;
  cursor: pointer;
  font-size: 0.8rem;
  padding: 0;
  margin-right: 12px;
}

.footer-section button:hover {
  text-decoration: underline;
  color: white;
}

.footer-row {
  display: flex;
  gap: 12px;
}

.footer-bottom {
  text-align: center;
  margin-top: 20px;
  padding-top: 15px;
  border-top: 1px solid #333;
  font-size: 0.75rem;
  color: #777;
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