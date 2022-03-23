let menu = document.querySelector(".menu");

$('.hamburger').click(moveMenu);

function moveMenu() {
    if (menu.classList.contains("menuDown")) {
        $(".menu").removeClass("menuDown");
        $(".menuLink").addClass("d-none");
        $(".menu").attr('id', 'menu-bg');
        $(".xIcon").removeClass("d-block");
        $(".xIcon").addClass("d-none");
        $(".menuIcon").addClass("d-block");
        $(".menuIcon").removeClass("d-none");
    } else {
        menu.classList.add("menuDown");
        $(".menuLink").removeClass("d-none");
        $(".menu").removeAttr('id');
        $(".xIcon").removeClass("d-none");
        $(".xIcon").addClass("d-block");
        $(".menuIcon").addClass("d-none");
        $(".menuIcon").removeClass("d-block");
    }
}

// let menuLinks = document.querySelectorAll(".menuLink");

// for (let link of menuLinks) {
//     link.addEventListener("click", moveMenu);
// }