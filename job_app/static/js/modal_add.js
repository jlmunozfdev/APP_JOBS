function openAddModal() {
    document.getElementById('addModalJob').classList.remove('hidden');
}

function closeAddModal() {
    document.getElementById('addModalJob').classList.add('hidden');
}

// Función para cerrar el modal al hacer clic fuera del contenido
function closeModalOutsideClick(modalId, contentClass) {
    const modal = document.getElementById(modalId);
    
    modal.addEventListener('click', function (event) {
        const modalContent = modal.querySelector(contentClass);
        if (!modalContent.contains(event.target)) {
            modal.classList.add('hidden');
        }
    })
}

// Agregar evento para cerrar al hacer clic fuera
closeModalOutsideClick('addModalJob', '.bg-gray-100');