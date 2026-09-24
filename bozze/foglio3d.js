// Foglio 3D: carta morbida in WebGL (Three.js). La scrittura è dipinta sulla carta,
// quindi si curva con lei. API: window.PAPER = { setText, kick, fold, unfold }.
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js';

const holder = document.getElementById('sheet');           // il foglio DOM resta come "sagoma" invisibile
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
let renderer;
try {
  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' });
} catch (e) { renderer = null; }
if (!renderer || !renderer.getContext()) throw new Error('niente WebGL: resta il foglio classico');

const S = 2;                                               // risoluzione della texture (x2)
const gl = renderer.domElement;
gl.id = 'paper3d';
Object.assign(gl.style, { position: 'fixed', inset: 0, width: '100%', height: '100%', pointerEvents: 'none', zIndex: 1 });
document.querySelector('.stage').before(gl);
document.body.classList.add('gl');
renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 2));

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(35, 1, 1, 8000);

// ── texture: carta (in cache) + scrittura (ridisegnata quando cambia)
const tex = document.createElement('canvas'), tg = tex.getContext('2d');
const bg = document.createElement('canvas'), bgg = bg.getContext('2d');
const texture = new THREE.CanvasTexture(tex);
texture.colorSpace = THREE.SRGBColorSpace; texture.anisotropy = 8;
let PW = 560, PH = 440;

let seed = 7;
const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
function paintPaper() {
  bg.width = tex.width = PW * S; bg.height = tex.height = PH * S;
  const g = bgg; g.setTransform(S, 0, 0, S, 0, 0); seed = 7;
  g.fillStyle = '#efe6d6'; g.fillRect(0, 0, PW, PH);
  let gr = g.createRadialGradient(PW * .3, PH * .2, 10, PW * .3, PH * .2, PW * .9);
  gr.addColorStop(0, 'rgba(255,253,246,.7)'); gr.addColorStop(1, 'rgba(255,253,246,0)'); g.fillStyle = gr; g.fillRect(0, 0, PW, PH);
  gr = g.createRadialGradient(PW * .85, PH * .95, 10, PW * .85, PH * .95, PW * .7);
  gr.addColorStop(0, 'rgba(150,115,60,.16)'); gr.addColorStop(1, 'rgba(150,115,60,0)'); g.fillStyle = gr; g.fillRect(0, 0, PW, PH);
  const im = g.getImageData(0, 0, PW * S, PH * S);               // grana
  for (let i = 0; i < im.data.length; i += 4) { const n = (Math.random() - .5) * 18; im.data[i] += n; im.data[i + 1] += n; im.data[i + 2] += n * .9; }
  g.putImageData(im, 0, 0);
  for (let i = 0; i < 90; i++) {                                 // fibre
    const x = rnd() * PW, y = rnd() * PH, l = 6 + rnd() * 18, a = rnd() * Math.PI;
    g.strokeStyle = `rgba(120,100,70,${(.05 + rnd() * .08).toFixed(3)})`; g.lineWidth = .5;
    g.beginPath(); g.moveTo(x, y); g.quadraticCurveTo(x + Math.cos(a) * l * .5 + rnd() * 3, y + Math.sin(a) * l * .5 + rnd() * 3, x + Math.cos(a) * l, y + Math.sin(a) * l); g.stroke();
  }
  for (let y = 34 + 44; y < PH - 24; y += 44) {                  // righe a china
    g.lineWidth = .9; let skip = 0;
    for (let x = 6; x < PW - 6; x += 16) {
      if (skip-- > 0) continue;
      if (rnd() < .03) { skip = 1 + Math.floor(rnd() * 2); continue; }
      g.strokeStyle = `rgba(70,92,160,${(.18 + rnd() * .12).toFixed(3)})`;
      g.beginPath(); g.moveTo(x, y + (rnd() - .5) * 1.1); g.lineTo(Math.min(x + 17, PW - 6), y + (rnd() - .5) * 1.1); g.stroke();
    }
  }
  [28, 32].forEach((mx0, k) => {                                  // margine rosso
    g.strokeStyle = `rgba(196,62,58,${k ? .28 : .42})`; g.lineWidth = k ? .7 : 1;
    g.beginPath(); for (let y = 0; y <= PH; y += 14) { const x = mx0 + (rnd() - .5) * 1.2; y ? g.lineTo(x, y) : g.moveTo(x, y); } g.stroke();
  });
  const d = new Date(), dd = `${String(d.getDate()).padStart(2, '0')} · ${String(d.getMonth() + 1).padStart(2, '0')} · ${d.getFullYear()}`;
  g.save(); g.translate(PW - 28, 30); g.rotate(-.035); g.font = '500 20px Caveat, cursive'; g.textAlign = 'right';
  g.fillStyle = 'rgba(80,78,74,.55)'; g.fillText(dd, 0, 0); g.restore();
}

