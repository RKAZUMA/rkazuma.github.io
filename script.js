document.addEventListener('DOMContentLoaded', function () {
    const currentYearEl = document.getElementById('current-year');
    if (currentYearEl) {
        const year = new Date().getFullYear();
        currentYearEl.textContent = year;
        currentYearEl.setAttribute('datetime', String(year));
    }

    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.getElementById('nav-menu');

    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', function () {
            const isOpen = navMenu.classList.toggle('is-open');
            menuToggle.setAttribute('aria-expanded', String(isOpen));
            menuToggle.setAttribute(
                'aria-label',
                isOpen ? 'Cerrar menú de navegación' : 'Abrir menú de navegación'
            );
        });

        navMenu.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                navMenu.classList.remove('is-open');
                menuToggle.setAttribute('aria-expanded', 'false');
                menuToggle.setAttribute('aria-label', 'Abrir menú de navegación');
            });
        });

        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape' && navMenu.classList.contains('is-open')) {
                navMenu.classList.remove('is-open');
                menuToggle.setAttribute('aria-expanded', 'false');
                menuToggle.setAttribute('aria-label', 'Abrir menú de navegación');
                menuToggle.focus();
            }
        });
    }
});
