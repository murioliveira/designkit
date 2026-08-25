/* ==========================================================================
   App — js/app.js
   --------------------------------------------------------------------------
   Interações do showcase (fase 2 + fase 4B):

     - Toggle de tema claro/escuro com persistência (localStorage)
     - Menu mobile (hambúrguer + backdrop + Esc + redimensionar)
     - Scrollspy da sidebar (IntersectionObserver)
     - Demonstrações dos componentes A (loading, fechar alerta)
     - Demonstrações dos formulários (senha, validação, toggles)

   Convenções:
   - JavaScript puro (ES6+), sem dependências.
   - Inicializações dentro de listeners de DOMContentLoaded.
   - Nomes descritivos; cada recurso com bloco de comentário próprio.
   ========================================================================== */

"use strict";

document.addEventListener("DOMContentLoaded", () => {
  initThemeToggle();
  initMenuToggle();
  initScrollSpy();
  initDemoLoading();
  initDemoAlerts();
  initPasswordToggles();
  initFormValidation();
  initIndeterminate();
  initToggleSwitches();
  initTooltips();
  initModals();
  initTabs();
  initDropdowns();
  initPaginationDemo();
});

/* --------------------------------------------------------------------------
   Tema claro/escuro
   - Estado inicial já vem do bootstrap inline no <head> (sem flash).
   - Aqui: alternância, persistência em localStorage e atributos acessíveis.
   -------------------------------------------------------------------------- */

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
      /* file:// pode bloquear o localStorage — o tema vale para a sessão */
    }
  });
}

/* --------------------------------------------------------------------------
   Menu mobile (off-canvas)
   - Abre/fecha com o hambúrguer; fecha ao clicar num link, no backdrop,
     com Esc, ou ao redimensionar para desktop (>= lg).
   - Estado refletido em aria-expanded e aria-label.
   -------------------------------------------------------------------------- */

function initMenuToggle() {
  const trigger = document.querySelector(".menu-toggle");
  const sidebar = document.getElementById("sidebar");
  const backdrop = document.querySelector(".layout__backdrop");
  if (!trigger || !sidebar) return;

  const mqDesktop = window.matchMedia("(min-width: 1024px)");

  const setMenu = (open) => {
    sidebar.classList.toggle("is-open", open);
    trigger.setAttribute("aria-expanded", String(open));
    trigger.setAttribute("aria-label", open ? "Fechar menu de navegação" : "Abrir menu de navegação");
    if (backdrop) backdrop.classList.toggle("is-visible", open);
    document.body.classList.toggle("no-scroll", open && !mqDesktop.matches);
  };

  trigger.addEventListener("click", () => {
    setMenu(!sidebar.classList.contains("is-open"));
  });

  // Fecha ao escolher uma seção (mobile)
  sidebar.addEventListener("click", (event) => {
    if (event.target.closest("a")) setMenu(false);
  });

  if (backdrop) {
    backdrop.addEventListener("click", () => setMenu(false));
  }

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && sidebar.classList.contains("is-open")) {
      setMenu(false);
      trigger.focus();
    }
  });

  // Ao voltar para o desktop, garante o estado fechado
  mqDesktop.addEventListener("change", (event) => {
    if (event.matches) setMenu(false);
  });
}

/* --------------------------------------------------------------------------
   Demonstrações dos componentes A (fase 3)
   - Loading simulado: botão com [data-demo-loading] entra em estado de
     carregamento por 2.2s (spinner + aria-busy + label alterada).
   - Fechar alerta: o .alert__close anima (.alert--closing) e remove o
     alerta do DOM. Apenas para o showcase; produção faria o mesmo via
     callback de remoção.
   -------------------------------------------------------------------------- */

function initDemoLoading() {
  const trigger = document.querySelector("[data-demo-loading]");
  if (!trigger) return;

  const label = trigger.querySelector(".btn__label");
  const originalLabel = label ? label.textContent : "";

  trigger.addEventListener("click", () => {
    if (trigger.disabled) return;

    trigger.disabled = true;
    trigger.classList.add("btn--loading");
    trigger.setAttribute("aria-busy", "true");
    if (label) label.textContent = "Salvando…";

    window.setTimeout(() => {
      trigger.disabled = false;
      trigger.classList.remove("btn--loading");
      trigger.removeAttribute("aria-busy");
      if (label) label.textContent = originalLabel;
    }, 2200);
  });
}

