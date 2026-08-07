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
      qw.querySelector('input[name=' + g.dataset.field + ']').value = b.textContent.trim();
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