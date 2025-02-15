const translations = {
    it: {
        name: "Alex Dallolio – Regista Creativo | Artista AI | Alchimista Visivo",
        tagline: "Fondendo intuizione umana e intelligenza artificiale per creare narrazioni visive straordinarie.",
        collaborations: "Collaborato con: Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza, WeBuild, Bonaveri, Canali.",
        cta: "Elevare i brand attraverso una narrazione visiva audace.",
        portfolio: "Guarda il Portfolio",
        email: "Email",
        call: "Prenota una Chiamata",
        vimeo: "Vimeo",
        instagram: "Instagram",
        back: "Torna alla Home"
    },
    en: {
        name: "Alex Dallolio – Creative Film Director | AI Artist | Visual Alchemist",
        tagline: "Blending human intuition with machine intelligence to craft compelling visual narratives.",
        collaborations: "Collaborated with: Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza, WeBuild, Bonaveri, Canali.",
        cta: "Elevating brands through bold visual storytelling.",
        portfolio: "View Portfolio",
        email: "Email",
        call: "Book a Call",
        vimeo: "Vimeo",
        instagram: "Instagram",
        back: "Back to Home"
    },
    fr: {
        name: "Alex Dallolio – Réalisateur Créatif | Artiste IA | Alchimiste Visuel",
        tagline: "Mélangeant intuition humaine et intelligence artificielle pour créer des récits visuels captivants.",
        collaborations: "Collaboré avec: Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza, WeBuild, Bonaveri, Canali.",
        cta: "Élever les marques grâce à une narration visuelle audacieuse.",
        portfolio: "Voir le Portfolio",
        email: "Email",
        call: "Réserver un Appel",
        vimeo: "Vimeo",
        instagram: "Instagram",
        back: "Retour à l'accueil"
    },
    de: {
        name: "Alex Dallolio – Kreativer Filmregisseur | KI-Künstler | Visueller Alchemist",
        tagline: "Menschliche Intuition mit künstlicher Intelligenz verbinden, um fesselnde visuelle Geschichten zu erschaffen.",
        collaborations: "Zusammengearbeitet mit: Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza, WeBuild, Bonaveri, Canali.",
        cta: "Marken durch kühne visuelle Erzählungen aufwerten.",
        portfolio: "Portfolio Ansehen",
        email: "Email",
        call: "Ein Gespräch Buchen",
        vimeo: "Vimeo",
        instagram: "Instagram",
        back: "Zurück zur Startseite"
    },
    cn: {
        name: "Alex Dallolio – 创意电影导演 | 人工智能艺术家 | 视觉炼金师",
        tagline: "融合人类直觉与人工智能，创造引人入胜的视觉叙事。",
        collaborations: "合作品牌：Nike、Prada、Tetrapak、Luisa Spagnoli、Lavazza、WeBuild、Bonaveri、Canali。",
        cta: "通过大胆的视觉叙事提升品牌价值。",
        portfolio: "查看作品集",
        email: "电子邮件",
        call: "预约通话",
        vimeo: "Vimeo",
        instagram: "Instagram",
        back: "返回主页"
    }
};

document.querySelectorAll('.language-switcher a').forEach(link => {
    link.addEventListener('click', function (event) {
        event.preventDefault();
        const selectedLang = this.getAttribute('data-lang');
        changeLanguage(selectedLang);
        localStorage.setItem('selectedLang', selectedLang);
    });
});

function changeLanguage(lang) {
    document.querySelectorAll('[data-lang]').forEach(element => {
        const key = element.getAttribute('data-lang');
        if (translations[lang] && translations[lang][key]) {
            element.textContent = translations[lang][key];
        }
    });
}

window.onload = function () {
    const savedLang = localStorage.getItem('selectedLang') || 'it';
    changeLanguage(savedLang);
};

// Effetto scurimento video al movimento del mouse
const videoContainer = document.querySelector(".video-container");

document.addEventListener("mousemove", () => {
    videoContainer.classList.add("dark");
    clearTimeout(window.scurimentoTimeout);
    
    window.scurimentoTimeout = setTimeout(() => {
        videoContainer.classList.remove("dark");
    }, 2000); // Dopo 2 secondi torna chiaro
});