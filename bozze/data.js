// Dati condivisi dalle tre bozze (solo contenuti già presenti sul sito)
window.WORKS = [
  { id: "N7Ta9EZstzA", t: "Showreel 2026", c: "Concept e regia", y: "2026", cat: "AI" },
  { id: "ySthwmhR-y4", t: "GERD", c: "Webuild · Documentario", y: "", cat: "Corporate" },
  { id: "pbGWFFmW1Fc", t: "WeSearch", c: "Webuild", y: "2025", cat: "Corporate" },
  { id: "r0N34NuRFZc", t: "Wake Up!", c: "AI & Concept", y: "", cat: "AI" },
  { id: "zJ28dM8DRYo", t: "FILA F-Box", c: "Salone del Mobile", y: "2023", cat: "AI" },
  { id: "fA3pBdKnWbo", t: "Prada Canali", c: "Fashion", y: "", cat: "Fashion" },
  { id: "UYnvGmCuroQ", t: "Builderhero", c: "Webuild", y: "", cat: "Corporate" },
  { id: "xv2S2flaYJQ", t: "Chopard", c: "Fashion spot", y: "", cat: "Fashion" },
  { id: "z-GjfCZasFo", t: "Progetto Italia", c: "Salini Impregilo", y: "", cat: "Corporate" },
  { id: "B4Rv_BOayx8", t: "Atomic Dream Dance", c: "Dell Ala · AI", y: "", cat: "AI" },
  { id: "YVLem2cHfoc", t: "Hands", c: "Canali · Director's cut", y: "", cat: "Fashion" },
  { id: "588LDT1c3zs", t: "Custodiamo il domani", c: "Tetra Pak", y: "", cat: "Corporate" },
];
window.BRANDS = ["Prada","Nike","BMW","Volkswagen","Bugatti","Ray-Ban","Timberland","Converse","Diadora","Fila","Colmar","Canali","John Richmond","Jacob Cohen","Luisa Spagnoli","Polaroid","Lavazza","Tetra Pak","Allianz","Novartis","Sisal","TIM","Webuild","Rai","Mediaset","Sky","Fox"];
window.thumb = (id, q = "maxresdefault") => `https://i.ytimg.com/vi/${id}/${q}.jpg`;

// Lightbox YouTube comune
window.openFilm = (id, title) => {
  let lb = document.getElementById("lb");
  if (!lb) {
    lb = document.createElement("div");
    lb.id = "lb";
    lb.innerHTML = '<button aria-label="Chiudi">×</button><div class="lb-frame"></div>';
    Object.assign(lb.style, { position: "fixed", inset: 0, zIndex: 999, background: "rgba(0,0,0,.92)", display: "flex", alignItems: "center", justifyContent: "center", padding: "4vw" });
    const b = lb.querySelector("button");
    Object.assign(b.style, { position: "absolute", top: "14px", right: "20px", background: "none", border: 0, color: "#fff", fontSize: "40px", cursor: "pointer", lineHeight: 1 });
    const close = () => { lb.style.display = "none"; lb.querySelector(".lb-frame").innerHTML = ""; };
    b.onclick = close;
    lb.onclick = e => { if (e.target === lb) close(); };
    addEventListener("keydown", e => { if (e.key === "Escape") close(); });
    document.body.appendChild(lb);
  }
  lb.style.display = "flex";
  lb.querySelector(".lb-frame").innerHTML =
    `<iframe src="https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0" title="${title}" allow="autoplay; fullscreen" allowfullscreen style="width:min(1200px,92vw);aspect-ratio:16/9;border:0;display:block"></iframe>`;
};
