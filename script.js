"use strict";
// Progressive enhancement: content and full-size image links work without JS.
(() => {
  const dialog = document.querySelector("#image-dialog");
  const image = document.querySelector("#dialog-image");
  const caption = document.querySelector("#dialog-caption");
  const links = [...document.querySelectorAll("a.capture-button")];
  let trigger = null;
  let suppressHistoryClose = false;
  let restoreAfterHistory = false;
  const revealCapture = new WeakMap();
  document.documentElement.classList.toggle("touch-input", navigator.maxTouchPoints > 0);
  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
  document.querySelectorAll(".capture-gallery").forEach((gallery) => {
    const figures = [...gallery.querySelectorAll(":scope > figure")];
    if (figures.length < 2) return;
    const name = gallery.dataset.gallery;
    let current = 0;
    const controls = document.createElement("div");
    controls.className = "gallery-controls";
    const previous = document.createElement("button");
    const next = document.createElement("button");
    previous.type = next.type = "button";
    previous.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m15 5-7 7 7 7"/></svg>';
    next.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>';
    previous.setAttribute("aria-label", `Previous ${name} image`);
    next.setAttribute("aria-label", `Next ${name} image`);
    const status = document.createElement("span");
    status.className = "gallery-status";
    status.setAttribute("role", "status");
    status.setAttribute("aria-live", "polite");
    status.setAttribute("aria-atomic", "true");
    controls.append(previous, status, next);
    gallery.setAttribute("role", "region");
    gallery.setAttribute("aria-label", `${name} image gallery`);
    function select(index, animate = true) {
      const focused = document.activeElement;
      const controlFocused = controls.contains(focused);
      const imageFocused = figures[current].querySelector(".capture-button") === focused;
      current = (index + figures.length) % figures.length;
      figures.forEach((figure, i) => {
        figure.getAnimations().forEach((animation) => animation.cancel());
        figure.hidden = i !== current;
      });
      const active = figures[current];
      active.querySelector(".capture-frame").append(controls);
      const title = active.querySelector(".capture-heading b").textContent.trim();
      status.textContent = `${current + 1} / ${figures.length}`;
      status.setAttribute("aria-label", `Image ${current + 1} of ${figures.length}: ${title}`);
      if (controlFocused) focused.focus({ preventScroll: true });
      else if (imageFocused) active.querySelector(".capture-button").focus({ preventScroll: true });
      if (animate && !reducedMotion.matches) active.animate([{ opacity: .35 }, { opacity: 1 }], { duration: 150, easing: "ease-out" });
    }
    figures.forEach((figure, index) => {
      const link = figure.querySelector(".capture-button");
      const frame = document.createElement("div");
      frame.className = "capture-frame";
      const original = link.querySelector("img");
      frame.style.setProperty("--capture-ratio", Number(original.getAttribute("width")) / Number(original.getAttribute("height")));
      link.replaceWith(frame);
      frame.append(link);
      // Intrinsic dimensions reserve the correct image shape before decoding.
      figure.querySelector("img").loading = "eager";
      revealCapture.set(figure.querySelector(".capture-button"), () => select(index, false));
    });
    previous.addEventListener("click", () => select(current - 1));
    next.addEventListener("click", () => select(current + 1));
    gallery.addEventListener("keydown", (event) => {
      if (event.altKey || event.ctrlKey || event.metaKey || event.isComposing) return;
      const destination = { ArrowLeft: current - 1, ArrowRight: current + 1, Home: 0, End: figures.length - 1 }[event.key];
      if (destination === undefined) return;
      event.preventDefault();
      const captureFocused = event.target.closest(".capture-button");
      select(destination);
      if (captureFocused) figures[current].querySelector(".capture-button").focus();
    });
    let swipeStart = null;
    let suppressEnlargeUntil = 0;
    gallery.addEventListener("pointerdown", (event) => {
      if (event.pointerType !== "touch" || !event.isPrimary || event.target.closest("button") || !event.target.closest(".capture-frame")) return;
      swipeStart = { id: event.pointerId, x: event.clientX, y: event.clientY };
    });
    gallery.addEventListener("pointercancel", () => { swipeStart = null; });
    gallery.addEventListener("pointerup", (event) => {
      const start = swipeStart;
      swipeStart = null;
      if (!start || start.id !== event.pointerId) return;
      const dx = event.clientX - start.x, dy = event.clientY - start.y;
      if (Math.abs(dx) < 40 || Math.abs(dx) < Math.abs(dy) * 1.5) return;
      suppressEnlargeUntil = performance.now() + 500;
      select(current + (dx < 0 ? 1 : -1));
    });
    gallery.addEventListener("click", (event) => {
      if (event.target.closest(".capture-button") && performance.now() < suppressEnlargeUntil) {
        event.preventDefault();
        event.stopImmediatePropagation();
      }
    }, true);
    select(0, false);
  });
  function restoreFocus() {
    // History traversal restores browser state after popstate; restore focus last.
    requestAnimationFrame(() => { if (trigger && !dialog.open) trigger.focus(); });
  }
  if (!dialog || typeof dialog.showModal !== "function") return;
  function openImage(link) {
    revealCapture.get(link)?.();
    trigger = link;
    image.src = link.href;
    image.alt = link.querySelector("img").alt;
    caption.textContent = link.closest("figure").querySelector("figcaption").innerText.trim();
    if (!dialog.open) dialog.showModal();
  }
  links.forEach((link) => {
    link.addEventListener("click", (event) => {
      if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      history.pushState({ portfolioCapture: link.getAttribute("href") }, "", location.href);
      openImage(link);
    });
  });
  dialog.querySelector(".dialog-close").addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (event) => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener("close", () => {
    if (suppressHistoryClose) suppressHistoryClose = false;
    else if (history.state?.portfolioCapture) { restoreAfterHistory = true; history.back(); return; }
    restoreFocus();
  });
  const initialLink = links.find((item) => item.getAttribute("href") === history.state?.portfolioCapture);
  if (initialLink) openImage(initialLink);
  window.addEventListener("popstate", (event) => {
    const link = links.find((item) => item.getAttribute("href") === event.state?.portfolioCapture);
    if (link) openImage(link);
    else if (dialog.open) {
      suppressHistoryClose = true;
      dialog.close();
    } else if (restoreAfterHistory) {
      restoreAfterHistory = false;
      restoreFocus();
    }
  });
})();

