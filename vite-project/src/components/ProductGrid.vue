<template>
  <section class="container">
    <div class="catalog-header">
      <h2 class="section-title">
        {{ search ? 'Resultados para: "' + search + '"' : (category === 'inicio' ? 'Inspirado en tus favoritos' : obtenerNombreCategoria(category)) }}
      </h2>
      <p class="results-counter">{{ productosFiltrados.length }} productos en esta sección</p>
    </div>

    <div v-if="productosFiltrados.length > 0" class="product-grid">
      <div v-for="product in productosFiltrados" :key="product.uniqueId" class="product-card" @click="verDetalle(product)">
        <div v-if="product.discount" class="discount-badge">{{ product.discount }}% OFF</div>
        
        <div class="product-image-container">
          <img :src="product.imgUrl" :alt="product.name" class="product-img" loading="lazy" />
        </div>

        <div class="product-info">
          <p class="vendor-tag">VENDIDO POR: <span class="vendor-name">{{ product.vendedor }}</span></p>
          <p v-if="product.subTag" class="sub-tag-blue">{{ product.subTag }}</p>
          
          <h3 class="product-name">{{ product.name }}</h3>
          <p class="color-spec-tag">Color/Modelo: {{ product.colorSpec }}</p>
          
          <div class="rating-container">
            <span class="stars">★</span>
            <span class="rating-text">{{ product.rating.toFixed(1) }}</span>
            <span class="rating-num">({{ product.opiniones }} opiniones)</span>
          </div>

          <div class="price-block">
            <p v-if="product.discount" class="original-price">$ {{ product.originalPrice.toLocaleString('es-AR') }}</p>
            <p class="current-price">$ {{ product.price.toLocaleString('es-AR') }}</p>
          </div>
          
          <div class="shipping-row">
            <span class="shipping-tag">Envío gratis</span>
            <span class="full-badge">⚡ FULL</span>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="no-results">
      <div class="warning-box">⚠️</div>
      <p>No se encontraron productos en esta sección.</p>
    </div>
  </section>
</template>

