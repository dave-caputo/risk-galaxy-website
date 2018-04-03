$(document).ready(function() {

    $('.home-item').hide();

    $('body').show();

    $(document).trigger('getPhoneCodes');

    var anchors = ('home, ' + $('.page_data').data('anchors')).split(", ");

    $('#fullpage').fullpage({
        afterLoad: function(anchorLink, index) {

            if (index != 1) {

                $('.navbar-brand').removeClass('text-transparent');
                $('.login_btn')
                    .removeClass('btn-success')
                    .addClass('btn-outline-success');
                $('.navbar-toggler svg')
                    .removeClass('text-white')
                    .addClass('text-galaxy');

            } else {

                $('.home-item').fadeOut();
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

                $('.login_btn')
                    .removeClass('btn-outline-success')
                    .addClass('btn-success');

                $('.navbar-toggler svg')
                    .removeClass('text-galaxy')
                    .addClass('text-white');
            } else {

                $('.home-item').fadeIn();
                $('#fp-nav ul li a span').removeClass('bg-white');
            }
        },
        onSlideLeave: function(
            anchorLink, index, slideIndex, direction, nextSlideIndex) {

            var slideNum = nextSlideIndex + 1

            $('.nav .nav-link').removeClass('active');
            $('#' + anchorLink + '-slide' + slideNum).addClass('active');
        },
        scrollHorizontally: true,
        slidesNavigation: true,
        slidesNavPosition: 'bottom',
        verticalCentered: false,

        // Responsive settings...
        // responsiveWidth: 768,
        // responsiveHeight: 637,
        // responsiveSlides: true
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
=            SET COUNTRY DIALLING CODE            =
=================================================*/

function getPhoneCode() {

    var countryCode = $('#id_country', '#demo_request_form')
        .countrySelect("getSelectedCountryData")
        .iso2
        .toUpperCase();

    // Look up code... (note: phoneCodes is assigned in separate .js file)
    return phoneCodes[countryCode]
}

$(document).on('input change', '#id_country', function(event) {

    var phc = getPhoneCode()

    // Update phone field prepend...
    $('.input-group-text', '#div_id_phone').text('+' + phc);

    // Update value of form phone code field...
    $('#id_phone_code', '#demo_request_form').val(phc);
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
            $('#id_country', '.modal-body').countrySelect();


            var phc = getPhoneCode()
            // Update phone field prepend...
            $('.input-group-text', '#div_id_phone').text('+' + phc);

            // Set value for phone code...
            $('#id_phone_code').val(phc)
        })
});

$(document).on('hide.bs.modal', function(event) {

    // Re-enable fullpage.js scrolling...
    $.fn.fullpage.setAllowScrolling(true);
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

            // $('#id_country', '#modal-body').countrySelect('destroy');

            // Display data...
            $('.modal-body').html(data);

            // If no form is valid...
            if (!$(data).find('.is-invalid').length) {
                console.log('no errors found');

                // Hide post button...
                $('.demo_request_post_btn').addClass('d-none');
            }

            // If form is invalid...
            else {

                // Store value of the country field and clear. This is
                // needed to avoid errors when initialising
                // countrySelect...
                var selCountry = $('#id_country').val();
                $('#id_country').val('');

                // Setup country-select field with country flags...
                $('#id_country').countrySelect();

                // Select instance value...
                $('#id_country').countrySelect('setCountry', selCountry);

                // Insert phone code into phone field input prepend...
                $('.input-group-text', '#div_id_phone')
                    .text('+' + getPhoneCode());
            }

        })
});
