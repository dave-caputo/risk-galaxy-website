$(document).ready(function() {

    $('#fullpage').fullpage({
        afterLoad: function(anchorLink, index) {

            if (index != 1) {
                $('.navbar-brand').removeClass('d-none').fadeIn(600);
            }

        },
        anchors: ['home', 'product', 'zen', 'investors', 'about'],
        menu: '.navbar-nav',
        // navigation: true,
        onLeave: function(index, nextIndex, direction) {
            var leavingSection = $(this);

            //after leaving section 2
            if (nextIndex == 1) {
                $('.navbar-brand').fadeOut(200).addClass('d-none');

            }
        },
        navigationTooltips: ['firstSlide', 'secondSlide'],
        // sectionsColor: ['blue', 'red', 'yellow'],
        verticalCentered: true,
        slidesNavigation: false,
        slidesNavPosition: 'bottom',
    });
});
