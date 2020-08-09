const toggleButton = document.getElementsByClassName("hamburger")[0];
const navbarLinks = document.getElementsByClassName("nav-links")[0];
const homePage = document.getElementById("p1");
const benefitsPage = document.getElementById("p2");
const servicesPage = document.getElementById("p3");
const contactPage = document.getElementById("p4");

window.addEventListener("resize", resizeHandler);

toggleButton.addEventListener("click", () => {
  if (screen.width <= 400) {
    navbarLinks.style.display = "flex";
  }
});

homePage.addEventListener("click", () => {
  if (screen.width <= 400) {
    navbarLinks.style.display = "none";
  }
});

benefitsPage.addEventListener("click", () => {
  if (screen.width <= 400) {
    navbarLinks.style.display = "none";
  }
});

servicesPage.addEventListener("click", () => {
  if (screen.width <= 400) {
    navbarLinks.style.display = "none";
  }
});

contactPage.addEventListener("click", () => {
  if (screen.width <= 400) {
    navbarLinks.style.display = "none";
  }
});

function resizeHandler() {
  location.reload();
}

