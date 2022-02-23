let menu = document.querySelector(".menu");
let hamburger = document.querySelector(".hamburger");
let xIcon = document.querySelector(".xIcon");
let menuIcon = document.querySelector(".menuIcon");

hamburger.addEventListener("click", moveMenu);

function moveMenu() {
    if (menu.classList.contains("menuDown")) {
        menu.classList.remove("menuDown");
        xIcon.style.display = "none";
        menuIcon.style.display = "block";
    } else {
        menu.classList.add("menuDown");
        xIcon.style.display = "block";
        menuIcon.style.display = "none";
    }
}

let menuLinks = document.querySelectorAll(".menuLink");

for (let link of menuLinks) {
    link.addEventListener("click", moveMenu);
}