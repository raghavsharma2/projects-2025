let currentIndex = 0;

function changeSlide(direction) {
    const slides = document.querySelectorAll('.slides img');
    const totalSlides = slides.length;

    currentIndex += direction;

    if (currentIndex < 0) {
        currentIndex = totalSlides - 1;
    } else if (currentIndex >= totalSlides) {
        currentIndex = 0;
    }

    const slideWidth = slides[0].client
}