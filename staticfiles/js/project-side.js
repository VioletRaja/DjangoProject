let currentImageIndex = 0;
const images = document.querySelectorAll('.carousel-image');
let projectInterval;
const projectIds = ["project1", "project2", "project3", "project4", "project5", "project6", "project7", "project8", "project9"];
let currentProjectIndex = 0;

function openSidebar(projectId) {
    document.getElementById("sidebar").style.width = "400px";
    loadProjectDetails(projectId);
}

function closeSidebar() {
    document.getElementById("sidebar").style.width = "0";
    clearInterval(projectInterval);
}

function loadProjectDetails(projectId) {
    const projectData = {
        project1: {
            title: "Luxury Home Project-1",
            description: "This is a detailed description of the Luxury Home Project.",
            images: ["Photos/Projects/New folder/IMG_3140.JPG"]
        },
        project2: {
            title: "Another Project-2",
            description: "This is a detailed description of Another Project.",
            images: ["Photos/Projects/New folder (2)/IMG_2647.JPG"]
        },
        project3: {
            title: "Another Project-3",
            description: "This is a detailed description of Another Project.",
            images: ["Photos/Projects/New folder (3)/IMG_8852.JPG"]
        },
        project4: {
            title: "Another Project-4",
            description: "This is a detailed description of Another Project.",
            images: ["Photos/Projects/New folder (4)/WhatsApp Image 2021-09-22 at 6.27.23 PM (2).jpeg"]
        },
        project5: {
            title: "Another Project-5",
            description: "This is a detailed description of Another Project.",
            images: ["Photos/Projects/New folder (5)/IMG_6569.JPG"]
        },
        project6: {
            title: "Another Project-6",
            description: "This is a detailed description of Another Project.",
            images: ["Photos/Projects/New folder (6)/IMG_5628.JPG"]
        },
        project7: {
            title: "Another Project-7",
            description: "This is a detailed description of Another Project.",
            images: ["Photos/Projects/New folder (7)/IMG_8177.JPG"]
        },
        project8: {
            title: "Another Project-8",
            description: "This is a detailed description of Another Project.",
            images: ["Photos/Projects/IMG_6108.JPG"]
        },
        project9: {
            title: "Another Project-9",
            description: "This is a detailed description of Another Project.",
            images: ["Photos/Projects/IMG_7596.JPG"]
        }
    };

    const project = projectData[projectId];

    if (project) {
        document.getElementById("project-title").innerText = project.title;
        document.getElementById("project-description").innerText = project.description;

        images.forEach((img, index) => {
            if (project.images[index]) {
                img.src = project.images[index];
                img.classList.add('active');
            } else {
                img.classList.remove('active');
            }
        });

        currentImageIndex = 0;
        showImage(currentImageIndex);
    }
}

function showImage(index) {
    images.forEach((img, i) => {
        img.classList.remove('active');
        if (i === index) {
            img.classList.add('active');
        }
    });
}

function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    showImage(currentImageIndex);
}

function prevImage() {
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    showImage(currentImageIndex);
}

// Add event listeners to arrow buttons
document.getElementById('next-arrow').addEventListener('click', nextImage);
document.getElementById('prev-arrow').addEventListener('click', prevImage);

// Initialize with the first project
loadProjectDetails(projectIds[currentProjectIndex]);
