document.addEventListener("DOMContentLoaded", function () {
    const languageLinks = document.querySelectorAll(".language-switcher a");
    const contentElements = {
        "name": document.querySelector(".name"),
        "tagline": document.querySelector(".tagline"),
        "description": document.querySelector(".description"),
        "collaborations": document.querySelector(".collaborations"),
        "cta": document.querySelector(".cta"),
        "links": document.querySelectorAll(".links a")
    };

    // Traduzioni per ogni lingua
    const translations = {
        "en": {
            "name": "Alex Dallolio",
            "tagline": "Creative Film Director | AI Artist | Visual Alchemist",
            "description": "Blending human intuition with machine intelligence to craft compelling visual narratives.",
            "collaborations": "Collaborated with: Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza, WeBuild, Bonaveri, Canali.",
            "cta": "Elevating brands through bold visual storytelling.",
            "links": ["View Portfolio", "Email", "Book a Call", "Vimeo", "Instagram"]
        },
        "it": {
            "name": "Alex Dallolio",
            "tagline": "Regista Creativo | Artista AI | Alchimista Visivo",
            "description": "Mescolare intuizione umana e intelligenza artificiale per creare narrazioni visive coinvolgenti.",
            "collaborations": "Ha collaborato con: Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza, WeBuild, Bonaveri, Canali.",
            "cta": "Dare forza ai brand attraverso una narrazione visiva audace.",
            "links": ["Visualizza Portfolio", "Email", "Prenota una Chiamata", "Vimeo", "Instagram"]
        },
        "fr": {
            "name": "Alex Dallolio",
            "tagline": "Réalisateur Créatif | Artiste AI | Alchimiste Visuel",
            "description": "Mélange de l'intuition humaine et de l'intelligence artificielle pour créer des récits visuels captivants.",
            "collaborations": "Collaboration avec: Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza, WeBuild, Bonaveri, Canali.",
            "cta": "Élever les marques grâce à une narration visuelle audacieuse.",
            "links": ["Voir le Portfolio", "Email", "Réserver un Appel", "Vimeo", "Instagram"]
        },
        "de": {
            "name": "Alex Dallolio",
            "tagline": "Kreativer Filmregisseur | KI-Künstler | Visueller Alchemist",
            "description": "Verschmelzung von menschlicher Intuition und künstlicher Intelligenz, um fesselnde visuelle Erzählungen zu erschaffen.",
            "collaborations": "Zusammenarbeit mit: Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza, WeBuild, Bonaveri, Canali.",
            "cta": "Marken durch mutige visuelle Erzählung stärken.",
            "links": ["Portfolio anzeigen", "Email", "Einen Anruf buchen", "Vimeo", "Instagram"]
        },
        "cn": {
            "name": "Alex Dallolio",
            "tagline": "创意电影导演 | AI 艺术家 | 视觉炼金术师",
            "description": "将人类直觉与人工智能结合，打造引人入胜的视觉叙事。",
            "collaborations": "合作品牌：Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza, WeBuild, Bonaveri, Canali。",
            "cta": "通过大胆的视觉叙事提升品牌影响力。",
            "links": ["查看作品集", "电子邮件", "预约通话", "Vimeo", "Instagram"]
        }
    };

    // Funzione per cambiare lingua
    function changeLanguage(lang) {
        if (translations[lang]) {
            contentElements.name.textContent = translations[lang].name;
            contentElements.tagline.textContent = translations[lang].tagline;
            contentElements.description.textContent = translations[lang].description;
            contentElements.collaborations.textContent = translations[lang].collaborations;
            contentElements.cta.textContent = translations[lang].cta;

            contentElements.links.forEach((link, index) => {
                link.textContent = translations[lang].links[index];
            });

            // Salva la lingua scelta nel localStorage
            localStorage.setItem("selectedLanguage", lang);
        }
    }

    // Aggiungi evento di cambio lingua
    languageLinks.forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            const selectedLang = this.getAttribute("data-lang");
            changeLanguage(selectedLang);
        });
    });

    // Controlla se c'è una lingua salvata e la imposta
    const savedLang = localStorage.getItem("selectedLanguage") || "it";
    changeLanguage(savedLang);
});