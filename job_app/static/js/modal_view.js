// Abrir el modal de la vista

    function openViewModal(id) {
        const modal = document.getElementById('viewModal');
        const modalContent = document.getElementById('modalContent');

        // Realiza una solicitud para obtener los detalles
        fetch(`/api/job/${id}/`)
            .then(response => response.json())
            .then(data => {
                // Actualizar contenido dinámico
                modalContent.innerHTML = `
                    <p><strong>Job Title:</strong> ${data.job_title}</p>
                    <p><strong>Company:</strong> ${data.company_name}</p>
                    <p><strong>Application Date:</strong> ${data.application_date}</p>
                    <p><strong>Closing Date:</strong> ${data.closing_date || 'N/A'}</p>
                    <p><strong>Status:</strong> ${data.get_status_display}</p>
                    <p class="overflow-hidden"><strong>Notes:</strong> ${data.notes || 'N/A'}</p>
                `;
                modal.classList.remove('hidden');
            });
    }

    function closeViewModal() {
        const modal = document.getElementById('viewModal');
        modal.classList.add('hidden');
    }
