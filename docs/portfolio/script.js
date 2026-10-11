"use strict";
// Progressive enhancement: content and full-size image links work without JS.
(() => {
  const dialog = document.querySelector("#image-dialog");
  const image = document.querySelector("#dialog-image");
  const caption = document.querySelector("#dialog-caption");
  const links = [...document.querySelectorAll("a.capture-button")];
  let trigger = null;
  let suppressHistoryClose = false;
  if (!dialog || typeof dialog.showModal !== "function") return;
  function openImage(link) {
    trigger = link;
    image.src = link.href;
    image.alt = link.querySelector("img").alt;
    caption.textContent = link.closest("figure").querySelector("figcaption").textContent.trim();
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
    else if (history.state?.portfolioCapture) history.back();
    if (trigger) trigger.focus();
  });
  const initialLink = links.find((item) => item.getAttribute("href") === history.state?.portfolioCapture);
  if (initialLink) openImage(initialLink);
  window.addEventListener("popstate", (event) => {
    const link = links.find((item) => item.getAttribute("href") === event.state?.portfolioCapture);
    if (link) openImage(link);
    else if (dialog.open) {
      suppressHistoryClose = true;
      dialog.close();
    }
  });
})();
