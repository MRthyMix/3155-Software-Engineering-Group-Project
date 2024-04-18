//Navbar 
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
  
// JavaScript for Slideshow
const images = document.querySelectorAll('.slideshow img');
let currentImage = 0;

function nextImage() {
  images[currentImage].classList.remove('active');
  currentImage = (currentImage + 1) % images.length;
  images[currentImage].classList.add('active');
}

// Show the first image initially
images[currentImage].classList.add('active');

// Automatically switch images every 3 seconds (adjust as needed)
setInterval(nextImage, 3000);



document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("contact-form").addEventListener("submit", function(event) {
        // Prevent the default behavior of the form submission
        event.preventDefault();
        
        // Add your code to handle the form submission here, such as sending the form data via AJAX
    });
});

