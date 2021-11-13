let thumbnails = document.getElementsByClassName("carousel-thumbnail");

document.getElementById("carousel-selected").style.backgroundImage = `url(${thumbnails[0].src})`
thumbnails[0].classList.add("active-thumbnail")

let activeImages = document.getElementsByClassName("active-thumbnail");

for (var i = 0; i < thumbnails.length; i++) {
  thumbnails[i].addEventListener("mouseover", function () {
    if (activeImages.length > 0) {
      activeImages[0].classList.remove("active-thumbnail");
    }
    this.classList.add("active-thumbnail");
    document.getElementById("carousel-selected").style.backgroundImage = `url(${this.src})`;
  });
}