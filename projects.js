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

function getSlidesPerView() {
    if (window.matchMedia('(min-width: 1024px)').matches) return 3;
    if (window.matchMedia('(min-width: 768px)').matches) return 2;
    return 1;
}

function renderProjects() {
    const track = document.getElementById('projects-grid');
    if (!track) return;

    track.innerHTML = projects.map(function (project, index) {
        const webp = getWebpPath(project.image);
        return (
            '<article class="project-card">' +
                '<div class="project-card-inner">' +
                    '<button type="button" class="project-card-button" data-index="' + index + '" aria-label="Ver proyecto: ' + project.alt + '">' +
                        '<picture>' +
                            '<source srcset="' + webp + '" type="image/webp">' +
                            '<img src="' + project.image + '" alt="' + project.alt + '" loading="lazy" width="600" height="338">' +
                        '</picture>' +
                    '</button>' +
                '</div>' +
            '</article>'
        );
    }).join('');
}

function initProjectCarousel() {
    const track = document.getElementById('projects-grid');
    const dotsContainer = document.getElementById('carousel-dots');
    const prevBtn = document.querySelector('.carousel-prev');
    const nextBtn = document.querySelector('.carousel-next');

    if (!track || !dotsContainer || !prevBtn || !nextBtn) return;

    let currentIndex = 0;
    let slidesPerView = getSlidesPerView();
    let maxIndex = Math.max(0, projects.length - slidesPerView);

    function renderDots() {
        dotsContainer.innerHTML = '';
        for (let i = 0; i <= maxIndex; i++) {
            const dot = document.createElement('button');
            dot.type = 'button';
            dot.className = 'carousel-dot' + (i === currentIndex ? ' is-active' : '');
            dot.setAttribute('aria-label', 'Ir al proyecto ' + (i + 1));
            dot.setAttribute('aria-selected', String(i === currentIndex));
            dot.addEventListener('click', function () {
                goToSlide(i);
            });
            dotsContainer.appendChild(dot);
        }
    }

    function updateCarousel() {
        slidesPerView = getSlidesPerView();
        maxIndex = Math.max(0, projects.length - slidesPerView);
        if (currentIndex > maxIndex) currentIndex = maxIndex;

        const offset = (currentIndex * 100) / slidesPerView;
        track.style.transform = 'translateX(-' + offset + '%)';

        prevBtn.disabled = currentIndex === 0;
        nextBtn.disabled = currentIndex >= maxIndex;

        dotsContainer.querySelectorAll('.carousel-dot').forEach(function (dot, index) {
            const isActive = index === currentIndex;
            dot.classList.toggle('is-active', isActive);
            dot.setAttribute('aria-selected', String(isActive));
        });
    }

    function goToSlide(index) {
        currentIndex = Math.max(0, Math.min(index, maxIndex));
        updateCarousel();
    }

    prevBtn.addEventListener('click', function () {
        goToSlide(currentIndex - 1);
    });

    nextBtn.addEventListener('click', function () {
        goToSlide(currentIndex + 1);
    });

    window.addEventListener('resize', function () {
        renderDots();
        updateCarousel();
    });

    renderDots();
    updateCarousel();
}

function initProjectLightbox() {
    const lightbox = document.getElementById('project-lightbox');
    const lightboxImage = document.getElementById('lightbox-image');
    const lightboxCaption = document.getElementById('lightbox-caption');
    const lightboxCounter = document.getElementById('lightbox-counter');
    const closeBtn = document.querySelector('.lightbox-close');
    const prevBtn = document.querySelector('.lightbox-prev');
    const nextBtn = document.querySelector('.lightbox-next');
    const track = document.getElementById('projects-grid');

    if (!lightbox || !lightboxImage || !track) return;

    let currentIndex = 0;

    function showLightboxSlide(index) {
        const project = projects[index];
        if (!project) return;

        currentIndex = index;
        lightboxImage.src = project.image;
        lightboxImage.alt = project.alt;
        lightboxCaption.textContent = project.alt;
        lightboxCounter.textContent = (index + 1) + ' / ' + projects.length;
    }

    function openLightbox(index) {
        showLightboxSlide(index);
        lightbox.hidden = false;
        document.body.classList.add('lightbox-open');
        closeBtn.focus();
    }

    function closeLightbox() {
        lightbox.hidden = true;
        lightboxImage.src = '';
        document.body.classList.remove('lightbox-open');
    }

    function showPrevious() {
        const index = currentIndex === 0 ? projects.length - 1 : currentIndex - 1;
        showLightboxSlide(index);
    }

    function showNext() {
        const index = currentIndex === projects.length - 1 ? 0 : currentIndex + 1;
        showLightboxSlide(index);
    }

    track.addEventListener('click', function (event) {
        const button = event.target.closest('.project-card-button');
        if (!button) return;
        openLightbox(Number(button.dataset.index));
    });

    closeBtn.addEventListener('click', closeLightbox);
    prevBtn.addEventListener('click', showPrevious);
    nextBtn.addEventListener('click', showNext);

    lightbox.addEventListener('click', function (event) {
        if (event.target === lightbox) closeLightbox();
    });

    document.addEventListener('keydown', function (event) {
        if (lightbox.hidden) return;

        if (event.key === 'Escape') {
            closeLightbox();
        } else if (event.key === 'ArrowLeft') {
            showPrevious();
        } else if (event.key === 'ArrowRight') {
            showNext();
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    renderProjects();
    initProjectCarousel();
    initProjectLightbox();
});
