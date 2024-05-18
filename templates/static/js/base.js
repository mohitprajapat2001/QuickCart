// script.js
$(document).ready(() => {
    // Custom Loader JS
    $(window).on('load', function () {
        $("#loading-beat").fadeOut(300)
    });
    // Custom Shortcut to Focus Nav Input
    $(document).keydown(function (event) {
        if (event.ctrlKey && event.key === '/') {
            event.preventDefault();
            $('#nav-input').focus();
        }
    });
});
