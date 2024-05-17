$(document).ready(() => {
    // Custom Shortcut to Focus Nav Input
    $(document).keydown(function (event) {
        if (event.ctrlKey && event.key === '/') {
            event.preventDefault();
            $('#nav-input').focus();
        }
    });
})