$(document).ready(function() {

    $('body').show();

    $(document).trigger('getPhoneCodes');

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
        // autoScrolling: false,
        // controlArrows: false,
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
        onSlideLeave: function(
            anchorLink, index, slideIndex, direction, nextSlideIndex) {

            var slideNum = nextSlideIndex + 1

            $('.nav .nav-link').removeClass('active');
            $('#id_slide' + slideNum).addClass('active');
        },
        scrollHorizontally: true,
        slidesNavigation: true,
        slidesNavPosition: 'bottom',
        verticalCentered: false,
    });

    $('.fp-next').html('<i class="fas fa-chevron-circle-right fa-2x"></i>')
    $('.fp-prev').html('<i class="fas fa-chevron-circle-left fa-2x"></i>')

    $('#fp-nav ul li a span').addClass('bg-white');

    // Show slide navigation on smaller viewports...
    $('.fp-slidesNav').addClass('d-lg-none');

    // Hide slide arrows on smaller viewports...
    // $('.fp-controlArrow').addClass('d-none d-lg-block');
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


/*=================================================
=             GET CLIENT INQUIRY FORM             =
=================================================*/


$(document).on('click', '.demo_request_get_button', function(event) {
    event.preventDefault();

    $.ajax({
            url: '/clients/demo-request-create/',
            type: 'GET',
        })
        .done(function(data) {

            // Load data to DOM...
            $('.modal-body').html(data);

            // Display submit button...
            $('.demo_request_post_btn').removeClass('d-none');

            // Launch modal...
            $('#homeModalCenter').modal({
                keyboard: false,
                backdrop: 'static'
            });

            // Prevent fullpage.js from scrolling...
            $.fn.fullpage.setAllowScrolling(false);

            // Set pretty country-select field...
            $("#id_country").countrySelect();
        })
});

$(document).on('hide.bs.modal', function(event) {

    // Re-enable fullpage.js scrolling...
    $.fn.fullpage.setAllowScrolling(true);
});


/*=================================================
=            SET COUNTRY DIALLING CODE            =
=================================================*/


$(document).on('input change', '#id_country', function(event) {
    var code = $("#id_country").countrySelect("getSelectedCountryData")
        .iso2
        .toUpperCase();

    var pcode = phoneCodes[code]

    $('.input-group-text').html('+' + pcode);
});


/*=================================================
=            POST CLIENT INQUIRY FORM             =
=================================================*/


$(document).on('click', '.demo_request_post_btn', function(event) {
    event.preventDefault();

    $.ajax({
            url: '/clients/demo-request-create/',
            type: 'POST',
            data: $('#demo_request_form').serialize()
        })
        .done(function(data) {

            // Load modal...
            $('.modal-body').html(data);

            // hide button...
            $('.demo_request_post_btn').addClass('d-none');
        })
});
