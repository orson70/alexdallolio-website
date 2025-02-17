document.addEventListener("DOMContentLoaded", function() {
  // Testi in italiano e inglese
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
      bookACall: "Prenota una chiamata"
    },
    en: {
      name: "Alex Dallolio",
      tagline1: "Film Creative Director | AI Artist | Visual Alchemist",
      tagline2: "Creative and innovative in the world of visual communication.",
      tagline3: "He has collaborated with brands such as Nike, Prada, Tetrapak, Luisa Spagnoli, Lavazza, and many more.",
      email: "Email",
      vimeo: "Vimeo",
      instagram: "Instagram",
      portfolio: "Portfolio",
      bookACall: "Book a Call"
    }
  };

  // Mappiamo gli elementi HTML che vogliamo tradurre
  const elements = {
    name: document.getElementById("name"),
    tagline1: document.getElementById("tagline1"),
    tagline2: document.getElementById("tagline2"),
    tagline3: document.getElementById("tagline3"),
    email: document.getElementById("email"),
    vimeo: document.getElementById("vimeo"),
    instagram: document.getElementById("instagram"),
    portfolio: document.getElementById("portfolio"),
    bookACall: document.getElementById("bookACall")
  };

  // Lingua di default
  let currentLang = "it";
  setLanguage(currentLang);

  // Aggiungiamo i listener ai link di selezione lingua
  const langLinks = document.querySelectorAll(".lang-link");
  langLinks.forEach(link => {
    link.addEventListener("click", e => {
      e.preventDefault();
      const lang = e.target.getAttribute("data-lang");
      setLanguage(lang);
    });
  });

  // Funzione per settare i testi in base alla lingua
  function setLanguage(lang) {
    currentLang = lang;
    elements.name.textContent = translations[lang].name;
    elements.tagline1.textContent = translations[lang].tagline1;
    elements.tagline2.textContent = translations[lang].tagline2;
    elements.tagline3.textContent = translations[lang].tagline3;
    elements.email.textContent = translations[lang].email;
    elements.vimeo.textContent = translations[lang].vimeo;
    elements.instagram.textContent = translations[lang].instagram;
    elements.portfolio.textContent = translations[lang].portfolio;
    elements.bookACall.textContent = translations[lang].bookACall;
  }
});