var logo = document.querySelector("#logo");

function goHome() {
    window.location.href = "https://mysite-xqn6.onrender.com/";
}

var icon = document.querySelector("#user-icon");

function dontWork() {
    window.location.href = "/under_construction";
}
// Mobile nav ------------------------------------------------------------------------------------------

var close = document.querySelector("#close");
var ham = document.querySelector("#ham");
var bottom_navbar = document.querySelector(".bottom_navbar");

function show() {
    ham.style.display = "none";
    close.style.display = "flex";
    bottom_navbar.classList.replace("bottom_navbar", "bottom_navbar_mobile");

}

function hide() {    
    close.style.display = "none";
    ham.style.display = "flex";
    bottom_navbar.classList.replace("bottom_navbar_mobile", "bottom_navbar");

}

var sign_in_text_content = document.querySelector("#sign-in-text");

if (screen.width <= 430){
    sign_in_text_content.style.display = "none";
}

//SUCESSS-grab--------------------------------------------------------------------------
var login_area_toggle = document.querySelector(".login-area-show");
var success_area_toggle = document.querySelector(".success-area-hide");
var success_area_show = document.querySelector(".success-area-show");


function success() {
  login_area_toggle.classList.replace("login-area-show", "login-area-hide");
  success_area_toggle.classList.replace("success-area-hide", "success-area-show");
}
