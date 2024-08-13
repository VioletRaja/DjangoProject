function smoothScroll(event, targetId) {
    event.preventDefault();
    const targetElement = document.getElementById(targetId);
    targetElement.scrollIntoView({ behavior: 'smooth' });
    highlightSection(targetId);
}

function toggleNestedMenu(event, targetId) {
    event.preventDefault();
    const nestedMenu = document.querySelector(`#${targetId} .nested-menu`);
    if (nestedMenu.style.display === 'none' || !nestedMenu.style.display) {
        nestedMenu.style.display = 'block';
        event.currentTarget.querySelector('.arrow').textContent = '▼';
    } else {
        nestedMenu.style.display = 'none';
        event.currentTarget.querySelector('.arrow').textContent = '▶';
    }
}

function highlightSection(targetId) {
    // Remove highlight from all sections
    const sections = document.querySelectorAll('section');
    sections.forEach(section => section.classList.remove('highlight'));

    // Add highlight to the target section
    const targetSection = document.getElementById(targetId);
    targetSection.classList.add('highlight');
}

// CSS to highlight the section
const style = document.createElement('style');
style.innerHTML = `
    .highlight {
        padding: 10px;
        background-color: #ffffe0;
    }
`;
document.head.appendChild(style);
