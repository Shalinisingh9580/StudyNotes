function searchChapters() {

    let input = document.getElementById("searchInput").value.toLowerCase();

    let chapters = document.getElementsByClassName("chapter-card");

    for (let i = 0; i < chapters.length; i++) {

        let title = chapters[i].getElementsByTagName("h3")[0].innerText.toLowerCase();

        if (title.includes(input)) {
            chapters[i].style.display = "flex";
        } else {
            chapters[i].style.display = "none";
        }
    }
}
function toggleDarkMode(){

    document.body.classList.toggle("dark-mode");

}
// Back to Top Button

let mybutton = document.getElementById("topBtn");

window.onscroll = function(){

    if(document.body.scrollTop > 200 || document.documentElement.scrollTop > 200){

        mybutton.style.display = "block";

    }else{

        mybutton.style.display = "none";

    }

}

function topFunction(){

    window.scrollTo({

        top:0,

        behavior:"smooth"

    });

}
const reveals = document.querySelectorAll(".reveal");

window.addEventListener("scroll", () => {
    reveals.forEach((element) => {
        const windowHeight = window.innerHeight;
        const elementTop = element.getBoundingClientRect().top;

        if (elementTop < windowHeight - 100) {
            element.classList.add("active");
        }
    });
});

window.addEventListener("load", function () {
    document.getElementById("loader").style.display = "none";
});