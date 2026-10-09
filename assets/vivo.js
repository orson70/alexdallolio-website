// Il sito che respira: logo che si disegna come un filo, testi che si posano entrando, showreel con suono.
(function () {
  var d = document, root = d.documentElement;
  d.querySelectorAll('.brand svg path, .sr-angolo path').forEach(function (p) { p.setAttribute('pathLength', '1'); });
  root.classList.add('vivo');
  if (root.dataset.luce) {
    var st=d.createElement('div'); st.className='L-stanza'; d.body.prepend(st);
    var ns='http://www.w3.org/2000/svg', sv=d.createElementNS(ns,'svg'); sv.setAttribute('class','L-binari'); sv.setAttribute('viewBox','0 0 1000 1000'); sv.setAttribute('preserveAspectRatio','none'); sv.setAttribute('aria-hidden','true');
    [[150,440],[380,480],[620,520],[850,560]].forEach(function(x){var l=d.createElementNS(ns,'line');l.setAttribute('x1',x[0]);l.setAttribute('y1',0);l.setAttribute('x2',x[1]);l.setAttribute('y2',520);sv.appendChild(l);});
    d.body.prepend(sv);
    if (matchMedia('(pointer:fine)').matches) { var lp=d.createElement('div'); lp.className='L-lampada'; d.body.appendChild(lp);
      addEventListener('pointermove',function(e){lp.style.left=e.clientX+'px';lp.style.top=e.clientY+'px';},{passive:true}); }
  }

  function spezza(el){
    var i=0;
    (function walk(node){
      [].slice.call(node.childNodes).forEach(function(ch){
        if(ch.nodeType===3){
          var f=d.createDocumentFragment();
          ch.textContent.split(/(\s+)/).forEach(function(t){
            if(!t) return;
            if(/^\s+$/.test(t)){f.appendChild(d.createTextNode(t));return;}
            var w=d.createElement('span');w.className='w';
            t.split('').forEach(function(l){var c=d.createElement('span');c.className='c';var n=i++;c.style.setProperty('--i',n);c.style.setProperty('--d',((n*0.035)+((n*37)%11)*0.05).toFixed(2)+'s');c.style.setProperty('--x',(n*0.11).toFixed(2)+'s');c.textContent=l;w.appendChild(c);});
            f.appendChild(w);
          });
          node.replaceChild(f,ch);
        } else if(ch.nodeType===1 && ch.tagName!=='BR') walk(ch);
      });
    })(el);
    el.setAttribute('aria-label', el.textContent); el.classList.add('sp');
  }
  var titoli = d.querySelectorAll('.open .h1, main section h2, section.cta2 h2, .who h2, .ig-head h2, .page-hero h1');
  titoli.forEach(spezza);

  var cose = d.querySelectorAll('.sp, .prose p, .sr');
  if (!('IntersectionObserver' in window)) { cose.forEach(function (e) { e.classList.add('qui'); }); return; }
  var io = new IntersectionObserver(function (voci) {
    voci.forEach(function (v) { if (v.isIntersecting) { v.target.classList.add('qui'); io.unobserve(v.target); } });
  }, { threshold: 0.18 });
  cose.forEach(function (e) { if (!e.classList.contains('sr') && !e.classList.contains('sp')) e.classList.add('appare'); io.observe(e); });

  d.querySelectorAll('.sr-box').forEach(function (box) {
    var v = box.querySelector('video');
    box.addEventListener('click', function () {
      if (box.classList.contains('va')) return;
      box.classList.add('va'); v.muted = false; v.controls = true; v.play();
    });
    v.addEventListener('ended', function () { box.classList.remove('va'); v.controls = false; v.load(); });
  });
})();
