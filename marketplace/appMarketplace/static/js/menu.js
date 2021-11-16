document.getElementById("menu-btn").addEventListener("click" , function() {
    document.getElementById("menu-container").style.display = "flex";
    document.body.style.overflowY = "hidden";

})

document.getElementById("menu-close-btn").addEventListener("click" , function() {
    document.getElementById("menu-container").style.display = "none"
    document.body.style.overflowY = "visible";
})