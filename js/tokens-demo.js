/* ==========================================================================
   Tokens Demo — js/tokens-demo.js
   --------------------------------------------------------------------------
   Demo interativo de motion para a galeria de tokens (seção #tokens).
   Anima um quadrado nas 4 curvas do kit em sequência:
   ease-out → ease-in → ease-in-out → spring.

   Regras:
   - Respeita prefers-reduced-motion: colapsa para estático.
   - Usa IntersectionObserver para só rodar quando visível.
   ========================================================================== */

"use strict";

document.addEventListener("DOMContentLoaded", () => {
  initMotionDemo();
});

/* --------------------------------------------------------------------------
   Motion demo
   -------------------------------------------------------------------------- */
function initMotionDemo() {
  const playBtn = document.getElementById("motion-play");
  const box = document.getElementById("motion-box");
  const label = document.getElementById("motion-label");
  const reduced = document.getElementById("motion-reduced");
  const demo = document.getElementById("motion-demo");
  if (!playBtn || !box || !label || !demo) return;

  const STAGE_WIDTH = () => box.parentElement.clientWidth - 48 - 16; /* box width + left padding */

  const CURVES = [
    { name: "ease-out", easing: "var(--motion-easing-out)", token: "--motion-easing-out" },
    { name: "ease-in", easing: "var(--motion-easing-in)", token: "--motion-easing-in" },
    { name: "ease-in-out", easing: "var(--motion-easing-in-out)", token: "--motion-easing-in-out" },
    { name: "spring", easing: "var(--motion-easing-spring)", token: "--motion-easing-spring" },
  ];

  let running = false;
  let prefersReduced = false;
  let observer = null;

  const mq = window.matchMedia("(prefers-reduced-motion: reduce)");

  const applyReduced = (matches) => {
    prefersReduced = matches;
    playBtn.disabled = matches;
    playBtn.setAttribute("aria-disabled", String(matches));
    box.style.transition = "none";
    box.style.left = "var(--space-2)";
    if (reduced) {
      reduced.hidden = !matches;
    }
    if (matches) {
      running = false;
      label.textContent = "Desativado";
    } else {
      label.textContent = "Pronto";
    }
  };

  applyReduced(mq.matches);
  mq.addEventListener("change", (event) => applyReduced(event.matches));

  const animPhase = (phaseIndex) => {
    if (prefersReduced || !running) return;
    if (phaseIndex >= CURVES.length) {
      running = false;
      label.textContent = "Pronto";
      playBtn.disabled = false;
      playBtn.setAttribute("aria-disabled", "false");
      return;
    }

    const curve = CURVES[phaseIndex];
    const finalLeft = `${Math.max(8, STAGE_WIDTH())}px`;

    label.textContent = `${curve.name}: ${curve.token}`;

    /* Reset para o início (anima para a direita) */
    box.style.transition = "none";
    box.style.left = "var(--space-2)";

    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        box.style.transition = `left var(--motion-duration-slow) ${curve.easing}`;
        box.style.left = finalLeft;
      });
    });

    /* Após a animação terminar, volta ao início e passa para a próxima fase */
    const duration = 320; /* motion-duration-slow */
    setTimeout(() => {
      box.style.transition = `left var(--motion-duration-fast) var(--motion-easing-out)`;
      box.style.left = "var(--space-2)";
      setTimeout(() => {
        animPhase(phaseIndex + 1);
      }, 130);
    }, duration + 60);
  };

  const play = () => {
    if (prefersReduced || running) return;
    running = true;
    playBtn.disabled = true;
    playBtn.setAttribute("aria-disabled", "true");
    animPhase(0);
  };

  playBtn.addEventListener("click", play);

  /* IntersectionObserver: só roda quando visível, pausa quando não */
  observer = new IntersectionObserver(
    (entries) => {
      if (entries[0].isIntersecting) return;
      /* Saiu da viewport: cancela animação pendente */
      if (running) {
        running = false;
        box.style.transition = "none";
        box.style.left = "var(--space-2)";
        label.textContent = "Pronto";
        playBtn.disabled = false;
        playBtn.setAttribute("aria-disabled", "false");
      }
    },
    { threshold: 0.1 }
  );

  observer.observe(demo);
}