$(document).ready(function() {

    $('body').show();


    var anchors = ('home, ' + $('.page_data').data('anchors')).split(", ");

    $('#fullpage').fullpage({
        afterLoad: function(anchorLink, index) {

            if (index != 1) {
                $('.navbar-brand').removeClass('text-transparent');
                $('.navbar-toggler svg')
                    .removeClass('text-white')
                    .addClass('text-galaxy');
            } else {
                $('#fp-nav ul li a span').addClass('bg-white');
            }
            $('.navbar-collapse').collapse('hide');
        },
        anchors: anchors,
        loopHorizontal: false,
        menu: '.navbar-nav',
        navigation: true,
        navigationPosition: 'right',
        onLeave: function(index, nextIndex, direction) {
            var leavingSection = $(this);

            //after leaving section 2
            if (nextIndex == 1) {
                $('.navbar-brand').addClass('text-transparent');
                $('.navbar-toggler svg')
                    .removeClass('text-galaxy')
                    .addClass('text-white');
            } else {
                $('#fp-nav ul li a span').removeClass('bg-white');
            }
        },
        scrollHorizontally: true,
        slidesNavigation: true,
        slidesNavPosition: 'bottom',
        verticalCentered: true,
    });

    $('#fp-nav ul li a span').addClass('bg-white');

    // Hide slide navigation on smaller viewports...
    $('.fp-slidesNav').addClass('d-lg-none');
});

$(document).on('click', '.dismiss_nav', function(event) {
    $('.navbar-collapse').collapse('hide');
});

$('.navbar-collapse').on('show.bs.collapse', function(event) {
    $(this).fadeIn('fast');
});

$('.navbar-collapse').on('hide.bs.collapse', function(event) {
    $(this).fadeOut();
});
