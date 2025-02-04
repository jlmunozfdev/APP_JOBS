function generateReportCSV() {
    let selectedStatus = document.getElementById('status_bulk').value;
    window.location.href = `/generate-report-csv/?status=${selectedStatus}`;
}
