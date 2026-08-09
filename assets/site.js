// nav: transparent over hero → solid navy on scroll
const nav = document.getElementById('nav');
const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 60);
window.addEventListener('scroll', onScroll, {passive:true}); onScroll();
// reveal on scroll — never leaves content hidden
const rvs = document.querySelectorAll('.rv');
const revealAll = () => rvs.forEach(el=>el.classList.add('in'));
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.1,rootMargin:'0px 0px -36px 0px'});
  rvs.forEach(el=>io.observe(el));
  window.addEventListener('load',()=>setTimeout(revealAll,2000));
  // safety net: reveal even if window load never fires (slow embeds on mobile)
  setTimeout(revealAll, 4000);
  // iOS back-forward cache restores the page without re-running scripts
  window.addEventListener('pageshow',(e)=>{ if (e.persisted) revealAll(); });
} else { revealAll(); }
// duplicate the review track for a seamless marquee
const track = document.getElementById('revTrack');
if (track) {
  const clone = track.cloneNode(true);
  clone.setAttribute('aria-hidden','true');
  track.parentNode.appendChild(clone);
}

// live open/closed status — Mon–Fri 8–8, Sat 9–4, Sun closed (shop's local time,
// not the visitor's, so a traveler doesn't see the wrong answer)
(() => {
  const slots = document.querySelectorAll('[data-open-now]');
  if (!slots.length) return;
  const HOURS = {1:[8,20],2:[8,20],3:[8,20],4:[8,20],5:[8,20],6:[9,16]}; // 0 = Sunday, closed
  let now;
  try {
    const p = new Intl.DateTimeFormat('en-US', {timeZone:'America/Chicago', weekday:'short', hour:'numeric', minute:'numeric', hour12:false})
      .formatToParts(new Date());
    const get = (t) => p.find(x => x.type === t).value;
    const days = {Sun:0,Mon:1,Tue:2,Wed:3,Thu:4,Fri:5,Sat:6};
    now = {day: days[get('weekday')], h: +get('hour') % 24, m: +get('minute')};
  } catch (e) { return; }               // no reliable clock → say nothing
  const today = HOURS[now.day];
  const mins = now.h * 60 + now.m;
  const open = today && mins >= today[0] * 60 && mins < today[1] * 60;
  const t12 = (h) => (h % 12 || 12) + (h < 12 ? ' AM' : ' PM');
  let next = null;
  for (let i = 1; i <= 7 && !next; i++) {
    const d = HOURS[(now.day + i) % 7];
    if (d) next = (i === 1 ? 'tomorrow' : 'Monday') + ' at ' + t12(d[0]);
  }
  const label = open
    ? 'Open now · until ' + t12(today[1])
    : (today && mins < today[0] * 60 ? 'Opens at ' + t12(today[0]) : 'Closed · opens ' + next);
  const short = open ? 'Open now' : 'Closed';   // the bar is tight on phones
  slots.forEach(el => {
    el.innerHTML = '<span class="on-full"></span><span class="on-short"></span>';
    el.querySelector('.on-full').textContent = label;
    el.querySelector('.on-short').textContent = short;
    el.classList.toggle('is-open', !!open);
    el.hidden = false;
  });
})();

// facebook reel: if the embed never arrives (content blocker, slow network),
// stop spinning and hand the visitor a working link instead
const reel = document.getElementById('reelFrame');
if (reel) {
  setTimeout(() => {
    if (reel.classList.contains('rf-ready')) return;
    const spin = reel.querySelector('.rf-spin');
    const txt = reel.querySelector('.rf-txt');
    if (spin) spin.style.display = 'none';
    if (txt) txt.innerHTML = 'Video won\'t load?<br><a href="https://www.facebook.com/reel/848179184659034/" target="_blank" rel="noopener">Watch it on Facebook</a>';
  }, 12000);
}

