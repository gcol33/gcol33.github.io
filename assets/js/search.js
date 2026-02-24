// Search functionality using Lunr.js
(function() {
  var searchIndex = null;
  var searchData = null;
  var searchModal = null;
  var searchInput = null;
  var searchResults = null;

  // Initialize search when DOM is ready
  document.addEventListener('DOMContentLoaded', function() {
    searchModal = document.getElementById('searchModal');
    searchInput = document.getElementById('searchInput');
    searchResults = document.getElementById('searchResults');

    if (!searchModal || !searchInput || !searchResults) return;

    // Load search data
    fetch('/search.json')
      .then(function(response) { return response.json(); })
      .then(function(data) {
        searchData = data;
        buildIndex();
      })
      .catch(function(err) {
        console.error('Failed to load search index:', err);
      });

    // Search input handler
    searchInput.addEventListener('input', debounce(performSearch, 200));

    // Keyboard shortcut (Ctrl/Cmd + K)
    document.addEventListener('keydown', function(e) {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        openSearch();
      }
      if (e.key === 'Escape' && searchModal.classList.contains('show')) {
        closeSearch();
      }
    });

    // Close on backdrop click
    searchModal.addEventListener('click', function(e) {
      if (e.target === searchModal) {
        closeSearch();
      }
    });
  });

  function buildIndex() {
    searchIndex = lunr(function() {
      this.ref('url');
      this.field('title', { boost: 10 });
      this.field('category', { boost: 5 });
      this.field('content');

      var self = this;
      searchData.forEach(function(item) {
        self.add(item);
      });
    });
  }

  function performSearch() {
    var query = searchInput.value.trim();

    if (query.length < 2) {
      searchResults.innerHTML = '<p class="search-hint">Type at least 2 characters to search...</p>';
      return;
    }

    if (!searchIndex) {
      searchResults.innerHTML = '<p class="search-loading">Loading search index...</p>';
      return;
    }

    try {
      var results = searchIndex.search(query + '*');
      displayResults(results, query);
    } catch (e) {
      // Fallback for invalid queries
      var results = searchIndex.search(query);
      displayResults(results, query);
    }
  }

  function displayResults(results, query) {
    if (results.length === 0) {
      searchResults.innerHTML = '<p class="search-no-results">No results found for "' + escapeHtml(query) + '"</p>';
      return;
    }

    var html = '<ul class="search-results-list">';
    results.slice(0, 10).forEach(function(result) {
      var item = searchData.find(function(d) { return d.url === result.ref; });
      if (item) {
        html += '<li class="search-result-item">';
        html += '<a href="' + item.url + '" class="search-result-link">';
        html += '<span class="search-result-title">' + escapeHtml(item.title) + '</span>';
        if (item.category) {
          html += '<span class="search-result-category">' + escapeHtml(item.category) + '</span>';
        }
        if (item.content) {
          html += '<span class="search-result-excerpt">' + escapeHtml(item.content.substring(0, 120)) + '...</span>';
        }
        html += '</a>';
        html += '</li>';
      }
    });
    html += '</ul>';

    if (results.length > 10) {
      html += '<p class="search-more">Showing 10 of ' + results.length + ' results</p>';
    }

    searchResults.innerHTML = html;
  }

  function openSearch() {
    searchModal.classList.add('show');
    searchModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    setTimeout(function() {
      searchInput.focus();
    }, 100);
  }

  function closeSearch() {
    searchModal.classList.remove('show');
    searchModal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    searchInput.value = '';
    searchResults.innerHTML = '<p class="search-hint">Type to search publications, projects, courses...</p>';
  }

  function debounce(func, wait) {
    var timeout;
    return function() {
      var context = this, args = arguments;
      clearTimeout(timeout);
      timeout = setTimeout(function() {
        func.apply(context, args);
      }, wait);
    };
  }

  function escapeHtml(text) {
    var div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Expose functions globally
  window.openSearch = openSearch;
  window.closeSearch = closeSearch;
})();
