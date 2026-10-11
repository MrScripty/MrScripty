"use strict";
// Progressive enhancement: content and source links work without JavaScript.
(() => {
  const dialog = document.querySelector("#image-dialog");
  const image = document.querySelector("#dialog-image");
  const caption = document.querySelector("#dialog-caption");
  let trigger = null;
  if (!dialog || typeof dialog.showModal !== "function") return;
  document.querySelectorAll("a.capture-button").forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      trigger = link;
      image.src = link.href;
      image.alt = link.querySelector("img").alt;
      caption.textContent = link.closest("figure").querySelector("figcaption").textContent.trim();
      dialog.showModal();
    });
  });
  dialog.querySelector(".dialog-close").addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (event) => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener("close", () => { if (trigger) trigger.focus(); });
})();
