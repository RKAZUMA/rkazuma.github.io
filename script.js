document.addEventListener('DOMContentLoaded', function() {
    // Actualizar el año en el footer
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }
});