// Repository composition is pre-rendered; open its key by hover, focus or touch.
(() => {
  const profiles = [...document.querySelectorAll('.language-profile')];
  const closeAll = (except) => profiles.forEach(profile => {
    if (profile === except) return;
    profile.dataset.pinned = '';
    profile.querySelector('.language-key').hidden = true;
    profile.querySelector('button').setAttribute('aria-expanded', 'false');
  });
  profiles.forEach(profile => {
    const button = profile.querySelector('button');
    const key = profile.querySelector('.language-key');
    const show = () => { closeAll(profile); key.hidden = false; button.setAttribute('aria-expanded', 'true'); };
    const hide = () => { key.hidden = true; button.setAttribute('aria-expanded', 'false'); };
    profile.addEventListener('pointerenter', event => { if (event.pointerType === 'mouse') show(); });
    profile.addEventListener('pointerleave', () => { if (!profile.dataset.pinned && !profile.contains(document.activeElement)) hide(); });
    profile.addEventListener('focusin', show);
    profile.addEventListener('focusout', event => { if (!profile.contains(event.relatedTarget)) { profile.dataset.pinned = ''; hide(); } });
    button.addEventListener('click', () => {
      if (profile.dataset.pinned) { profile.dataset.pinned = ''; hide(); }
      else { profile.dataset.pinned = 'true'; show(); }
    });
    profile.addEventListener('keydown', event => { if (event.key === 'Escape') { profile.dataset.pinned = ''; hide(); event.stopPropagation(); } });
  });
  document.addEventListener('pointerdown', event => { if (!event.target.closest('.language-profile')) closeAll(); });
})();