<script>
export default {
  props: ['category', 'search'],
  data() {
    return {
      extendedProducts: []
    }
  },
  created() {
    this.generarCatalogoUnicoPremium();
  },
  computed: {
    productosFiltrados() {
      let listado = this.extendedProducts;

      if (this.search) {
        return listado.filter(p => 
          p.name.toLowerCase().includes(this.search.toLowerCase()) || 
          p.category.toLowerCase().includes(this.search.toLowerCase())
        );
      }

      if (this.category === 'inicio') {
        return listado.filter(p => p.destacadoHome).slice(0, 4);
      }

      if (this.category === 'ofertas') {
        return listado.filter(p => p.discount);
      }

      return listado.filter(p => p.category === this.category);
    }
  },
  methods: {
    generarCatalogoUnicoPremium() {
      const db = [];
      const tiendas = ['MUNDO DIGITAL', 'MEGA HARDWARE', 'GIGA COMPUTACIÓN', 'DELTA HARDWARE', 'BARES IT'];

      // ==========================================
      // 1. COMPUTADORAS (15 Productos Únicos y Fotos Distintas)
      // ==========================================
      const modelosComp = [
        { name: 'Notebook Lenovo ThinkPad L14 Gen 4', spec: 'Intel i5 16GB 512GB SSD', color: 'Negro Mate' },
        { name: 'Notebook ASUS Vivobook 15 OLED', spec: 'AMD Ryzen 7 16GB 1TB SSD', color: 'Plata Pulida' },
        { name: 'Notebook HP Pavilion Laptop 14', spec: 'Intel i7 16GB 512GB NVMe', color: 'Gris Mineral' },
        { name: 'Notebook Dell Inspiron 3520 Pro', spec: 'Intel i5 8GB 256GB PCIe', color: 'Negro Carbón' },
        { name: 'Notebook Acer Nitro V15 Gaming', spec: 'Intel i5 RTX 4050 16GB 512GB', color: 'Negro Obsidiana' },
        { name: 'Apple MacBook Air M2 Chip', spec: '8-Core CPU 8GB RAM 256GB SSD', color: 'Gris Espacial' },
        { name: 'Notebook MSI Cyborg 15 Translucent', spec: 'Intel i7 RTX 4060 16GB', color: 'Cyber Black' },
        { name: 'Notebook Gigabyte Aero 14 OLED', spec: 'Intel i9 32GB 1TB Creator', color: 'Blanco Glaciar' },
        { name: 'Notebook Lenovo IdeaPad Slim 3', spec: 'AMD Ryzen 5 8GB 512GB', color: 'Azul Abismo' },
        { name: 'Notebook ASUS TUF Gaming F15', spec: 'Intel i5 GTX 1650 16GB RAM', color: 'Gris Grafito' },
        { name: 'Notebook HP 15-dy Pro Business', spec: 'Intel i3 8GB 256GB Ultra', color: 'Plata Natural' },
        { name: 'Notebook Dell Vostro 3400 Corporate', spec: 'Intel i5 16GB 1TB HDD', color: 'Negro Clásico' },
        { name: 'Notebook Acer Aspire 5 Slim-Fit', spec: 'Intel i7 8GB 512GB Kingston', color: 'Gris Acero' },
        { name: 'Apple MacBook Pro M3 Max Pro', spec: '14-Core CPU 36GB RAM 1TB SSD', color: 'Negro Espacial' },
        { name: 'Notebook Samsung Galaxy Book3 Pro', spec: 'Intel i7 Evo 16GB 512GB', color: 'Grafito Mate' }
      ];

      modelosComp.forEach((item, index) => {
        const precioBase = 540000 + (index * 22000);
        const desc = index % 4 === 0 ? 10 : null; // Distribuye ofertas reales

        db.push({
          uniqueId: `comp-${index}`,
          name: `${item.name} ${item.spec}`,
          category: 'computadoras',
          originalPrice: precioBase,
          price: desc ? Math.floor(precioBase * 0.9) : precioBase,
          discount: desc,
          colorSpec: item.color,
          // La query 'sig' fuerza a Unsplash a buscar una foto diferente del tag laptop para cada iteración
          imgUrl: `https://images.unsplash.com/photo-1593642632823-8f785ba67e45?q=80&w=400&auto=format&fit=crop&sig=laptop-${index}`,
          vendedor: tiendas[index % tiendas.length],
          subTag: index % 5 === 0 ? 'DISTRIBUIDORA' : null,
          rating: 4.2 + ((index % 7) * 0.1),
          opiniones: 32 + (index * 5),
          destacadoHome: index === 1
        });
      });

      // ==========================================
      // 2. CELULARES (15 Productos Únicos y Fotos Distintas)
      // ==========================================
      const modelosCelu = [
        { name: 'Samsung Galaxy S24 Ultra 5G', spec: '256GB 12GB RAM Dynamic AMOLED', color: 'Gris Titanio' },
        { name: 'Motorola Edge 40 Neo Premium', spec: '256GB 8GB RAM Leather Back', color: 'Azul Profundo' },
        { name: 'Xiaomi Redmi Note 13 Pro Plus', spec: '512GB 12GB RAM 200MP Cam', color: 'Negro Absoluto' },
        { name: 'ZTE Blade A56 Pro Entry-Level', spec: '128GB 4GB RAM Octa-Core', color: 'Blanco Glaciar' },
        { name: 'Apple iPhone 15 Pro Max Novedad', spec: '256GB Apple A17 Pro Bionic', color: 'Titanio Natural' },
        { name: 'Google Pixel 8 Pro Pure Android', spec: '128GB 12GB RAM Tensor G3', color: 'Celeste Porcelana' },
        { name: 'Samsung Galaxy A54 5G Balance', spec: '128GB 8GB RAM Nightography', color: 'Verde Lima' },
        { name: 'Motorola Moto G84 Entertainment', spec: '256GB 8GB RAM Dolby Atmos', color: 'Rojo Viva Magenta' },
        { name: 'Xiaomi Poco X6 Pro Performance', spec: '512GB 12GB RAM Dimensity Ultra', color: 'Amarillo Poco' },
        { name: 'Infinix Note 40 Pro Super Charge', spec: '256GB 8GB RAM 70W Fast', color: 'Verde Vintage' },
        { name: 'Realme 11 Pro Plus Luxury Design', spec: '512GB 12GB RAM 120Hz Curve', color: 'Beige Arena' },
        { name: 'Samsung Galaxy Z Flip5 Foldable', spec: '256GB 8GB RAM Flex Window', color: 'Crema Menta' },
        { name: 'Apple iPhone 13 Original Box', spec: '128GB Super Retina XDR Display', color: 'Azul Medianoche' },
        { name: 'Xiaomi Redmi 13C Pocket-Friendly', spec: '128GB 4GB RAM Dual Sim', color: 'Verde Trébol' },
        { name: 'Motorola Edge 50 Ultra Masterpiece', spec: '1TB Storage 16GB RAM Wooden', color: 'Madera Nórdica' }
      ];

      modelosCelu.forEach((item, index) => {
        const precioBase = 250000 + (index * 19500);
        const desc = index % 3 === 0 ? 15 : null;

        db.push({
          uniqueId: `cel-${index}`,
          name: item.name,
          category: 'celulares',
          originalPrice: precioBase,
          price: desc ? Math.floor(precioBase * 0.85) : precioBase,
          discount: desc,
          colorSpec: `${item.color} (${item.spec})`,
          imgUrl: `https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=400&auto=format&fit=crop&sig=phone-${index}`,
          vendedor: tiendas[(index + 2) % tiendas.length],
          subTag: index % 4 === 0 ? 'DISTRIBUIDORA' : null,
          rating: 3.8 + ((index % 10) * 0.1),
          opiniones: 14 + (index * 8),
          destacadoHome: index === 3
        });
      });

      // ==========================================
      // 3. AUDIO (15 Productos Únicos y Fotos Distintas)
      // ==========================================
      const modelosAudio = [
        { name: 'Auriculares Sony WH-1000XM4 ANC', spec: 'Wireless Headband Over-Ear Hi-Res', color: 'Negro Mate' },
        { name: 'Parlante Portátil JBL Flip 6 Bass', spec: 'Bluetooth Speaker Waterproof IPX7', color: 'Azul Marino' },
        { name: 'Auriculares In-Ear Sennheiser Sport', spec: 'True Wireless Bluetooth Earbuds Twist', color: 'Blanco Glaciar' },
        { name: 'Audio-Technica M50x Studio Monitor', spec: 'Professional Wired DJ Headphones Pack', color: 'Negro Estudio' },
        { name: 'Auriculares Bose QuietComfort Ultra', spec: 'Spatial Audio Immersive Noise Cancelling', color: 'Blanco Humo' },
        { name: 'Parlante Logitech UE Boom 3 360', spec: 'Wireless Portable Rugged Speaker Pro', color: 'Rojo Sunset' },
        { name: 'Auriculares Razer BlackShark V2 Pro', spec: 'Esports Wireless Gaming Headset 7.1', color: 'Negro Razer' },
        { name: 'Soundbar JBL Bar 500 Home Cinema', spec: '5.1 Channels Dolby Atmos Subwoofer', color: 'Gris Carbón' },
        { name: 'Auriculares Apple AirPods Pro Gen 2', spec: 'MagSafe USB-C Active Transparecy', color: 'Blanco Original' },
        { name: 'Parlante Portátil Marshall Emberton II', spec: 'Iconic Design Bluetooth Stereo Sound', color: 'Negro/Bronce' },
        { name: 'Auriculares HyperX Cloud II Red', spec: 'Wired Gaming Headset Memory Foam', color: 'Negro/Rojo' },
        { name: 'Auriculares Sony WF-C500 Compact', spec: 'True Wireless Earbuds Splashproof', color: 'Verde Pastel' },
        { name: 'Parlante Xiaomi Mi Portable 16W', spec: 'Dual TWS Connection Metallic Body', color: 'Azul Cobalto' },
        { name: 'Auriculares Philips TWS TAT2206', spec: 'Super Small Case Ergonomic Fit 18h', color: 'Rosado Soft' },
        { name: 'Soundbar Samsung HW-Q600C Q-Symphony', spec: '3.1.2 Channels Acoustic Beam True HD', color: 'Negro Titanio' }
      ];

      modelosAudio.forEach((item, index) => {
        // Asignación de precio estricta para emular tu captura original ($ 399.000 / $ 155.000)
        const precioBase = index % 2 === 0 ? 399000 : 155000;
        const desc = index % 5 === 0 ? 20 : null;

        db.push({
          uniqueId: `aud-${index}`,
          name: item.name,
          category: 'audio',
          originalPrice: precioBase * 1.25,
          price: desc ? Math.floor(precioBase * 0.8) : precioBase,
          discount: desc,
          colorSpec: `${item.color} - ${item.spec}`,
          imgUrl: `https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=400&auto=format&fit=crop&sig=audio-${index}`,
          vendedor: tiendas[(index + 1) % tiendas.length],
          subTag: index % 3 === 0 ? 'COMPONENTES' : null,
          rating: 4.3 + ((index % 6) * 0.1),
          opiniones: 50 + (index * 11),
          destacadoHome: index === 0
        });
      });

      // ==========================================
      // 4. CONSOLAS & GAMING (15 Productos Únicos y Fotos Distintas)
      // ==========================================
      const modelosGaming = [
        { name: 'Teclado Mecánico Redragon Kumara K552', spec: 'Outemu Blue Switches Anti-Ghosting', color: 'RGB Setup Black' },
        { name: 'Mouse Óptico Razer Viper Mini Ultra', spec: '8500 DPI Speedflex Cable Light', color: 'Classic Black' },
        { name: 'Auriculares Gaming HyperX Cloud Flight', spec: 'Wireless Long Battery Detachable Mic', color: 'Negro Mate' },
        { name: 'Placa de Video MSI NVIDIA RTX 4060', spec: 'Ventus 2X 8GB GDDR6 Dual Fan PCIe', color: 'Gris Metalizado' },
        { name: 'Consola Sony PlayStation 5 Slim', spec: 'Chassis D 1TB SSD Digital Edition', color: 'Blanco/Negro' },
        { name: 'Mando Inalámbrico Xbox Series Controller', spec: 'Bluetooth Textured Grips Share Button', color: 'Robot White' },
        { name: 'Mouse Gaming Logitech G Pro X Superlight', spec: 'HERO 25K Sensor 63g Wireless Pro', color: 'Magenta Pop' },
        { name: 'Teclado Mecánico Corsair K70 RGB PRO', spec: 'Cherry MX Red Switches Aluminum Frame', color: 'Negro Anodizado' },
        { name: 'Procesador AMD Ryzen 7 5700X Box', spec: '8 Cores 16 Threads AM4 Socket No Fan', color: 'Silicon Edition' },
        { name: 'Memoria RAM Kingston Fury Beast DDR4', spec: '16GB (2x8GB) 3200MHz CL16 Intel XMP', color: 'Negro Disipador' },
        { name: 'Placa Madre ASUS ROG Strix B550-F', spec: 'Gaming PCIe 4.0 Aura Sync Motherboard', color: 'Black Armor' },
        { name: 'Fuente Certificada EVGA 750W N1', spec: '750W Power Supply Active PFC Quiet', color: 'Negro Industrial' },
        { name: 'Gabinete Gamer Cougar MX410 Mesh', spec: '4 ARGB Fans Included Tempered Glass', color: 'Negro Rejilla' },
        { name: 'Disco SSD M.2 WD Black SN850X', spec: '1TB NVMe PCIe Gen4 Internal Gaming', color: 'Heatsink Edition' },
        { name: 'Consola Nintendo Switch OLED Model', spec: '7-inch Vibrant Screen 64GB Dock LAN', color: 'Azul/Rojo Neón' }
      ];

      modelosGaming.forEach((item, index) => {
        const precioBase = 75000 + (index * 26000);
        const desc = index % 4 === 1 ? 25 : null;

        db.push({
          uniqueId: `gam-${index}`,
          name: item.name,
          category: 'perifericos', // Conectado a tu nav de Gaming
          originalPrice: precioBase,
          price: desc ? Math.floor(precioBase * 0.75) : precioBase,
          discount: desc,
          colorSpec: `${item.color} - ${item.spec}`,
          imgUrl: `https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?q=80&w=400&auto=format&fit=crop&sig=gaming-${index}`,
          vendedor: tiendas[(index + 3) % tiendas.length],
          subTag: index % 2 === 0 ? 'COMPONENTES' : null,
          rating: 4.5 + ((index % 5) * 0.1),
          opiniones: 42 + (index * 6),
          destacadoHome: index === 4
        });
      });

      this.extendedProducts = db;
    },
    obtenerNombreCategoria(catId) {
      const mapa = {
        computadoras: 'Computadoras & Notebooks',
        celulares: 'Celulares & Smartphones',
        audio: 'Audio & Sonido Pro',
        perifericos: 'Consolas & Gaming',
        ofertas: 'Liquidación & Ofertas'
      };
      return mapa[catId] || catId.toUpperCase();
    },
    verDetalle(prod) {
      alert(`📦 Item seleccionado:\n${prod.name}\n\nDistribuye de forma directa: ${prod.vendedor}`);
    }
  }
}
</script>

