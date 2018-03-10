$(document).ready(function() {

    var anchors = ('home, ' + $('.page_data').data('anchors')).split(", ");

    $('#fullpage').fullpage({
        afterLoad: function(anchorLink, index) {

            if (index != 1) {
                $('.navbar-brand').removeClass('d-none').fadeIn(600);
            }

        },
        anchors: anchors,
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
