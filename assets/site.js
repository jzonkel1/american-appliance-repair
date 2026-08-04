// nav: transparent over hero → solid navy on scroll
const nav = document.getElementById('nav');
const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 60);
window.addEventListener('scroll', onScroll, {passive:true}); onScroll();
// reveal on scroll — never leaves content hidden
const rvs = document.querySelectorAll('.rv');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.1,rootMargin:'0px 0px -36px 0px'});
  rvs.forEach(el=>io.observe(el));
  window.addEventListener('load',()=>setTimeout(()=>rvs.forEach(el=>el.classList.add('in')),2500));
} else { rvs.forEach(el=>el.classList.add('in')); }
// duplicate the review track for a seamless marquee
const track = document.getElementById('revTrack');
if (track) {
  const clone = track.cloneNode(true);
  clone.setAttribute('aria-hidden','true');
  track.parentNode.appendChild(clone);
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