<template>
  <section class="promo-banner">
    <div class="promo-content">
      <div class="promo-text">
        <span>OFERTA LIMITADA</span>
        <h2>¡Hasta 40% de Descuento en Tecnología!</h2>
        <p>Aprovecha nuestras cuotas sin interés en productos seleccionados.</p>
        <button class="promo-btn">Ver Promociones</button>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Publicidad'
}
</script>

<style scoped>
.promo-banner {
  background: linear-gradient(135deg, #007bff 0%, #003d7a 100%);
  margin: 20px auto;
  max-width: 1160px;
  border-radius: 12px;
  padding: 40px;
  color: white;
  text-align: left;
}

.promo-text span {
  font-weight: bold;
  font-size: 0.8rem;
  background: rgba(255, 255, 255, 0.2);
  padding: 5px 12px;
  border-radius: 20px;
}

.promo-text h2 {
  font-size: 2rem;
  margin: 15px 0;
}

.promo-text p {
  font-size: 1.1rem;
  margin-bottom: 25px;
  opacity: 0.9;
}

.promo-btn {
  background: white;
  color: #007bff;
  border: none;
  padding: 12px 30px;
  font-weight: bold;
  border-radius: 6px;
  cursor: pointer;
  transition: transform 0.2s;
}

.promo-btn:hover {
  transform: scale(1.05);
}

@media (max-width: 768px) {
  .promo-banner {
    margin: 10px;
    padding: 30px 20px;
    text-align: center;
  }
}
</style>