function initDemoAlerts() {
  const closers = [...document.querySelectorAll(".alert__close")];
  if (!closers.length) return;

  closers.forEach((closer) => {
    closer.addEventListener("click", () => {
      const alert = closer.closest(".alert");
      if (!alert) return;

      // Anima o fechamento e remove após a transição (fast = 120ms)
      alert.classList.add("alert--closing");
      window.setTimeout(() => alert.remove(), 130);
    });
  });
}

/* --------------------------------------------------------------------------
   Demonstrações dos formulários (fase 4B)
   - Toggle de visibilidade de senha: botão [data-password-toggle] alterna
     o type do input e reflete em aria-pressed/aria-label.
   - Validação no submit: campos [data-validate] com regras por name;
     erro em .field__error (role="alert") + aria-invalid no controle.
   - Checkbox indeterminate: [data-indeterminate] para demonstração.
   - Toggle switch: input checkbox ganha role="switch" e sincroniza
     aria-checked (o clique nativo continua funcionando).
   -------------------------------------------------------------------------- */

function initPasswordToggles() {
  const actions = [...document.querySelectorAll("[data-password-toggle]")];
  actions.forEach((btn) => {
    const input = document.getElementById(btn.getAttribute("aria-controls"));
    if (!input) return;

    btn.addEventListener("click", () => {
      const show = input.type === "password";
      input.type = show ? "text" : "password";
      btn.setAttribute("aria-pressed", String(show));
      btn.setAttribute("aria-label", show ? "Ocultar senha" : "Mostrar senha");
      // Devolve o foco ao campo após alternar
      input.focus();
    });
  });
}

function initFormValidation() {
  const form = document.getElementById("demo-signup");
  if (!form) return;

  const status = document.getElementById("form-status");
  const fields = [...form.querySelectorAll("[data-validate]")];

  // Regras simples de demonstração, por name do campo
  const rules = {
    nome: (value) =>
      value.trim().length >= 2 ? "" : "Informe seu nome completo (mínimo de 2 caracteres).",
    email: (value) =>
      /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value.trim()) ? "" : "Informe um e-mail válido.",
    senha: (value) =>
      value.length >= 8 ? "" : "A senha precisa de pelo menos 8 caracteres.",
  };

  const setError = (input, message) => {
    const field = input.closest(".field");
    input.setAttribute("aria-invalid", "true");
    if (field) field.classList.add("field--error");
    const errorEl = field ? field.querySelector(".field__error") : null;
    if (errorEl) errorEl.textContent = message;
  };

  const clearError = (input) => {
    const field = input.closest(".field");
    input.removeAttribute("aria-invalid");
    if (field) field.classList.remove("field--error");
  };

  // O erro some enquanto o usuário corrige
  fields.forEach((input) => {
    input.addEventListener("input", () => clearError(input));
  });

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (status) status.hidden = true;

    let firstInvalid = null;

    fields.forEach((input) => {
      const rule = rules[input.name];
      const message = rule ? rule(input.value) : "";
      if (message) {
        setError(input, message);
        if (!firstInvalid) firstInvalid = input;
      } else {
        clearError(input);
      }
    });

    // Termos obrigatórios (checkbox customizado fora do [data-validate])
    const terms = form.querySelector("#f-termos");
    if (terms) {
      if (!terms.checked) {
        setError(terms, "Você precisa aceitar os termos para continuar.");
        if (!firstInvalid) firstInvalid = terms;
      } else {
        clearError(terms);
      }
    }

    if (firstInvalid) {
      firstInvalid.focus();
      return;
    }

    if (status) status.hidden = false;
  });
}

function initIndeterminate() {
  const checkboxes = [...document.querySelectorAll("[data-indeterminate]")];
  checkboxes.forEach((el) => {
    el.indeterminate = true;
    // Estado acessível: ARIA não deriva o mixed do estado nativo do checkbox
    el.setAttribute("aria-checked", "mixed");
  });
}

function initToggleSwitches() {
  const switches = [...document.querySelectorAll('.toggle input[type="checkbox"]')];
  switches.forEach((input) => {
    input.setAttribute("role", "switch");
    const sync = () => input.setAttribute("aria-checked", String(input.checked));
    sync();
    input.addEventListener("change", sync);
  });
}

