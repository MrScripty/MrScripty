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
    previous.textContent = "← Previous";
    next.textContent = "Next →";
    previous.setAttribute("aria-label", `Previous ${name} image`);
    next.setAttribute("aria-label", `Next ${name} image`);
    const status = document.createElement("span");
    status.className = "gallery-status";
    status.setAttribute("role", "status");
    status.setAttribute("aria-live", "polite");
    status.setAttribute("aria-atomic", "true");
    controls.append(previous, status, next);
    gallery.prepend(controls);
    gallery.setAttribute("role", "region");
    gallery.setAttribute("aria-label", `${name} image gallery`);
    function select(index, animate = true) {
      current = (index + figures.length) % figures.length;
      figures.forEach((figure, i) => {
        figure.getAnimations().forEach((animation) => animation.cancel());
        figure.hidden = i !== current;
      });
      const active = figures[current];
      const title = active.querySelector(".capture-heading b").textContent.trim();
      status.textContent = `${current + 1} / ${figures.length}`;
      status.setAttribute("aria-label", `Image ${current + 1} of ${figures.length}: ${title}`);
      if (animate && !reducedMotion.matches) active.animate([{ opacity: .35 }, { opacity: 1 }], { duration: 150, easing: "ease-out" });
    }
    figures.forEach((figure, index) => {
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
