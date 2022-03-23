let menu = document.querySelector(".menu");
let hamburger = document.querySelector(".hamburger");
let xIcon = document.querySelector(".xIcon");
let menuIcon = document.querySelector(".menuIcon");

hamburger.addEventListener("click", moveMenu);

function moveMenu() {
    if (menu.classList.contains("menuDown")) {
        $(".menu").removeClass("menuDown");
        $(".menuLink").addClass("d-none");
        $(".menu").attr('id', 'menu-bg');
        $(".xIcon").removeClass("d-block");
        $(".xIcon").addClass("d-none");
        menuIcon.style.display = "block";
    } else {
        menu.classList.add("menuDown");
        $(".menuLink").removeClass("d-none");
        $(".menu").removeAttr('id');
        $(".xIcon").removeClass("d-none");
        $(".xIcon").addClass("d-block");
        menuIcon.style.display = "none";
    }
}

// let menuLinks = document.querySelectorAll(".menuLink");

// for (let link of menuLinks) {
//     link.addEventListener("click", moveMenu);
// }