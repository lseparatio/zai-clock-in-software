// Navbar Mobile

$(document).ready(function () {
    $('.sidenav').sidenav({ edge: "right" });
});

// Character counter
$(document).ready(function () {
    $('input#username, input#password, input#phone_number').characterCounter();
});

// Floating Action Button
$(document).ready(function () {
    $('.fixed-action-btn').floatingActionButton();
});

// Modal
$(document).ready(function () {
    $('.modal').modal();
});

// Collapsible
$(document).ready(function () {
    $('.collapsible').collapsible();
});