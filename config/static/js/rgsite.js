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
            }
            $('.navbar-collapse').collapse('hide');
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

$(document).on('click', '.dismiss_nav', function(event) {
    $('.navbar-collapse').collapse('hide');
});

$('.navbar-collapse').on('show.bs.collapse', function(event) {
    $(this).fadeIn('fast');
});

$('.navbar-collapse').on('hide.bs.collapse', function(event) {
    $(this).fadeOut();
});
