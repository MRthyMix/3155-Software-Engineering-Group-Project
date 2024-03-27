// JavaScript code for FAQ dropdown functionality
document.addEventListener("DOMContentLoaded", function() {
    const faqItems = document.querySelectorAll(".faq-item");
  
    faqItems.forEach(function(item) {
      const question = item.querySelector(".question");
      const answer = item.querySelector(".answer");
      const toggle = question.querySelector(".toggle");
  
      question.addEventListener("click", function() {
        answer.classList.toggle("active");
        toggle.classList.toggle("rotate"); // Toggle rotation class for plus sign
      });
    });
  });
  