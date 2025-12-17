(function() {
  const container = document.querySelector('.lectures-scroll-container');
  if (!container) return;
  const area = container.querySelector('.lectures-scroll-area');
  const prevBtn = container.querySelector('.lectures-scroll-prev');
  const nextBtn = container.querySelector('.lectures-scroll-next');
  const scrollAmount = 300;

  prevBtn.addEventListener('click', () => {
    area.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
  });
  nextBtn.addEventListener('click', () => {
    area.scrollBy({ left: scrollAmount, behavior: 'smooth' });
  });
})();
