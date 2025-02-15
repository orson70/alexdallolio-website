document.addEventListener("DOMContentLoaded", function () {
    const defaultLang = document.documentElement.getAttribute("data-default-lang") || "it";
    const userLang = localStorage.getItem("selectedLang") || navigator.language.substring(0, 2) || defaultLang;
    setLanguage(userLang);

    document.querySelectorAll(".language-switcher a").forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            const selectedLang = this.getAttribute("data-lang");
            setLanguage(selectedLang);
            localStorage.setItem("selectedLang", selectedLang);
        });
    });

    function setLanguage(lang) {
        document.querySelectorAll("[data-lang-text]").forEach(element => {
            element.style.display = element.getAttribute("data-lang-text") === lang ? "block" : "none";
        });
    }
});