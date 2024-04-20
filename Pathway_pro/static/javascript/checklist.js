function toggleChecklist(event, checklistId) {
    event.preventDefault();
    
    const options = document.getElementById(checklistId);
    const toggleButton = document.querySelector(`button[onclick="toggleChecklist('${checklistId}')"]`);
    
    if (options.style.maxHeight === '0px' || options.style.maxHeight === '') {
        options.style.maxHeight = '500px'; // Adjust to fit content
        options.style.opacity = '1';
        toggleButton.classList.add('expanded');
    } else {
        options.style.maxHeight = '0';
        options.style.opacity = '0';
        toggleButton.classList.remove('expanded');
    }
}
