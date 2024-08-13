$(document).ready(function() {
    function animateCounter($element, countTo, duration) {
        $element.prop('Counter', 0).animate({
            Counter: countTo
        }, {
            duration: duration,
            easing: 'linear',
            step: function(now) {
                $element.text(Math.ceil(now));
            }
        });
    }

    function startCounters() {
        $('.count-text').each(function() {
            var $this = $(this),
                countTo = parseInt($this.attr('data-stop')),
                duration = parseInt($this.attr('data-speed'));

            animateCounter($this, countTo, duration);
        });
    }

    function resetCounters() {
        $('.count-text').each(function() {
            var $this = $(this);
            $this.text('0');
            $this.prop('Counter', 0);
        });
    }

    var hasAnimated = false;
    var sectionId = '#fun-fact-and-features';

    $(window).on('scroll', function() {
        var section = $(sectionId);
        var sectionTop = section.offset().top;
        var sectionBottom = sectionTop + section.outerHeight();
        var scrollTop = $(window).scrollTop();
        var scrollBottom = scrollTop + window.innerHeight;

        if (scrollBottom > sectionTop && scrollTop < sectionBottom) {
            if (!hasAnimated) {
                hasAnimated = true;
                startCounters();
            }
        } else {
            if (hasAnimated) {
                hasAnimated = false;
                resetCounters();
            }
        }
    });
});