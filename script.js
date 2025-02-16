document.addEventListener("DOMContentLoaded", function () {
    // Gestione cambio lingua
    const languageSwitcher = document.querySelectorAll(".language-switcher a");
    const textElements = document.querySelectorAll("[data-lang-text]");
    
    languageSwitcher.forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault();
            const selectedLang = this.getAttribute("data-lang");

            // Salva la lingua selezionata nel localStorage
            localStorage.setItem("selectedLanguage", selectedLang);

            // Cambia il testo
            textElements.forEach(el => {
                el.innerText = el.getAttribute(`data-text-${selectedLang}`) || el.innerText;
            });
        });
    });

    // Mantiene la lingua selezionata anche dopo il refresh
    const savedLang = localStorage.getItem("selectedLanguage") || "it";
    textElements.forEach(el => {
        el.innerText = el.getAttribute(`data-text-${savedLang}`) || el.innerText;
    });

    // Effetto scurimento dello sfondo con movimento del mouse
    const videoContainer = document.querySelector(".video-container");
    if (videoContainer) {
        document.addEventListener("mousemove", (e) => {
            let opacity = Math.min(0.6, e.clientY / window.innerHeight);
            videoContainer.style.backgroundColor = `rgba(0, 0, 0, ${opacity})`;
        });
    }

    // Mobile - Assicura che il testo rimanga visibile e ben distribuito
    function adjustMobileLayout() {
        if (window.innerWidth < 768) {
            document.querySelector(".content").style.textAlign = "center";
        } else {
            document.querySelector(".content").style.textAlign = "left";
        }
    }

    adjustMobileLayout();
    window.addEventListener("resize", adjustMobileLayout);
});