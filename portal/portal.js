/* ==========================================================================
   Portal — portal/portal.js
   --------------------------------------------------------------------------
   Toggle de tema claro/escuro com persistência (mesmo localStorage do showcase).
   ========================================================================== */

"use strict";

document.addEventListener("DOMContentLoaded", () => {
  initThemeToggle();
});

function initThemeToggle() {
  const toggle = document.querySelector(".theme-toggle");
  if (!toggle) return;

  const apply = (theme) => {
    const dark = theme === "dark";
    document.documentElement.setAttribute("data-theme", theme);
    toggle.setAttribute("aria-pressed", String(dark));
    toggle.setAttribute("aria-label", dark ? "Ativar tema claro" : "Ativar tema escuro");
  };

  apply(document.documentElement.getAttribute("data-theme") || "light");

  toggle.addEventListener("click", () => {
    const current = document.documentElement.getAttribute("data-theme");
    const next = current === "dark" ? "light" : "dark";
    apply(next);
    try {
      localStorage.setItem("dk-theme", next);
    } catch (e) {
      /* file:// pode bloquear o localStorage */
    }
  });
}