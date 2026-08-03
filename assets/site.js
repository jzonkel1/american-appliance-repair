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
