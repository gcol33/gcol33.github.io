document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll("table.collapsible-table").forEach(function(table) {
    let headerRow = table.tHead ? table.tHead.rows[0] : table.rows[0];
    if (!headerRow) return;
    headerRow.style.cursor = "pointer";

    const headerCells = Array.from(headerRow.cells);
    let bodyRows = [];
    if (table.tBodies.length) {
      bodyRows = table.tHead 
        ? Array.from(table.tBodies[0].rows) 
        : Array.from(table.tBodies[0].rows).slice(1);
    } else {
      bodyRows = Array.from(table.rows).slice(1);
    }

    headerRow.addEventListener("click", function() {
      table.classList.toggle('collapsed');

      const isCollapsed = table.classList.contains('collapsed');
      if (isCollapsed) {
        let cachedWidths = headerCells.map(cell => window.getComputedStyle(cell).width);
        headerCells.forEach((cell, i) => cell.style.width = cachedWidths[i]);

        const colgroup = document.createElement("colgroup");
        cachedWidths.forEach(width => {
          const col = document.createElement("col");
          col.style.width = width;
          colgroup.appendChild(col);
        });
        table.insertBefore(colgroup, table.firstElementChild);
        table._colgroup = colgroup;

        bodyRows.forEach(row => row.classList.add("collapsedRow"));
      } else {
        headerCells.forEach(cell => cell.style.width = "");
        if (table._colgroup) {
          table.removeChild(table._colgroup);
          delete table._colgroup;
        }
        bodyRows.forEach(row => row.classList.remove("collapsedRow"));
      }
    });
  });
});
