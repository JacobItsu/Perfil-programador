document.addEventListener('DOMContentLoaded', () => {
    inicializarEventos();
});

function inicializarEventos() {
    const botonTelefono = document.getElementById('btn-phone');
    if (botonTelefono) {
        botonTelefono.addEventListener('click', mostrarTelefono);
    }
}

function mostrarTelefono() {
    const contenedorTelefono = document.getElementById('phone-display');
    const numeroTelefono = '04242285272';
    
    if (contenedorTelefono.textContent === '') {
        contenedorTelefono.textContent = `📞 ${numeroTelefono}`;
        this.textContent = 'Ocultar Teléfono';
    } else {
        contenedorTelefono.textContent = '';
        this.textContent = 'Ver Teléfono';
    }
}
