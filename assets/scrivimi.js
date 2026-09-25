// "Scrivimi" sul sito: invece di aprire il programma di posta del visitatore,
// apre una finestrella e manda il messaggio col postino (Cloudflare + Brevo).
(() => {
  const POSTINO = 'https://stanza-postino.postino.workers.dev';
  const it = (document.documentElement.lang || 'it').startsWith('it');
  const T = it ? {
    h: 'Scrivimi.', p: 'Un progetto, del materiale da trasformare, una domanda. Arriva a me e ti rispondo io.',
    msg: 'Il tuo messaggio', mail: 'La tua email', name: 'Nome (facoltativo)', send: 'Manda', sending: 'Invio…',
    ok: 'Arrivato. Ti ho mandato una copia: ti rispondo io.', err: 'Non è partito. Riprova, oppure scrivimi a', close: 'Chiudi', back: '← Indietro',
    privacy: 'Uso la tua email solo per risponderti.',
  } : {
    h: 'Write to me.', p: 'A project, material to transform, a question. It comes straight to me, and I reply personally.',
    msg: 'Your message', mail: 'Your email', name: 'Name (optional)', send: 'Send', sending: 'Sending…',
    ok: 'Received. I sent you a copy: I will get back to you.', err: 'It did not go through. Try again, or write to', close: 'Close', back: '← Back',
    privacy: 'I only use your email to reply to you.',
  };
  const css = `
  .sv-p{position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,.9);backdrop-filter:blur(6px);display:none;align-items:center;justify-content:center;padding:16px;overflow-y:auto}
  .sv-p.sv-on{display:flex}
  .sv-b button:focus-visible,.sv-b input:focus-visible,.sv-b textarea:focus-visible{outline:2px solid #D5B893;outline-offset:3px}
  .sv-b{width:min(560px,100%);background:#1B2632;border:1px solid rgba(236,235,231,.18);padding:30px 28px;position:relative;margin:auto;color:#ecebe7;font-family:"Montserrat",Helvetica,Arial,sans-serif}
  .sv-b h2{font-weight:300;letter-spacing:-.01em;font-size:clamp(30px,3.6vw,44px);line-height:1;margin:0 0 12px;color:#ecebe7}
  .sv-b p{color:#bdb9b2;font-size:15px;line-height:1.6;margin:0 0 12px}
  .sv-b label{display:block;font:11px "Montserrat",sans-serif;letter-spacing:.07em;text-transform:uppercase;color:#8a867f;margin:14px 0 6px}
  .sv-b input,.sv-b textarea{width:100%;box-sizing:border-box;background:#000;border:1px solid rgba(236,235,231,.22);color:#ecebe7;font:16px/1.5 "Montserrat",Helvetica,sans-serif;padding:10px 12px;border-radius:0}
  .sv-b textarea{min-height:120px}
  .sv-b .sv-s{all:unset;cursor:pointer;display:inline-block;margin-top:18px;background:#D5B893;color:#000;font:12px "Montserrat",sans-serif;letter-spacing:.08em;text-transform:uppercase;padding:12px 18px}
  .sv-b .sv-s[disabled]{opacity:.4}
  .sv-b .sv-x{all:unset;cursor:pointer;position:absolute;top:10px;right:14px;font-size:30px;line-height:1;color:#8a867f}
  .sv-b .sv-bk{all:unset;cursor:pointer;font:11px "Montserrat",sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#8a867f;margin-bottom:12px;display:inline-block}
  .sv-b .sv-m{margin-top:14px;font-weight:500}
  .sv-b .sv-m a{color:#D5B893}
  .sv-b small{display:block;color:#8a867f;font-size:12px;margin-top:10px}
  .sv-hp{position:absolute;left:-9999px}`;
  const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  const p = document.createElement('div'); p.className = 'sv-p'; p.setAttribute('role', 'dialog'); p.setAttribute('aria-modal', 'true'); p.setAttribute('aria-labelledby', 'sv-h');
  p.innerHTML = `<form class="sv-b"><button type="button" class="sv-x" aria-label="${T.close}">×</button><button type="button" class="sv-bk">${T.back}</button>
    <h2 id="sv-h">${T.h}</h2><p>${T.p}</p>
    <label for="sv-t">${T.msg}</label><textarea id="sv-t" name="pensiero" required minlength="3" maxlength="2000"></textarea>
    <label for="sv-e">${T.mail}</label><input id="sv-e" type="email" name="email" required autocomplete="email">
    <label for="sv-n">${T.name}</label><input id="sv-n" type="text" name="nome" autocomplete="name">
    <input class="sv-hp" type="text" name="_honey" tabindex="-1" autocomplete="off">
    <small>${T.privacy}</small>
    <button type="submit" class="sv-s">${T.send}</button><div class="sv-m" aria-live="polite"></div></form>`;
  document.body.appendChild(p);
  const f = p.querySelector('form'), msg = p.querySelector('.sv-m'), btn = p.querySelector('.sv-s');
  let opener = null;
  const close = () => { if (!p.classList.contains('sv-on')) return; p.classList.remove('sv-on'); opener?.focus(); };
  p.querySelector('.sv-x').onclick = close; p.querySelector('.sv-bk').onclick = close;
  p.addEventListener('click', e => { if (e.target === p) close(); });
  addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href^="mailto:alexdallolio@alexdallolio.com"]');
    if (!a || a.hasAttribute('data-direct')) return;
    e.preventDefault(); opener = a; p.classList.add('sv-on'); setTimeout(() => p.querySelector('textarea').focus(), 50);
  });
  f.addEventListener('submit', async e => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(f).entries());
    if (data._honey) return;
    data.kind = 'note'; data.lang = it ? 'it' : 'en'; data.pensiero = `[${location.pathname}]\n${data.pensiero}`;
    btn.disabled = true; msg.textContent = T.sending;
    try {
      const r = await fetch(POSTINO, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data), signal: AbortSignal.timeout ? AbortSignal.timeout(15000) : undefined });
      const j = await r.json().catch(() => ({}));
      if (!r.ok || !j.ok) throw new Error(j.error || r.status);
      msg.textContent = T.ok; f.querySelectorAll('input,textarea').forEach(i => i.disabled = true);
    } catch (err) {
      btn.disabled = false;
      msg.innerHTML = `${T.err} <a href="mailto:alexdallolio@alexdallolio.com" data-direct>alexdallolio@alexdallolio.com</a>`;
    }
  });
})();
