document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.video-slide');
    const owlDots = document.querySelectorAll('.owl-dot');
    let currentSlide = 0;
    let isPlaying = false;

    function playNextSlide() {
        if (!isPlaying) {
            isPlaying = true;
            playVideo(currentSlide);
            setTimeout(function() {
                isPlaying = false;
                goToNextSlide();
            }, getVideoDuration(currentSlide) * 1000);
        }
    }

    function goToNextSlide() {
        pauseVideo(currentSlide);
        currentSlide = (currentSlide + 1) % slides.length;
        updateActiveStates();
        playNextSlide();
    }

    function playVideo(slideIndex) {
        const video = slides[slideIndex].querySelector('video');
        video.currentTime = 0;
        video.play();
        slides[slideIndex].classList.add('active');
    }

    function pauseVideo(slideIndex) {
        const video = slides[slideIndex].querySelector('video');
        video.pause();
        slides[slideIndex].classList.remove('active');
    }

    function getVideoDuration(slideIndex) {
        const video = slides[slideIndex].querySelector('video');
        return video.duration;
    }

    function pauseVideos() {
        slides.forEach((slide, index) => {
            pauseVideo(index);
        });
    }

    function updateActiveStates() {
        slides.forEach((slide, index) => {
            if (index === currentSlide) {
                slide.classList.add('active');
                owlDots[index].classList.add('active');
            } else {
                slide.classList.remove('active');
                owlDots[index].classList.remove('active');
            }
        });
    }
    playNextSlide();
});