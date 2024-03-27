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
