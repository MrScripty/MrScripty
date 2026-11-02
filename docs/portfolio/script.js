"use strict";
// Progressive enhancement: content and full-size image links work without JS.
(() => {
  const dialog = document.querySelector("#image-dialog");
  const image = document.querySelector("#dialog-image");
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
      const title = active.querySelector("img").alt;
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
  // Single captures get the same proportion-sized frame as gallery images, so their space is reserved before
  // lazy loading finishes and the page does not shift as they arrive.
  document.querySelectorAll("figure.app-capture > a.capture-button").forEach((link) => {
    const frame = document.createElement("div");
    frame.className = "capture-frame";
    const original = link.querySelector("img");
    frame.style.setProperty("--capture-ratio", Number(original.getAttribute("width")) / Number(original.getAttribute("height")));
    link.replaceWith(frame);
    frame.append(link);
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

// Project map: node-editor wires between named ports. Each port's --side (left/right/top/bottom/none)
// comes from CSS so the stacked phone layout can turn or hide wires.
(() => {
  const graph = document.querySelector(".graph");
  const svg = graph?.querySelector(".wires");
  if (!svg) return;
  const NS = "http://www.w3.org/2000/svg";
  const TANGENT = { right: [1, 0], left: [-1, 0], top: [0, -1], bottom: [0, 1] };
  const pairs = (graph.dataset.wires || "").split(/\s+/).filter(Boolean)
    .map((spec) => spec.split(">").map((id) => document.getElementById(id)))
    .filter(([out, into]) => out && into);
  const paths = pairs.map(() => svg.appendChild(document.createElementNS(NS, "path")));
  const anchor = (port, box) => {
    const r = port.getBoundingClientRect();
    const side = getComputedStyle(port).getPropertyValue("--side").trim();
    return { x: r.left + r.width / 2 - box.left, y: r.top + r.height / 2 - box.top, t: TANGENT[side] };
  };
  function draw() {
    const box = graph.getBoundingClientRect();
    svg.setAttribute("viewBox", `0 0 ${box.width} ${box.height}`);
    pairs.forEach(([out, into], i) => {
      const a = anchor(out, box), b = anchor(into, box);
      if (!a.t || !b.t || !out.offsetParent || !into.offsetParent) { paths[i].setAttribute("d", ""); return; }
      paths[i].style.stroke = getComputedStyle(out).borderTopColor;
      const k = Math.max(28, Math.hypot(b.x - a.x, b.y - a.y) * 0.45);
      paths[i].setAttribute("d", `M${a.x} ${a.y}C${a.x + a.t[0] * k} ${a.y + a.t[1] * k} ${b.x + b.t[0] * k} ${b.y + b.t[1] * k} ${b.x} ${b.y}`);
    });
  }
  draw();
  new ResizeObserver(draw).observe(graph);
  document.fonts?.ready.then(draw);
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  // On load each wire draws in, then a pulse travels it once.
  paths.forEach((path, i) => {
    if (!path.getAttribute("d")) return;
    const length = path.getTotalLength();
    const delay = 250 + i * 420;
    path.animate([{ strokeDasharray: `${length}`, strokeDashoffset: length }, { strokeDasharray: `${length}`, strokeDashoffset: 0 }],
      { duration: 520, delay, easing: "cubic-bezier(.4,0,.2,1)", fill: "backwards" });
    if (!("offsetPath" in document.documentElement.style)) return;
    const pulse = svg.appendChild(document.createElementNS(NS, "circle"));
    pulse.setAttribute("r", "4");
    pulse.style.offsetPath = `path("${path.getAttribute("d")}")`;
    pulse.animate([{ offsetDistance: "0%", opacity: 1 }, { offsetDistance: "100%", opacity: 1 }, { offsetDistance: "100%", opacity: 0 }],
      { duration: 900, delay: delay + 140, easing: "ease-in-out", fill: "both" }).finished.then(() => pulse.remove());
  });
})();

// Background: a coarse real-time 2D fluid (Stam's stable fluids with vorticity confinement) moves a
// faint dot grid. The pointer stirs it; slow ambient stirrers keep it alive. Static under reduced motion.
(() => {
  const canvas = document.querySelector(".flow-field");
  const ctx = canvas?.getContext("2d");
  if (!ctx) return;
  const SPACING = 26, CELL = 22, FPS = 30, DT = 1 / FPS, ITER = 12;
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;
  let W = 0, H = 0, nx = 0, ny = 0, u, v, u0, v0, d, d0, curl;
  const IX = (i, j) => i + (nx + 2) * j;

  function resize() {
    const dpr = Math.min(devicePixelRatio || 1, 2);
    W = innerWidth; H = innerHeight;
    canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const next = [Math.ceil(W / CELL), Math.ceil(H / CELL)];
    if (next[0] !== nx || next[1] !== ny) {
      [nx, ny] = next;
      const n = (nx + 2) * (ny + 2);
      [u, v, u0, v0, d, d0, curl] = Array.from({ length: 7 }, () => new Float32Array(n));
    }
    render();
  }

  function bound(b, x) {
    for (let i = 1; i <= nx; i++) {
      x[IX(i, 0)] = b === 2 ? -x[IX(i, 1)] : x[IX(i, 1)];
      x[IX(i, ny + 1)] = b === 2 ? -x[IX(i, ny)] : x[IX(i, ny)];
    }
    for (let j = 1; j <= ny; j++) {
      x[IX(0, j)] = b === 1 ? -x[IX(1, j)] : x[IX(1, j)];
      x[IX(nx + 1, j)] = b === 1 ? -x[IX(nx, j)] : x[IX(nx, j)];
    }
  }
  function advect(b, dst, src, uu, vv) {
    for (let j = 1; j <= ny; j++) for (let i = 1; i <= nx; i++) {
      const k = IX(i, j);
      const x = Math.min(nx + 0.5, Math.max(0.5, i - DT * uu[k]));
      const y = Math.min(ny + 0.5, Math.max(0.5, j - DT * vv[k]));
      const i0 = x | 0, j0 = y | 0, s = x - i0, t = y - j0;
      dst[k] = (1 - s) * ((1 - t) * src[IX(i0, j0)] + t * src[IX(i0, j0 + 1)]) + s * ((1 - t) * src[IX(i0 + 1, j0)] + t * src[IX(i0 + 1, j0 + 1)]);
    }
    bound(b, dst);
  }
  function project(p, div) {
    for (let j = 1; j <= ny; j++) for (let i = 1; i <= nx; i++) {
      const k = IX(i, j);
      div[k] = -0.5 * (u[k + 1] - u[k - 1] + v[IX(i, j + 1)] - v[IX(i, j - 1)]);
      p[k] = 0;
    }
    bound(0, div); bound(0, p);
    for (let n = 0; n < ITER; n++) {
      for (let j = 1; j <= ny; j++) for (let i = 1; i <= nx; i++) {
        const k = IX(i, j);
        p[k] = (div[k] + p[k - 1] + p[k + 1] + p[IX(i, j - 1)] + p[IX(i, j + 1)]) / 4;
      }
      bound(0, p);
    }
    for (let j = 1; j <= ny; j++) for (let i = 1; i <= nx; i++) {
      const k = IX(i, j);
      u[k] -= 0.5 * (p[k + 1] - p[k - 1]);
      v[k] -= 0.5 * (p[IX(i, j + 1)] - p[IX(i, j - 1)]);
    }
    bound(1, u); bound(2, v);
  }
  function confine(strength) {
    for (let j = 1; j <= ny; j++) for (let i = 1; i <= nx; i++) {
      curl[IX(i, j)] = 0.5 * (v[IX(i + 1, j)] - v[IX(i - 1, j)] - u[IX(i, j + 1)] + u[IX(i, j - 1)]);
    }
    for (let j = 2; j < ny; j++) for (let i = 2; i < nx; i++) {
      const k = IX(i, j);
      const gx = 0.5 * (Math.abs(curl[k + 1]) - Math.abs(curl[k - 1]));
      const gy = 0.5 * (Math.abs(curl[IX(i, j + 1)]) - Math.abs(curl[IX(i, j - 1)]));
      const len = Math.hypot(gx, gy) + 1e-5;
      u[k] += DT * strength * (gy / len) * curl[k];
      v[k] -= DT * strength * (gx / len) * curl[k];
    }
  }
  function splat(cx, cy, fx, fy, dye, radius) {
    const r = Math.ceil(radius * 2);
    for (let j = Math.max(1, (cy | 0) - r); j <= Math.min(ny, (cy | 0) + r); j++) {
      for (let i = Math.max(1, (cx | 0) - r); i <= Math.min(nx, (cx | 0) + r); i++) {
        const w = Math.exp(-((i - cx) ** 2 + (j - cy) ** 2) / (radius * radius));
        const k = IX(i, j);
        u[k] += fx * w; v[k] += fy * w; d[k] = Math.min(1, d[k] + dye * w);
      }
    }
  }

  let pointer = null;
  const stirrers = [0, 1, 2].map((n) => ({ phase: n * 2.1, speed: 0.05 + n * 0.017, last: null }));
  function step(time) {
    const s = time / 1000;
    stirrers.forEach((st) => {
      const t = s * st.speed + st.phase;
      const x = (0.5 + 0.42 * Math.sin(t * 1.3)) * nx, y = (0.5 + 0.4 * Math.sin(t * 0.9 + st.phase)) * ny;
      if (st.last) splat(x, y, (x - st.last[0]) * 8, (y - st.last[1]) * 8, 0.006, 3);
      st.last = [x, y];
    });
    if (pointer?.moved) {
      const [x, y, px, py] = [pointer.x / CELL + 0.5, pointer.y / CELL + 0.5, pointer.px / CELL + 0.5, pointer.py / CELL + 0.5];
      const fx = Math.max(-40, Math.min(30, (x - px) * 7)), fy = Math.max(-30, Math.min(30, (y - py) * 7));
      splat(x, y, fx, fy, Math.min(0.35, Math.hypot(fx, fy) * 0.02), 2.2);
      pointer.px = pointer.x; pointer.py = pointer.y; pointer.moved = false;
    }
    confine(9);
    u0.set(u); v0.set(v);
    advect(1, u, u0, u0, v0); advect(2, v, v0, u0, v0);
    project(u0, v0);
    d0.set(d); advect(0, d, d0, u, v);
    for (let k = 0; k < u.length; k++) { u[k] *= 0.992; v[k] *= 0.992; d[k] *= 0.975; }
  }

  const sample = (f, x, y) => {
    const i = Math.min(nx, Math.max(0, x | 0)), j = Math.min(ny, Math.max(0, y | 0)), s = x - i, t = y - j;
    return (1 - s) * ((1 - t) * f[IX(i, j)] + t * f[IX(i, j + 1)]) + s * ((1 - t) * f[IX(i + 1, j)] + t * f[IX(i + 1, j + 1)]);
  };
  // Eight energy levels, batched into one path each: faint neutral at rest, cooler and brighter when stirred.
  const LEVELS = Array.from({ length: 8 }, (_, n) => {
    const e = n / 7;
    return { r: 0.9 + e * 0.9, color: `rgba(${236 - 120 * e | 0},${234 - 50 * e | 0},${230 + 10 * e | 0},${0.075 + e * 0.4})` };
  });
  const buckets = LEVELS.map(() => []);
  function render() {
    ctx.clearRect(0, 0, W, H);
    buckets.forEach((b) => (b.length = 0));
    for (let y = SPACING / 2; y < H; y += SPACING) {
      for (let x = SPACING / 2; x < W; x += SPACING) {
        const cx = x / CELL + 0.5, cy = y / CELL + 0.5;
        const vx = sample(u, cx, cy), vy = sample(v, cx, cy);
        const e = Math.min(1, Math.hypot(vx, vy) * 0.09 + sample(d, cx, cy) * 1.2);
        buckets[Math.min(7, (e * 8) | 0)].push(x + Math.max(-8, Math.min(8, vx * 1.6)), y + Math.max(-8, Math.min(8, vy * 1.6)));
      }
    }
    buckets.forEach((pts, n) => {
      if (!pts.length) return;
      const { r, color } = LEVELS[n];
      ctx.fillStyle = color;
      ctx.beginPath();
      for (let p = 0; p < pts.length; p += 2) ctx.rect(pts[p] - r, pts[p + 1] - r, r * 2, r * 2);
      ctx.fill();
    });
  }

  resize();
  addEventListener("resize", resize);
  if (still) return;
  addEventListener("pointermove", (event) => {
    if (!pointer) pointer = { px: event.clientX, py: event.clientY };
    pointer.x = event.clientX; pointer.y = event.clientY; pointer.moved = true;
  }, { passive: true });
  let last = 0, running = true;
  function frame(time) {
    if (!running) return;
    requestAnimationFrame(frame);
    if (time - last < 1000 / FPS - 2) return;
    last = time;
    step(time);
    render();
  }
  document.addEventListener("visibilitychange", () => {
    running = !document.hidden;
    if (running) requestAnimationFrame(frame);
  });
  requestAnimationFrame(frame);
})();

// Hero verb: cycle what the systems let you do. Each change sweeps a trace line under the new word.
(() => {
  const verb = document.querySelector(".verb");
  if (!verb || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const words = [...verb.querySelectorAll(".verb-word")];
  const trace = verb.querySelector(".verb-trace");
  let current = 0;
  const ease = "cubic-bezier(.3,0,.2,1)";
  function advance() {
    if (document.hidden) return;
    const out = words[current];
    current = (current + 1) % words.length;
    const into = words[current];
    into.setAttribute("data-active", "");
    out.animate([{ transform: "translateY(0)", opacity: 1 }, { transform: "translateY(-.6em)", opacity: 0 }], { duration: 380, easing: ease })
      .finished.then(() => out.removeAttribute("data-active"));
    into.animate([{ transform: "translateY(.6em)", opacity: 0 }, { transform: "translateY(0)", opacity: 1 }], { duration: 420, delay: 120, easing: ease, fill: "backwards" });
    const width = into.offsetWidth / verb.offsetWidth;
    trace.animate([{ transform: "scaleX(0)", opacity: 1 }, { transform: `scaleX(${width})`, opacity: 1, offset: .55 }, { transform: `scaleX(${width})`, opacity: 0 }],
      { duration: 1500, delay: 180, easing: ease, fill: "backwards" });
  }
  setInterval(advance, 2800);
})();
