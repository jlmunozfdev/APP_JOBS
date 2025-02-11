 // Abrir el modal con los datos del registro seleccionado
 function openDeleteModal(id, jobTitle) {
    const modal = document.getElementById('deleteModal');
    const modalText = document.getElementById('deleteModalText');
    const deleteForm = document.getElementById('deleteForm');

    // Actualizar el texto del modal
    modalText.innerText = `Are you sure you want to delete the job "${jobTitle}"?`;

    // Actualizar la acción del formulario para eliminar
    deleteForm.action = `/delete/${id}/`;

    // Mostrar el modal
    modal.classList.remove('hidden');
}

// Cerrar el modal
function closeDeleteModal() {
    const modal = document.getElementById('deleteModal');
    modal.classList.add('hidden');
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
closeModalOutsideClick('deleteModal', '.bg-gray-100');