// scrittura: ogni lettera ha la sua piccola inclinazione e il suo istante di nascita (inchiostro che scorre)
let chars = [], caretOn = true, dirty = true;
const jit = i => { let x = Math.sin(i * 12.9898) * 43758.5453; return x - Math.floor(x); };
function setText(t) {
  const now = performance.now();
  const next = [...t];
  if (next.length < chars.length || next.slice(0, chars.length).join('') !== chars.map(c => c.c).join('')) {
    chars = next.map((c, i) => ({ c, born: now - 1000, i }));    // cancellazione: niente animazione
  } else {
    for (let i = chars.length; i < next.length; i++) chars.push({ c: next[i], born: now + (i - chars.length) * 25, i });
  }
  dirty = true;
}
function paintText(now) {
  tg.setTransform(1, 0, 0, 1, 0, 0);
  tg.drawImage(bg, 0, 0);
  tg.setTransform(S, 0, 0, S, 0, 0);
  let size = 34;
  const left = 44, right = PW - 30, top = 34 + 44 - 10, lh = 44, maxLines = Math.floor((PH - 60 - top) / lh) + 1;
  const layout = sz => {                                          // a capo per parole
    tg.font = `500 ${sz}px Caveat, cursive`;
    const pos = []; let x = left, line = 0; const text = chars.map(c => c.c).join('');
    const words = text.split(/(\s+)/); let k = 0;
    for (const w of words) {
      if (w === '\n' || w.includes('\n')) { for (const ch of w) { pos[k++] = null; if (ch === '\n') { line++; x = left; } } continue; }
      const ww = tg.measureText(w).width;
      if (!/^\s+$/.test(w) && x + ww > right && x > left) { line++; x = left; }
      for (const ch of w) { const cw = tg.measureText(ch).width; pos[k++] = [x, top + line * lh * (sz / 34)]; x += cw; }
    }
    return { pos, lines: line + 1, end: [x, top + line * lh * (sz / 34)] };
  };
  let L = layout(size);
  while (L.lines > maxLines && size > 18) { size -= 2; L = layout(size); }
  tg.textBaseline = 'alphabetic';
  chars.forEach((ch, i) => {
    const p = L.pos[i]; if (!p || /\s/.test(ch.c)) return;
    const age = now - ch.born; if (age < 0) return;
    const k = Math.min(1, age / 220);
    const w = tg.measureText(ch.c).width;
    tg.save(); tg.translate(p[0], p[1] + (jit(i) - .5) * 2); tg.rotate((jit(i + 7) - .5) * .05);
    tg.beginPath(); tg.rect(-2, -size, (w + 4) * k, size * 1.5); tg.clip();
    tg.fillStyle = `rgba(29,35,68,${(.82 + jit(i + 3) * .18).toFixed(2)})`;
    tg.shadowColor = 'rgba(29,35,68,.35)'; tg.shadowBlur = 1.2;
    tg.fillText(ch.c, 0, 0); tg.restore();
    if (k < 1) dirty = true;
  });
  if (caretOn && !folding) { tg.fillStyle = 'rgba(29,35,68,.8)'; tg.fillRect(L.end[0] + 2, L.end[1] - size * .78, 2, size * .9); }
  texture.needsUpdate = true;
}
setInterval(() => { caretOn = !caretOn; dirty = true; }, 530);