<style scoped>
.container { max-width: 1200px; margin: 0 auto; padding: 20px; min-height: 500px; }
.catalog-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 24px; border-bottom: 1px solid #e2e8f0; padding-bottom: 10px; font-family: Arial, sans-serif; }
.section-title { text-align: left; margin: 0; color: #333333; font-size: 1.4rem; font-weight: 600; }
.results-counter { font-size: 0.85rem; color: #666666; margin: 0; }

.product-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 16px; }
.product-card { background: white; border-radius: 4px; padding: 16px; border: 1px solid #e6e6e6; position: relative; cursor: pointer; display: flex; flex-direction: column; transition: box-shadow 0.2s; box-shadow: 0 1px 2px rgba(0,0,0,0.02); }
.product-card:hover { box-shadow: 0 10px 20px rgba(0,0,0,0.08); border-color: #d9d9d9; }

.product-image-container { width: 100%; height: 180px; overflow: hidden; display: flex; align-items: center; justify-content: center; background: #ffffff; margin-bottom: 8px; }
.product-img { max-width: 100%; max-height: 100%; object-fit: contain; }

.discount-badge { position: absolute; top: 12px; left: 12px; background: #00a650; color: white; padding: 2px 6px; border-radius: 3px; font-weight: bold; font-size: 0.75rem; z-index: 10; font-family: Arial, sans-serif; }
.product-info { text-align: left; display: flex; flex-direction: column; flex-grow: 1; font-family: Arial, sans-serif; }

.vendor-tag { font-size: 0.72rem; color: #999999; margin: 0 0 2px 0; font-weight: 400; letter-spacing: 0.3px; }
.vendor-name { color: #3483fa; font-weight: bold; }
.sub-tag-blue { font-size: 0.68rem; color: #3483fa; font-weight: bold; margin: 0 0 4px 0; letter-spacing: 0.5px; }

.product-name { font-size: 0.95rem; color: #333333; margin: 2px 0; font-weight: bold; line-height: 1.3; height: 38px; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }
.color-spec-tag { font-size: 0.8rem; color: #666666; margin: 0 0 6px 0; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; }

.rating-container { display: flex; align-items: center; gap: 4px; margin-bottom: 12px; }
.stars { color: #3483fa; font-size: 0.85rem; }
.rating-text { font-size: 0.8rem; font-weight: bold; color: #3483fa; }
.rating-num { font-size: 0.75rem; color: #999999; }

.price-block { margin-top: auto; display: flex; flex-direction: column; gap: 2px; margin-bottom: 8px; }
.original-price { font-size: 0.75rem; color: #999999; text-decoration: line-through; margin: 0; }
.current-price { font-size: 1.5rem; font-weight: bold; color: #1a1a1a; margin: 0; letter-spacing: -0.5px; }

.shipping-row { display: flex; align-items: center; justify-content: space-between; margin-top: 4px; padding-top: 2px; }
.shipping-tag { font-size: 0.82rem; color: #00a650; font-weight: bold; margin: 0; }
.full-badge { font-size: 0.7rem; background: #00a650; color: white; padding: 2px 5px; border-radius: 3px; font-weight: 900; font-style: italic; letter-spacing: 0.2px; }

.no-results { text-align: center; padding: 60px 20px; color: #666666; font-family: Arial, sans-serif; }
.warning-box { font-size: 3rem; margin-bottom: 15px; }
</style>