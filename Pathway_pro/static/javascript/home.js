//Navbar Navigation
function navigateTo(page) {
    window.location.href = page;
}

//FAQ dropdown
document.addEventListener('DOMContentLoaded', function() {
    const questions = document.querySelectorAll('.question');
    
    questions.forEach(function(question) {
        question.addEventListener('click', function() {
            // Toggle the 'active' class on the clicked question
            question.classList.toggle('active');
            
            // Toggle the display of the corresponding answer
            const answer = question.nextElementSibling;
            if (answer.style.display === 'block') {
                answer.style.display = 'none';
            } else {
                answer.style.display = 'block';
            }
        });
    });
  });
  

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("contact-form").addEventListener("submit", function(event) {
        // Prevent the default behavior of the form submission
        event.preventDefault();
        
        // Add your code to handle the form submission here, such as sending the form data via AJAX
    });
});

