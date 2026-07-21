---
layout: default
title: Search
---

# Search

<input type="text" id="search-input" placeholder="Type to search all entities..." style="width:100%;padding:12px;font-size:16px;border:2px solid #3498db;border-radius:6px;margin-bottom:20px;">

<div id="search-filters" style="margin-bottom:20px;">
  <button class="filter-btn active" data-type="all">All</button>
  <button class="filter-btn" data-type="protein">Proteins</button>
  <button class="filter-btn" data-type="reagent">Reagents</button>
  <button class="filter-btn" data-type="method">Methods</button>
  <button class="filter-btn" data-type="concept">Concepts</button>
</div>

<div id="search-results" style="display:grid;gap:8px;"></div>

<p id="search-status" style="color:#7f8c8d;font-size:14px;">Enter at least 2 characters to search.</p>

<script>
const searchIndex = {{ site.data.search_index | jsonify }};
const input = document.getElementById('search-input');
const results = document.getElementById('search-results');
const status = document.getElementById('search-status');
let filterType = 'all';

// Filter buttons
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    filterType = btn.dataset.type;
    doSearch();
  });
});

function doSearch() {
  const q = input.value.trim().toLowerCase();
  if (q.length < 2) {
    results.innerHTML = '';
    status.textContent = 'Enter at least 2 characters to search.';
    return;
  }

  let filtered = searchIndex.filter(e => {
    if (filterType !== 'all' && e.type !== filterType) return false;
    const title = (e.title || '').toLowerCase();
    const tags = (e.tags || []).join(' ').toLowerCase();
    const slug = (e.slug || '').toLowerCase();
    const haystack = title + ' ' + tags + ' ' + slug;
    return haystack.includes(q);
  }).slice(0, 50);

  if (filtered.length === 0) {
    results.innerHTML = '<div style="padding:20px;color:#7f8c8d;">No results found.</div>';
    status.textContent = '0 results.';
    return;
  }

  results.innerHTML = filtered.map(e => {
    const badgeColors = {protein:'#3498db', reagent:'#2ecc71', method:'#e67e22', concept:'#9b59b6'};
    const color = badgeColors[e.type] || '#95a5a6';
    return `<a href="${e.path}" style="display:block;padding:10px 14px;border:1px solid #ecf0f1;border-radius:6px;text-decoration:none;color:#2c3e50;transition:background 0.15s;" onmouseover="this.style.background='#f7f9fa'" onmouseout="this.style.background=''">
      <span style="display:inline-block;padding:2px 8px;border-radius:4px;background:${color};color:white;font-size:12px;font-weight:bold;margin-right:8px;">${e.category_display}</span>
      <strong>${e.title}</strong>
      <span style="color:#95a5a6;font-size:13px;margin-left:8px;">${e.slug}</span>
    </a>`;
  }).join('');

  status.textContent = `${filtered.length} result${filtered.length === 1 ? '' : 's'}.`;
}

input.addEventListener('input', doSearch);
</script>

<style>
.filter-btn {
  padding:6px 14px;
  border:1px solid #bdc3c7;
  border-radius:4px;
  background:white;
  cursor:pointer;
  font-size:13px;
  margin-right:4px;
  margin-bottom:4px;
}
.filter-btn.active {
  background:#3498db;
  color:white;
  border-color:#3498db;
}
.filter-btn:hover {
  background:#ecf0f1;
}
.filter-btn.active:hover {
  background:#2980b9;
}
</style>
