function openEditModal(jobId) {
    console.log("Opening edit modal for job ID:", jobId); 
    fetch(`/api/job/${jobId}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Data received:", data); // Debugging

            // Verifica que el formulario tenga la acción correcta
            document.getElementById('editJobForm').action = `/edit/${jobId}/`;

            // Llenar los campos del formulario
            document.getElementById('edit_job_title').value = data.job_title || '';
            document.getElementById('edit_company_name').value = data.company_name || '';
            document.getElementById('edit_requirements').value = data.requirements || '';
            document.getElementById('edit_contact_name').value = data.contact_name || '';
            document.getElementById('edit_contact_phone').value = data.contact_phone || '';
            document.getElementById('edit_application_date').value = data.application_date || '';
            document.getElementById('edit_closing_date').value = data.closing_date || '';

            // Seleccionar el estado correcto en el select
            let statusField = document.getElementById('edit_status');
            for (let i = 0; i < statusField.options.length; i++) {
                if (statusField.options[i].value === data.status) {
                    statusField.options[i].selected = true;
                    break;
                }
            }

            document.getElementById('edit_notes').value = data.notes || '';

            // Mostrar el modal
            document.getElementById('editModalJob').classList.remove('hidden');
        })
        .catch(error => {
            console.error("Error fetching job details:", error);
        });
}

function closeEditModal() {
    console.log("Closing edit modal");
    document.getElementById('editModalJob').classList.add('hidden');
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
closeModalOutsideClick('editModalJob', '.bg-gray-100');
