document.addEventListener("DOMContentLoaded", () => {
  const translations = {
    it: {
      name: "Alex Dallolio",
      tagline1: "Film Creative Director | AI Artist | Visual Alchemist",
      tagline2: "Creativo e innovatore nel mondo della comunicazione visiva.",
      tagline3: "Ha collaborato con brand come Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza e molti altri.",
      email: "Email",
      vimeo: "Vimeo",
      instagram: "Instagram",
      portfolio: "Portfolio",
      prenota: "Prenota una chiamata"
    },
    en: {
      name: "Alex Dallolio",
      tagline1: "Film Creative Director | AI Artist | Visual Alchemist",
      tagline2: "Creative and innovative in the world of visual communication.",
      tagline3: "Has collaborated with brands such as Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza, and many others.",
      email: "Email",
      vimeo: "Vimeo",
      instagram: "Instagram",
      portfolio: "Portfolio",
      prenota: "Book a Call"
    }
  };

  function setLanguage(lang) {
    document.querySelectorAll("[data-key]").forEach(el => {
      const key = el.getAttribute("data-key");
      if (translations[lang] && translations[lang][key]) {
        el.textContent = translations[lang][key];
      }
    });
  }

  // Set default language to Italian
  setLanguage("it");

  // Language switcher event listeners
  const langLinks = document.querySelectorAll(".lang-link");
  langLinks.forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const lang = link.getAttribute("data-lang");
      setLanguage(lang);
      // Aggiorna lo stato active
      langLinks.forEach(l => l.classList.remove("active"));
      link.classList.add("active");
    });
  });
});