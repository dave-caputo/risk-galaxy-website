$(document).ready(function() {


    var anchors = ('home, ' + $('.page_data').data('anchors')).split(", ");

    $('#fullpage').fullpage({
        afterLoad: function(anchorLink, index) {

            if (index != 1) {
                $('.navbar-brand').removeClass('text-transparent');
                $('.navbar-toggler svg')
                    .removeClass('text-white')
                    .addClass('text-galaxy');
            }
        },
        anchors: anchors,
        loopHorizontal: false,
        menu: '.navbar-nav',
        onLeave: function(index, nextIndex, direction) {
            var leavingSection = $(this);

            //after leaving section 2
            if (nextIndex == 1) {
                $('.navbar-brand').addClass('text-transparent');
                $('.navbar-toggler svg')
                    .removeClass('text-galaxy')
                    .addClass('text-white');
            }
        },
        navigationTooltips: ['firstSlide', 'secondSlide'],
        scrollHorizontally: true,
        slidesNavigation: false,
        slidesNavPosition: 'bottom',
        verticalCentered: true,
    });

});
