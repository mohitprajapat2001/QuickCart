$(function () {

    var owl = $('.owl-1');
    owl.owlCarousel({
        loop: true,
        autoplay: true,
        margin: 0,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        nav: true,
        dots: true,
        autoplayHoverPause: false,
        items: 1,
        navText: ['<span class="icon-keyboard_arrow_left">', '<span class="icon-keyboard_arrow_right">']
    });

    var carousel_nav_a = $('.carousel-nav a');

    carousel_nav_a.each(function (slide_index) {
        var $this = $(this);
        $this.attr('data-num', slide_index);
        $this.click(function (e) {
            owl.trigger('to.owl.carousel', [slide_index, 1500]);
            e.preventDefault();
        })
    })

    owl.on('changed.owl.carousel', function (event) {
        carousel_nav_a.removeClass('active');
        $(".carousel-nav a[data-num=" + event.item.index + "]").addClass('active');
    })


})