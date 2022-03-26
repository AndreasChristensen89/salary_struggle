$('.action').click(moveMenu);

// When .action is clicked classes change the color, display, and placement of the action menu
// showing and hiding it
function moveMenu() {
    if ( $(".menu").hasClass("menuDown")) {
        $(".menu").removeClass("menuDown");
        $(".menuLink").addClass("d-none");

        $(".xIcon").removeClass("d-block");
        $(".xIcon").addClass("d-none");
        $(".menuIcon").addClass("d-block");
        $(".menuIcon").removeClass("d-none");
        setTimeout(() => {
            $(".menu").attr('id', 'large-bg');
        }, 300);
    } else {
        $(".menu").addClass("menuDown");
        $(".menuLink").removeClass("d-none");
        $(".xIcon").removeClass("d-none");
        $(".xIcon").addClass("d-block");
        $(".menuIcon").addClass("d-none");
        $(".menuIcon").removeClass("d-block");
        $(".menu").removeAttr('id', 'large-bg');
    }
}

// let menuLinks = document.querySelectorAll(".menuLink");

for (let link of $(".menuLink")) {
    link.addEventListener("click", moveMenu);
}