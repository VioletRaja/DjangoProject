function toggleNestedMenu(event, id) {
    event.preventDefault();
    var nestedMenu = document.querySelector('#' + id + ' .nested-menu');
    if (nestedMenu) {
        nestedMenu.classList.toggle('show');

        var services = nestedMenu.querySelectorAll('li');
        services.forEach(function(service) {
            service.style.backgroundColor = 'white';
            service.style.color = '#050505';
        });
    }
}