/* --------------------------------------------------------------------------
   Scrollspy da sidebar
   - Observa as seções do <main>; a seção "atual" é a que intersecta a faixa
     logo abaixo do header (IntersectionObserver com rootMargin).
   - A escolha entre seções simultaneamente visíveis usa o topo mais baixo
     (a que o usuário acabou de alcançar ao rolar).
   - Fallback: a última seção é ativada ao chegar ao fim da página.
   -------------------------------------------------------------------------- */

function initScrollSpy() {
  const links = [...document.querySelectorAll('.sidebar__link[href^="#"]')];
  if (!links.length) return;

  const linkById = new Map(
    links.map((link) => [link.getAttribute("href").slice(1), link]),
  );

  const sections = [...document.querySelectorAll("main section[id]")].filter(
    (section) => linkById.has(section.id),
  );
  if (!sections.length) return;

  const header = document.querySelector(".site-header");
  const bandTop = header ? header.offsetHeight : 64;
  const lastSection = sections[sections.length - 1];

  const setActive = (id) => {
    links.forEach((link) => {
      if (link.getAttribute("href") === `#${id}`) {
        link.setAttribute("aria-current", "true");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  };

  const observer = new IntersectionObserver(
    (entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting);
      if (!visible.length) return;

      // Entre as seções na faixa, a "atual" é a de topo mais baixo
      // (a mais recente alcançada ao rolar para baixo).
      let current = visible[0];
      for (const entry of visible) {
        if (entry.target.getBoundingClientRect().top > current.target.getBoundingClientRect().top) {
          current = entry;
        }
      }
      setActive(current.target.id);
    },
    { rootMargin: `-${bandTop}px 0px -55% 0px`, threshold: 0 },
  );

  sections.forEach((section) => observer.observe(section));

  // Última seção curta pode nunca cruzar a faixa: ativa ao chegar ao fim.
  window.addEventListener(
    "scroll",
    () => {
      const atBottom = window.innerHeight + window.scrollY >= document.body.scrollHeight - 4;
      if (atBottom) setActive(lastSection.id);
    },
    { passive: true },
  );
}

/* --------------------------------------------------------------------------
   Tooltips (fase 4C)
   - Gatilhos: [data-tooltip] com texto; posição via [data-tooltip-pos]
     (top | bottom | left | right; padrão top).
   - Cria um .tooltip no <body> sob demanda, posiciona com coordenadas
     fixas sobre o gatilho, liga aria-describedby no gatilho e remove ao
     sair. Mostra em hover (mouse) e foco (teclado).
   -------------------------------------------------------------------------- */

function initTooltips() {
  const triggers = [...document.querySelectorAll("[data-tooltip]")];
  if (!triggers.length) return;

  let tooltip = null;
  let active = null;

  // Folga entre o gatilho e a dica (constante do componente)
  const GAP = 8;

  const position = () => {
    if (!tooltip || !active) return;

    const pos = active.getAttribute("data-tooltip-pos") || "top";
    const rect = active.getBoundingClientRect();
    const tipRect = tooltip.getBoundingClientRect();

    let left = rect.left + rect.width / 2 - tipRect.width / 2;
    let top = rect.top - tipRect.height - GAP;

    if (pos === "bottom") {
      top = rect.bottom + GAP;
    } else if (pos === "left") {
      left = rect.left - tipRect.width - GAP;
      top = rect.top + rect.height / 2 - tipRect.height / 2;
    } else if (pos === "right") {
      left = rect.right + GAP;
      top = rect.top + rect.height / 2 - tipRect.height / 2;
    }

    // Mantém dentro da viewport (clamp simples)
    left = Math.max(GAP, Math.min(left, window.innerWidth - tipRect.width - GAP));
    top = Math.max(GAP, Math.min(top, window.innerHeight - tipRect.height - GAP));

    tooltip.style.left = `${left}px`;
    tooltip.style.top = `${top}px`;
    tooltip.setAttribute("data-pos", pos);
  };

  const show = (trigger) => {
    if (tooltip) tooltip.remove();

    tooltip = document.createElement("span");
    tooltip.className = "tooltip";
    tooltip.setAttribute("role", "tooltip");
    tooltip.id = `dk-tooltip-${triggers.indexOf(trigger)}`;
    tooltip.textContent = trigger.getAttribute("data-tooltip") || "";
    document.body.appendChild(tooltip);

    active = trigger;
    trigger.setAttribute("aria-describedby", tooltip.id);

    // Posiciona no próximo frame (layout já calculado) e revela
    requestAnimationFrame(() => {
      position();
      tooltip.classList.add("is-visible");
    });
  };

  const hide = (trigger) => {
    if (active !== trigger) return;
    if (tooltip) tooltip.remove();
    tooltip = null;
    active = null;
    trigger.removeAttribute("aria-describedby");
  };

  triggers.forEach((trigger) => {
    trigger.addEventListener("mouseenter", () => show(trigger));
    trigger.addEventListener("mouseleave", () => hide(trigger));
    trigger.addEventListener("focus", () => show(trigger));
    trigger.addEventListener("blur", () => hide(trigger));
  });

  // Reposiciona ao rolar/redimensionar enquanto a dica estiver visível
  window.addEventListener("scroll", position, { passive: true });
  window.addEventListener("resize", position);
}

/* --------------------------------------------------------------------------
   Modais (fase 4C)
   - Abertura: [data-modal-open="#id"]; fechamento: [data-modal-close]
     (botão, botão X ou backdrop), tecla Esc, ou devolução de foco ao
     gatilho ao fechar.
   - Acessibilidade: aria-modal + role=dialog no HTML, foco no primeiro
     foco-ficável ao abrir, trap de foco (Tab/Shift+Tab) e body.no-scroll
     enquanto aberto.
   -------------------------------------------------------------------------- */

function initModals() {
  const FOCUSABLE =
    'a[href], button:not([disabled]), input:not([disabled]), ' +
    'select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])';

  const getFocusables = (root) =>
    [...root.querySelectorAll(FOCUSABLE)].filter(
      (el) => el.offsetParent !== null || el === document.activeElement,
    );

  const closeModal = (modal) => {
    if (modal.hidden) return;

    modal.hidden = true;
    document.body.classList.remove("no-scroll");
    document.removeEventListener("keydown", modal._dkKeydown);

    // Devolve o foco ao gatilho que abriu o diálogo
    if (modal._dkTrigger) modal._dkTrigger.focus();
    modal._dkTrigger = null;
    modal._dkKeydown = null;
  };

  const openModal = (modal, trigger) => {
    modal.hidden = false;
    document.body.classList.add("no-scroll");
    modal._dkTrigger = trigger;

    const dialog = modal.querySelector(".modal__dialog");
    const focusables = getFocusables(dialog || modal);

    // Foco no primeiro controle do diálogo (ou no próprio diálogo)
    (focusables[0] || dialog || modal).focus();

    const onKeydown = (event) => {
      if (event.key === "Escape") {
        event.preventDefault();
        closeModal(modal);
        return;
      }

      // Trap de foco: cicla entre primeiro e último elemento
      if (event.key !== "Tab" || !focusables.length) return;
      const first = focusables[0];
      const last = focusables[focusables.length - 1];

      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    };

    modal._dkKeydown = onKeydown;
    document.addEventListener("keydown", onKeydown);
  };

  // Gatilhos de abertura
  [...document.querySelectorAll("[data-modal-open]")].forEach((trigger) => {
    trigger.addEventListener("click", () => {
      const selector = trigger.getAttribute("data-modal-open");
      const modal = document.querySelector(selector);
      if (modal) openModal(modal, trigger);
    });
  });

  // Fechamento: botões [data-modal-close] (inclui o X e o backdrop)
  [...document.querySelectorAll("[data-modal-close]")].forEach((closer) => {
    closer.addEventListener("click", () => {
      const modal = closer.closest(".modal");
      if (modal) closeModal(modal);
    });
  });
}

/* --------------------------------------------------------------------------
   Tabs (fase 4C)
   - Estrutura WAI-ARIA: [role=tablist] > [role=tab] + painéis
     [role=tabpanel] identificados por aria-controls.
   - Clique ativa; setas ←/→ (e ↑/↓) movem e ativam; Home/End vão ao
     primeiro/último. Roving tabindex: ativa = 0, demais = -1.
   - Ativação automática ao focar (padrão comum para abas de conteúdo).
   -------------------------------------------------------------------------- */

function initTabs() {
  const tablists = [...document.querySelectorAll('[role="tablist"]')];
  if (!tablists.length) return;

  tablists.forEach((tablist) => {
    const tabs = [...tablist.querySelectorAll('[role="tab"]')];
    if (!tabs.length) return;

    const activate = (tab) => {
      tabs.forEach((t) => {
        const selected = t === tab;
        t.setAttribute("aria-selected", String(selected));
        t.tabIndex = selected ? 0 : -1;

        const panel = document.getElementById(t.getAttribute("aria-controls"));
        if (panel) panel.hidden = !selected;
      });
    };

    tablist.addEventListener("click", (event) => {
      const tab = event.target.closest('[role="tab"]');
      if (tab && tabs.includes(tab)) {
        activate(tab);
        tab.focus();
      }
    });

    tablist.addEventListener("keydown", (event) => {
      const current = tabs.indexOf(document.activeElement);
      if (current === -1) return;

      let next = -1;
      switch (event.key) {
        case "ArrowRight":
        case "ArrowDown":
          next = (current + 1) % tabs.length;
          break;
        case "ArrowLeft":
        case "ArrowUp":
          next = (current - 1 + tabs.length) % tabs.length;
          break;
        case "Home":
          next = 0;
          break;
        case "End":
          next = tabs.length - 1;
          break;
        default:
          return;
      }

      event.preventDefault();
      activate(tabs[next]);
      tabs[next].focus();
    });
  });
}

/* --------------------------------------------------------------------------
   Dropdowns / menus (ciclo de expansão)
   - Gatilhos: [data-dropdown] com aria-haspopup/aria-expanded/aria-controls
     apontando para .dropdown__menu (role="menu", oculto via [hidden]).
   - Abre no clique e nas teclas Enter/Espaço/↑/↓ (foca o 1º/último item);
     fecha com Esc (devolve o foco ao gatilho), clique fora, escolha de
     item ou Tab.
   - Navegação dentro do menu: ↑/↓ circular, Home/End.
   - Select-like ([data-select-like] no menu): o item escolhido move
     aria-current (check visível via CSS) e o valor vai para
     .dropdown__value do gatilho.
   -------------------------------------------------------------------------- */

function initDropdowns() {
  const triggers = [...document.querySelectorAll("[data-dropdown]")];
  if (!triggers.length) return;

  const menuOf = (trigger) =>
    document.getElementById(trigger.getAttribute("aria-controls"));

  const itemsOf = (menu) =>
    [...menu.querySelectorAll('[role="menuitem"]')].filter(
      (item) => !item.disabled,
    );

  const closeAll = (except) => {
    triggers.forEach((trigger) => {
      if (trigger === except) return;
      const menu = menuOf(trigger);
      if (menu) menu.hidden = true;
      trigger.setAttribute("aria-expanded", "false");
    });
  };

  const open = (trigger) => {
    const menu = menuOf(trigger);
    if (!menu) return;
    closeAll(trigger);
    menu.hidden = false;
    trigger.setAttribute("aria-expanded", "true");

    // Roving tabindex: apenas o primeiro item entra na ordem de Tab
    const items = itemsOf(menu);
    items.forEach((item, index) => {
      item.tabIndex = index === 0 ? 0 : -1;
    });
  };

  const toggle = (trigger) => {
    const menu = menuOf(trigger);
    if (menu && !menu.hidden) {
      menu.hidden = true;
      trigger.setAttribute("aria-expanded", "false");
    } else {
      open(trigger);
    }
  };

  const moveFocus = (menu, from, delta) => {
    const items = itemsOf(menu);
    if (!items.length) return;
    const index = items.indexOf(from);
    const next = (index + delta + items.length) % items.length;
    items[next].focus();
  };

  triggers.forEach((trigger) => {
    // Clique: alterna o menu
    trigger.addEventListener("click", () => toggle(trigger));

    // Teclado no gatilho: Enter/Espaço abrem; ↑/↓ abrem e focam item
    trigger.addEventListener("keydown", (event) => {
      const menu = menuOf(trigger);
      if (!menu) return;

      if (event.key === "Enter" || event.key === " ") {
        if (menu.hidden) {
          event.preventDefault();
          open(trigger);
          itemsOf(menu)[0]?.focus();
        } else {
          event.preventDefault();
          closeAll();
        }
        return;
      }

      if (event.key === "ArrowDown" || event.key === "ArrowUp") {
        event.preventDefault();
        if (menu.hidden) {
          open(trigger);
          const items = itemsOf(menu);
          (event.key === "ArrowDown" ? items[0] : items[items.length - 1])?.focus();
        } else {
          // Menu aberto com foco no gatilho: ↓ primeiro item, ↑ último item.
          // O gatilho não está em itemsOf(menu) — indexOf === -1 faria moveFocus
          // modular girar para o lado errado (último na ↓, penúltimo na ↑).
          const items = itemsOf(menu);
          if (!items.length) return;
          (event.key === "ArrowDown" ? items[0] : items[items.length - 1])?.focus();
        }
        return;
      }

      if (event.key === "Escape" && !menu.hidden) {
        event.preventDefault();
        closeAll();
        trigger.focus();
      }
    });
  });

  // Navegação por teclado DENTRO do menu (delegação no documento)
  document.addEventListener("keydown", (event) => {
    const item = event.target.closest('[role="menuitem"]');
    if (!item) return;
    const menu = item.closest(".dropdown__menu");
    if (!menu || menu.hidden) return;

    if (event.key === "ArrowDown" || event.key === "ArrowUp") {
      event.preventDefault();
      moveFocus(menu, item, event.key === "ArrowDown" ? 1 : -1);
      return;
    }
    if (event.key === "Home") {
      event.preventDefault();
      itemsOf(menu)[0]?.focus();
      return;
    }
    if (event.key === "End") {
      event.preventDefault();
      const items = itemsOf(menu);
      items[items.length - 1]?.focus();
      return;
    }
    if (event.key === "Escape") {
      event.preventDefault();
      const trigger = [...triggers].find((t) => menuOf(t) === menu);
      closeAll();
      if (trigger) trigger.focus();
      return;
    }
    if (event.key === "Tab") {
      // Sai do menu com Tab: fecha e segue a ordem natural do documento
      closeAll();
    }
  });

  // Clique fora de qualquer dropdown fecha todos
  document.addEventListener("click", (event) => {
    if (!event.target.closest(".dropdown")) closeAll();
  });

  // Escolha de item: fecha; select-like move a seleção
  document.addEventListener("click", (event) => {
    const item = event.target.closest('[role="menuitem"]');
    if (!item) return;
    const menu = item.closest(".dropdown__menu");
    if (!menu) return;

    const trigger = [...triggers].find((t) => menuOf(t) === menu);

    if (menu.hasAttribute("data-select-like")) {
      itemsOf(menu).forEach((other) => {
        other.removeAttribute("aria-current");
        other.tabIndex = -1;
      });
      item.setAttribute("aria-current", "true");
      item.tabIndex = 0;
      const value = trigger?.querySelector(".dropdown__value");
      if (value) value.textContent = item.textContent.trim();
    }

    closeAll();
    if (trigger) trigger.focus();
  });
}

function initPaginationDemo() {
  // Demo do showcase apenas: clicar numa página atualiza aria-current e o
  // status "Página X de Y". Em produção, os links apontam para URLs reais
  // e o estado atual é servido pelo backend (sem JS).
  const lists = [...document.querySelectorAll("[data-pagination-demo]")];
  if (!lists.length) return;

  lists.forEach((list) => {
    const status = list.parentElement?.querySelector(".pagination__status");
    const total = list.getAttribute("data-total") || "";

    list.addEventListener("click", (event) => {
      const link = event.target.closest(".pagination__link[data-page]");
      if (!link || link.hasAttribute("aria-disabled")) return;
      event.preventDefault();

      const page = link.getAttribute("data-page");
      list.querySelectorAll(".pagination__link[data-page]").forEach((item) => {
        item.removeAttribute("aria-current");
      });
      link.setAttribute("aria-current", "page");

      if (status) {
        status.textContent = total
          ? `Página ${page} de ${total}`
          : `Página ${page}`;
      }
    });
  });
}
