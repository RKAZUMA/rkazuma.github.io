/**
 * Proyectos / prototipos
 *
 * Para agregar un proyecto:
 * 1. Coloca la imagen en images/projects/
 * 2. Añade una entrada aquí con la ruta y una descripción breve (alt)
 */
const projects = [
    {
        image: 'images/projects/saratex-inventario-resumen.jpg',
        alt: 'SARATEX S.A.S - Sistema de inventario de telas: productos, códigos de barras, facturas y reportes Excel'
    },
    {
        image: 'images/projects/saratex-inventario-dashboard.jpg',
        alt: 'SARATEX S.A.S - Dashboard de gestión de inventario de telas con control de stock en tiempo real'
    },
    {
        image: 'images/projects/marco-barbershop-reserva.jpg',
        alt: 'MARCO Barber Shop - Reserva de citas en línea: selección de servicio, fecha, hora y confirmación por WhatsApp'
    },
    {
        image: 'images/projects/marco-barbershop-citas.jpg',
        alt: 'MARCO Barber Shop CITAS - Sistema de gestión de citas con dashboard, calendario y control de barberos'
    },
    {
        image: 'images/projects/sabores-valle-catalogo.jpg',
        alt: 'Sabores del Valle - Catálogo digital interactivo con productos, fotos, precios y carrito de compras'
    },
    {
        image: 'images/projects/sabores-valle-whatsapp.jpg',
        alt: 'Sabores del Valle - Pedidos por WhatsApp: mensaje estructurado automático con detalle del carrito al negocio'
    },
    {
        image: 'images/projects/cotizapro-cotizador.jpg',
        alt: 'CotizaPro - Generador de cotizaciones con selección de clientes, servicios e impuestos automáticos'
    },
    {
        image: 'images/projects/cotizapro-pdf-analytics.jpg',
        alt: 'CotizaPro - PDF proforma con diseño corporativo y panel de tasa de aprobación de cotizaciones'
    },
    {
        image: 'images/projects/flotaviva-dashboard.jpg',
        alt: 'FlotaViva - Control de flotas con registro de vehículos y alertas de vencimiento de documentos legales'
    },
    {
        image: 'images/projects/flotaviva-mantenimiento.jpg',
        alt: 'FlotaViva - Historial de mantenimientos preventivos y correctivos con gráfico de consumo de gasolina'
    },
    {
        image: 'images/projects/horizonte-landing.jpg',
        alt: 'Estudio Horizonte Arquitectura - Página web de presentación con portafolio de casas y edificios'
    },
    {
        image: 'images/projects/horizonte-servicios.jpg',
        alt: 'Estudio Horizonte Arquitectura - Servicios de análisis, diseño arquitectónico y construcción'
    }
];

function getWebpPath(imagePath) {
    return imagePath.replace(/\.(png|jpe?g)$/i, '.webp');
}

function renderProjects() {
    const grid = document.getElementById('projects-grid');
    if (!grid) return;

    grid.innerHTML = projects.map(function (project, index) {
        const webp = getWebpPath(project.image);
        return (
            '<article class="project-card">' +
                '<button type="button" class="project-card-button" data-index="' + index + '" aria-label="Ver proyecto: ' + project.alt + '">' +
                    '<picture>' +
                        '<source srcset="' + webp + '" type="image/webp">' +
                        '<img src="' + project.image + '" alt="' + project.alt + '" loading="lazy" width="600" height="338">' +
                    '</picture>' +
                '</button>' +
            '</article>'
        );
    }).join('');
}

function initProjectLightbox() {
    const lightbox = document.getElementById('project-lightbox');
    const lightboxImage = document.getElementById('lightbox-image');
    const lightboxCaption = document.getElementById('lightbox-caption');
    const closeBtn = document.querySelector('.lightbox-close');
    const grid = document.getElementById('projects-grid');

    if (!lightbox || !lightboxImage || !grid) return;

    function openLightbox(index) {
        const project = projects[index];
        if (!project) return;

        lightboxImage.src = project.image;
        lightboxImage.alt = project.alt;
        lightboxCaption.textContent = project.alt;
        lightbox.hidden = false;
        document.body.classList.add('lightbox-open');
        closeBtn.focus();
    }

    function closeLightbox() {
        lightbox.hidden = true;
        lightboxImage.src = '';
        document.body.classList.remove('lightbox-open');
    }

    grid.addEventListener('click', function (event) {
        const button = event.target.closest('.project-card-button');
        if (!button) return;
        openLightbox(Number(button.dataset.index));
    });

    closeBtn.addEventListener('click', closeLightbox);

    lightbox.addEventListener('click', function (event) {
        if (event.target === lightbox) closeLightbox();
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && !lightbox.hidden) closeLightbox();
    });
}

document.addEventListener('DOMContentLoaded', function () {
    renderProjects();
    initProjectLightbox();
});
