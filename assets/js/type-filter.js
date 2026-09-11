// Chip filter for listing pages. Filters every element carrying data-type and
// hides list year headings whose rows are all filtered out.
(function () {
  function init() {
    var buttons = document.querySelectorAll('.archive-filter-btn');
    if (!buttons.length) return;
    var items = document.querySelectorAll('[data-type]');
    var years = document.querySelectorAll('.archive-list-year');

    function apply(filter) {
      items.forEach(function (el) {
        el.hidden = filter !== 'all' && el.getAttribute('data-type') !== filter;
      });
      years.forEach(function (yr) {
        var n = yr.nextElementSibling, any = false;
        while (n && n.tagName === 'DD') {
          if (!n.hidden) any = true;
          n = n.nextElementSibling;
        }
        yr.hidden = !any;
      });
    }

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        buttons.forEach(function (b) {
          var on = b === btn;
          b.classList.toggle('active', on);
          b.setAttribute('aria-pressed', on ? 'true' : 'false');
        });
        apply(btn.getAttribute('data-filter'));
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