// marquees: hold the scroll animation until the logos have real dimensions AND
// the strip is on screen. An undecoded image measures 0 wide, so a track that
// animates to translateX(-100%) sprints through a collapsed width and snaps back.
document.querySelectorAll('.marquee, .rev-marquee').forEach(m => {
  let imgsReady = false, onScreen = false;
  const go = () => { if (imgsReady && onScreen) m.classList.add('mq-go'); };
  const pending = [...m.querySelectorAll('img')].filter(i => !i.complete);
  if (!pending.length) { imgsReady = true; }
  else {
    let left = pending.length;
    const done = () => { if (--left <= 0) { imgsReady = true; go(); } };
    pending.forEach(i => { i.addEventListener('load', done, {once:true}); i.addEventListener('error', done, {once:true}); });
  }
  // never leave a strip frozen because one logo never resolves
  setTimeout(() => { imgsReady = true; go(); }, 3000);
  if ('IntersectionObserver' in window) {
    const mio = new IntersectionObserver((es) => {
      es.forEach(e => { if (e.isIntersecting) { onScreen = true; mio.disconnect(); go(); } });
    }, {threshold:.05});
    mio.observe(m);
  } else { onScreen = true; }
  go();
});

// quote wizard — tap-first multi-step request form
const qw = document.getElementById('qw');
if (qw) {
  const steps = [...qw.querySelectorAll('.qw-step')];
  const bar = document.getElementById('qwBar');
  const back = document.getElementById('qwBack');
  const sum = document.getElementById('qwSum');
  let cur = 0;
  const show = (i) => {
    cur = i;
    steps.forEach((s, j) => s.classList.toggle('on', j === i));
    back.hidden = (i === 0);
    bar.style.width = (((i + 1) / steps.length) * 100) + '%';
    if (sum && i === steps.length - 1) {
      sum.textContent = ['appliance','issue','timing']
        .map(n => qw.querySelector('input[name=' + n + ']').value)
        .filter(Boolean).join('  ·  ');
    }
  };
  qw.querySelectorAll('.qw-opts').forEach(g => {
    g.addEventListener('click', (e) => {
      const b = e.target.closest('button');
      if (!b) return;
      g.querySelectorAll('button').forEach(x => x.classList.remove('sel'));
      b.classList.add('sel');
      const label = b.querySelector('span') || b;
      qw.querySelector('input[name=' + g.dataset.field + ']').value = label.textContent.trim();
      setTimeout(() => show(Math.min(cur + 1, steps.length - 1)), 160);
    });
  });
  back.addEventListener('click', () => show(Math.max(cur - 1, 0)));
  show(0);
}

// mobile menu open/close — locks page scroll behind the menu (iOS-safe)
const burger = document.querySelector('.burger');
const mnav = document.getElementById('mnav');
if (burger && mnav) {
  let lockY = 0;
  const isOpen = () => document.body.classList.contains('menu-open');
  const openMenu = () => {
    lockY = window.scrollY;
    mnav.style.display = 'block';
    document.body.style.top = (-lockY) + 'px';
    document.body.classList.add('menu-open');
  };
  const closeMenu = () => {
    document.body.classList.remove('menu-open');
    document.body.style.top = '';
    mnav.style.display = 'none';
    window.scrollTo(0, lockY);
  };
  burger.addEventListener('click', () => { isOpen() ? closeMenu() : openMenu(); });
  // tapping any link in the menu closes it (matters for same-page anchors)
  mnav.addEventListener('click', (e) => { if (e.target.closest('a')) closeMenu(); });
}

// mobile menu accordions — one group open at a time
document.querySelectorAll('#mnav .mgroup').forEach(btn => {
  btn.addEventListener('click', () => {
    const wasOpen = btn.classList.contains('open');
    document.querySelectorAll('#mnav .mgroup.open').forEach(o => o.classList.remove('open'));
    if (!wasOpen) btn.classList.add('open');
  });
});

// mobile sticky call/book bar — appears after scrolling past the hero
if (window.matchMedia('(max-width:640px)').matches) {
  const bar = document.createElement('div');
  bar.className = 'mcall';
  bar.innerHTML = '<a class="mc-call" href="tel:+13616730937">Call (361) 673-0937</a><button class="mc-book" onclick="if(window.HCPWidget)HCPWidget.openModal()">Book Online</button>';
  document.body.appendChild(bar);
  const tick = () => bar.classList.toggle('on', window.scrollY > window.innerHeight * 0.7);
  window.addEventListener('scroll', tick, {passive:true});
  tick();
}