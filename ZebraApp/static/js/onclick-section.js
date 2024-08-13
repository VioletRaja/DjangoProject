$(document).ready(function() {
    const services = {
        "service1": {
            "title": "ACP Cladding",
            "description": "Elevate your building's exterior aesthetics and functionality with ACP (Aluminum Composite Panel) Cladding services from Zebra Sign World. ACP Cladding is a versatile solution known for its durability, aesthetic appeal, and practical benefits in modern architecture.",
            "strategy": "Our strategy for ACP Cladding revolves around integrating innovative design, meticulous craftsmanship, and sustainable practices to enhance the exterior aesthetics and functionality of your property.",
            "features": [
                "Customized ACP Panels",
                "Expert Installation",
                "Maintenance and Support"
            ],
            "images": [
                "https://artfasad.com/wp-content/uploads/2020/08/black-and-white-design-of-a-two-story-house-outside-4-777x518.jpg.webp",
                "https://artfasad.com/wp-content/uploads/2020/08/black-and-white-design-of-a-two-story-house-outside-4-777x518.jpg.webp",
                "https://artfasad.com/wp-content/uploads/2020/08/black-and-white-design-of-a-two-story-house-outside-4-777x518.jpg.webp"
            ],
            "quote": "Quote for ACP Cladding"
        },
        "service2": {
            "title": "Architectural Signage",
            "description": "Is a bespoke signage solution, through which brands are strengthened. Companies using this visual source of promotion are able to elevate their brand image, highlight corporate messaging and raise awareness around the products and services offered",
            "strategy": "We focus on delivering innovative architectural signage solutions that harmonize with the design ethos of each project.",
            "features": [
                "Design Expertise",
                "Material Selection ",
                "Project Management"
            ],
            "images": [
                "https://artfasad.com/wp-content/uploads/2020/08/black-and-white-design-of-a-two-story-house-outside-20-777x518.jpg.webp",
                "https://artfasad.com/wp-content/uploads/2020/08/black-and-white-design-of-a-two-story-house-outside-20-777x518.jpg.webp",
                "static/images/resource/service-002.jpg",
                "https://artfasad.com/wp-content/uploads/2020/08/black-and-white-design-of-a-two-story-house-outside-4-777x518.jpg.webp"
            ],
            "quote": "Quote for Architectural Signage"
        },
        "service3": {
            "title": "Pylon Signage",
            "description": "Because of its sheer height, pylon signs can be seen from a great distance, making them a wonderful advertisement for your business and a great tool for grabbing peoples' attention",
            "strategy": "Using high-quality materials and construction techniques to guarantee longevity and withstand outdoor elements.",
            "features": [
                "Design Flexibility",
                "Technological Integration",
                "Expertise and Support"
            ],
            "images": [
                "https://artfasad.com/wp-content/uploads/2020/08/black-and-white-design-of-a-two-story-house-outside-8.jpg.webp",
                "static/images/resource/service-002.jpg",
                "static/images/resource/service-001.jpg"
            ],
            "quote": "Quote for Pylon Signage"
        },
        "service4": {
            "title": "Unipole Signage",
            "description": "The large size of a pylon sign makes it a great canvas for beautifully portraying your company's message. Because they tend to be larger, you could find that you may have extra space to showcase images, logos and text without having to cram your design together.",
            "strategy": "Adhering to local regulations and safety standards throughout the design, installation, and maintenance phases to ensure the safety of both pedestrians and motorists.",
            "features": [
                "Customization Options",
                "Visibility Enhancements",
                "Project Management Expertise"
            ],
            "images": [
                "static/images/resource/service-001.jpg",
                "static/images/resource/service-002.jpg",
                "https://artfasad.com/wp-content/uploads/2020/08/black-and-white-design-of-a-two-story-house-outside-20-777x518.jpg.webp",
            ],
            "quote": "Quote for Unipole Signage"
        }
    };

    function updateServiceDetails(service) {
        $('.service-title').text(service.title);
        $('.service-description').html('<strong>' + service.title + '</strong><br>' + service.description);
        $('.service-strategy').text(service.strategy);

        const featureList = service.features.map(feature => '<li>' + feature + '</li>').join('');
        $('.service-features').html(featureList);

        const carousel = $('.single-item-carousel');
        carousel.owlCarousel('destroy');
        carousel.empty();
        service.images.forEach(function(imageSrc, index) {
            const figure = $('<figure class="image image-' + (index + 1) + '"><img src="' + imageSrc + '" alt="" /></figure>');
            carousel.append(figure);
        });
        carousel.owlCarousel({
            loop: true,
            nav: true,
            navText: ['<i class="fa fa-chevron-left"></i>', '<i class="fa fa-chevron-right"></i>'],
            dots: false,
            items: 1,
            autoplay: true,
            autoplayTimeout: 4000
        });

        $('.service-quote').html(service.quote);
    }

    $('.blog-categories li').click(function(e) {
        e.preventDefault();
        e.stopPropagation();

        const serviceKey = $(this).find('a').attr('href').substr(1);
        const service = services[serviceKey];


        if ($(this).hasClass('category-open')) {
            $('.blog-categories li').removeClass('active').find('.nested-menu').slideUp();
            $(this).toggleClass('active').find('.nested-menu').slideDown();
        } else {
            $('.blog-categories li').removeClass('active');
            $(this).addClass('active');
        }


        if (service) {
            updateServiceDetails(service);
        }
    });


    $('#category-signages').click(function(e) {
        e.preventDefault();
        e.stopPropagation();

        $('.nested-menu').slideDown();

        $('.nested-menu li').addClass('animated-item');
        setTimeout(function() {
            $('.nested-menu li').removeClass('animated-item');
        }, 1000); 
    });

    $('.nested-menu li').click(function(e) {
        e.preventDefault();
        e.stopPropagation();


        $('.nested-menu li').removeClass('active active-yellow');

        $(this).addClass('active active-yellow');

        const serviceKey = $(this).data('service');
        const service = services[serviceKey];


        if (service) {
            updateServiceDetails(service);
        }


        $(this).addClass('animated-item');
        setTimeout(function() {
            $('.nested-menu li').removeClass('animated-item');
        }, 1000);
    });


    const initialServiceKey = 'service1';
    updateServiceDetails(services[initialServiceKey]);
});
