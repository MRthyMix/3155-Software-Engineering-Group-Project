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