// ── la carta: piano suddiviso, deformato nello shader (curva, onda, angolo sollevato, piega a metà)
const uniforms = {
  map: { value: texture }, uTime: { value: 0 }, uKick: { value: 0 }, uFold: { value: 0 }, uFade: { value: 1 },
  uW: { value: PW }, uH: { value: PH }, uMouse: { value: new THREE.Vector2() },
};
const material = new THREE.ShaderMaterial({
  uniforms, transparent: true, side: THREE.DoubleSide,
  vertexShader: `
    uniform float uTime, uKick, uFold, uW, uH; uniform vec2 uMouse;
    varying vec2 vUv; varying vec3 vN; varying float vZ;
    vec3 disp(vec2 p) {
      float nx = p.x / (uW * .5), ny = p.y / (uH * .5);
      float z = nx * nx * 14.0;                                        // lieve curva a cilindro
      z += sin(nx * 2.6 + uTime * 1.1) * 7.0 + sin(ny * 2.0 - uTime * .8) * 4.5 + sin((nx + ny) * 4.0 + uTime * 1.7) * 2.0;
      z += uKick * sin(nx * 7.0 - uTime * 14.0) * 12.0 * (.55 + .45 * nx);   // onda al tasto
      float c = smoothstep(.62, 1.0, (nx - ny) * .5 + .5); z += c * c * 46.0; // angolo in basso a destra che si solleva
      float d = distance(vec2(nx, ny), uMouse); z += exp(-d * d * 3.0) * 10.0;  // il mouse "soffia" sulla carta
      return vec3(p, z);
    }
    vec3 fold(vec3 P) {                                                  // piega a metà sul lato verticale centrale
      if (P.x <= 0.0) return P;
      float a = uFold * 3.05;
      return vec3(P.x * cos(a) - P.z * sin(a), P.y, P.x * sin(a) + P.z * cos(a));
    }
    void main() {
      vUv = uv;
      vec3 P = disp(position.xy);
      vec3 dx = disp(position.xy + vec2(1.5, 0.0)) - P, dy = disp(position.xy + vec2(0.0, 1.5)) - P;
      vec3 N = normalize(cross(dx, dy));
      P = fold(P);
      if (position.x > 0.0) { float a = uFold * 3.05; N = vec3(N.x * cos(a) - N.z * sin(a), N.y, N.x * sin(a) + N.z * cos(a)); }
      vN = normalize(normalMatrix * N); vZ = P.z;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(P, 1.0);
    }`,
  fragmentShader: `
    uniform sampler2D map; uniform float uFade;
    varying vec2 vUv; varying vec3 vN; varying float vZ;
    void main() {
      vec3 L = normalize(vec3(-.35, .55, 1.0));
      vec3 N = gl_FrontFacing ? vN : -vN;
      float dif = clamp(dot(N, L), 0.0, 1.0);
      vec3 H = normalize(L + vec3(0.0, 0.0, 1.0));
      float spec = pow(clamp(dot(N, H), 0.0, 1.0), 40.0) * .12;
      vec3 base = gl_FrontFacing ? texture2D(map, vUv).rgb : vec3(.90, .86, .79);
      vec3 col = base * (.52 + .58 * dif) + spec;
      gl_FragColor = vec4(col, uFade);
    }`,
});
let mesh;
function build() {
  PW = holder.offsetWidth; PH = holder.offsetHeight;
  uniforms.uW.value = PW; uniforms.uH.value = PH;
  if (mesh) { mesh.geometry.dispose(); scene.remove(mesh); }
  mesh = new THREE.Mesh(new THREE.PlaneGeometry(PW, PH, 90, 70), material);
  scene.add(mesh);
  paintPaper(); dirty = true;
}
function fit() {
  const W = innerWidth, H = innerHeight;
  renderer.setSize(W, H, false);
  camera.aspect = W / H; camera.position.z = (H / 2) / Math.tan(THREE.MathUtils.degToRad(35 / 2)); camera.updateProjectionMatrix();
  if (!mesh || holder.offsetWidth !== PW || holder.offsetHeight !== PH) build();
}

// ── movimento: mouse, respiro, onda, piega e volo
let mx = 0, my = 0, kick = 0, folding = 0, foldT = 0, flyT = 0;
addEventListener('pointermove', e => {
  mx = e.clientX / innerWidth - .5; my = e.clientY / innerHeight - .5;
  const r = holder.getBoundingClientRect();
  uniforms.uMouse.value.set(((e.clientX - r.left) / r.width - .5) * 2, -((e.clientY - r.top) / r.height - .5) * 2);
});
const t0 = performance.now();
function loop(now) {
  const t = (now - t0) / 1000;
  const r = holder.getBoundingClientRect();
  uniforms.uTime.value = reduce ? 0 : t;
  kick *= .94; uniforms.uKick.value = kick;
  foldT += ((folding ? 1 : 0) - foldT) * .06; uniforms.uFold.value = foldT;
  flyT += ((folding ? 1 : 0) - flyT) * (folding ? .025 : .12);
  const fly = Math.max(0, flyT - .35) / .65;
  uniforms.uFade.value = 1 - fly;
  mesh.position.set(r.left + r.width / 2 - innerWidth / 2, -(r.top + r.height / 2 - innerHeight / 2) + (reduce ? 0 : Math.sin(t * 1.1) * 6) + fly * 260, fly * 180);
  mesh.rotation.set(my * .32 + (reduce ? 0 : Math.sin(t * .9) * .03) - fly * .6, mx * .42 + (reduce ? 0 : Math.cos(t * .7) * .04), -.02 + fly * .3);
  if (dirty) { dirty = false; paintText(performance.now()); }
  renderer.render(scene, camera);
  requestAnimationFrame(loop);
}
(document.fonts ? document.fonts.load('500 34px Caveat') : Promise.resolve()).finally(() => {
  fit(); addEventListener('resize', fit); new ResizeObserver(fit).observe(holder);
  requestAnimationFrame(loop);
});

window.PAPER = {
  setText,
  kick: () => { kick = Math.min(kick + .55, 1.4); },
  fold: () => { folding = 1; },
  unfold: () => { folding = 0; },
};
