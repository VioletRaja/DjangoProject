var imageSets = JSON.parse(document.getElementById('imageSetsData').textContent);
var currentIndex = 0;
var currentSet = '';

function showFullImage(set) {
    currentSet = 'set' + set;
    if (imageSets[currentSet] && imageSets[currentSet].length > 0) {
        currentIndex = 0;
        var fullImage = document.getElementById("fullImage");
        fullImage.src = imageSets[currentSet][currentIndex];
        document.getElementById("fullImageModal").style.display = "block";
    } else {
        console.error("Image set not found or it is empty:", currentSet);
    }
}

function closeModal() {
    var modal = document.getElementById("fullImageModal");
    modal.style.display = "none";
}

function changeImage(direction) {
    var images = imageSets[currentSet];
    if (!images || images.length === 0) return;

    currentIndex += direction;
    if (currentIndex < 0) {
        currentIndex = images.length - 1; // Move to the last image in the current set
    } else if (currentIndex >= images.length) {
        currentIndex = 0; // Move to the first image in the current set
    }

    var fullImage = document.getElementById("fullImage");
    fullImage.src = images[currentIndex];
}

document.getElementById('prev-arrow').addEventListener('click', function() {
    changeImage(-1);
});
document.getElementById('next-arrow').addEventListener('click', function() {
    changeImage(1);
});
