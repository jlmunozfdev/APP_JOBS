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