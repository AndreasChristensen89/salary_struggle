$('.action').click(moveMenu);

// When .action is clicked classes change the color, display, and placement of the action menu
// showing and hiding it
function moveMenu() {
    if ( $(".menu").hasClass("menuDown")) {
        $(".menu").removeClass("menuDown");
        $(".menu").addClass("d-block");
        $(".xIcon").removeClass("d-block");
        $(".xIcon").addClass("d-none");
        $(".menuIcon").addClass("d-block");
        $(".menuIcon").removeClass("d-none");
        $(".menu").animate({opacity: "0"}, 300);
    } else {
        $(".menu").addClass("menuDown");
        $(".xIcon").removeClass("d-none");
        $(".xIcon").addClass("d-block");
        $(".menuIcon").addClass("d-none");
        $(".menuIcon").removeClass("d-block");
        $(".menu").removeClass("d-block");
        $(".menu").animate({opacity: "1.0"}, 300);
    }
}

// let menuLinks = document.querySelectorAll(".menuLink");

for (let link of $(".menuLink")) {
    link.addEventListener("click", moveMenu);
}