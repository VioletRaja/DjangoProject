function toggleNestedMenu(event, id) {
    event.preventDefault();

    // Remove 'active' class from all items
    const activeItems = document.querySelectorAll('.blog-categories .active');
    activeItems.forEach(item => {
        item.classList.remove('active');
    });

    // Add 'active' class to the clicked item
    const clickedItem = document.getElementById('currect-' + id);
    clickedItem.classList.add('active');

    // Your existing logic to toggle nested menu display goes here
}
