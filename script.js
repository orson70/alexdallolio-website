document.addEventListener("DOMContentLoaded", function () {
    const languageLinks = document.querySelectorAll(".language-switcher a");
    const textElements = document.querySelectorAll(".content p, .links a");
    
    const translations = {
        "it": {
            "tagline": "Alex Dallolio – Film Creative Director | AI Artist | Visual Alchemist",
            "description": "Creativo e innovatore nel mondo della comunicazione visiva.",
            "cta": "Specializzato in campagne pubblicitarie, storytelling visivo e narrazione artistica.",
            "collaborations": "Ha collaborato con brand come: Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza e molti altri."
        },
        "en": {
            "tagline": "Alex Dallolio – Film Creative Director | AI Artist | Visual Alchemist",
            "description": "Creative and innovator in the world of visual communication.",
            "cta": "Specialized in advertising campaigns, visual storytelling, and artistic narration.",
            "collaborations": "Collaborated with brands like Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza, and many others."
        }
        // Altre lingue possono essere aggiunte qui
    };

    languageLinks.forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault();
            const selectedLang = this.getAttribute("data-lang");
            
            if (translations[selectedLang]) {
                textElements[0].textContent = translations[selectedLang]["tagline"];
                textElements[1].textContent = translations[selectedLang]["description"];
                textElements[2].textContent = translations[selectedLang]["cta"];
                textElements[3].textContent = translations[selectedLang]["collaborations"];
            }
        });
    });
});
