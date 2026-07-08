# Jayson Tech

Sitio web de presentación de **Jayson Tech** — desarrollo web, automatización y capacitación tecnológica.

**Sitio en producción:** [https://jaysontech.com.co](https://jaysontech.com.co)

## Estructura del proyecto

```
├── index.html          # Página principal
├── style.css           # Estilos
├── script.js           # Interactividad (menú móvil, año dinámico)
├── projects.js         # Lista de proyectos (solo imagen + descripción)
├── 404.html            # Página de error personalizada
├── CNAME               # Dominio personalizado (GitHub Pages)
├── robots.txt          # Directivas para buscadores
├── sitemap.xml         # Mapa del sitio
└── images/
    └── projects/       # Imágenes de presentación de proyectos
```

## Despliegue en GitHub Pages

1. Sube el repositorio a GitHub.
2. Ve a **Settings → Pages**.
3. En **Source**, selecciona la rama `main` y la carpeta `/ (root)`.
4. El archivo `CNAME` configura automáticamente el dominio `jaysontech.com.co`.
5. Configura en tu proveedor DNS un registro **CNAME** apuntando a `<usuario>.github.io`.

## Desarrollo local

No se requiere build ni dependencias. Abre `index.html` en el navegador o usa un servidor local:

```bash
python3 -m http.server 8000
```

Luego visita `http://localhost:8000`.

## Agregar un proyecto

1. Coloca la imagen de presentación en `images/projects/` (JPG, PNG o WebP).
2. Abre `projects.js` y añade una entrada al array:

```javascript
{
    image: 'images/projects/mi-proyecto.jpg',
    alt: 'Descripción breve del proyecto para accesibilidad'
}
```

La imagen aparecerá automáticamente en la sección **Proyectos y Prototipos**. Si existe una versión `.webp` con el mismo nombre, se usará para mejor rendimiento.

## Contacto

WhatsApp: [+57 318 261 1489](https://wa.me/573182611489)
