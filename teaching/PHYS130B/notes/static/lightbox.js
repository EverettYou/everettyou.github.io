/**
 * Figure lightbox: intercept clicks on figure image links so the image opens
 * in an in-page overlay instead of navigating to the raw image file. Clicking
 * the dark backdrop (or pressing Esc) returns the user to the page.
 *
 * Targets Jupyter Book markup:
 *   <a class="reference internal image-reference" href="_images/foo.png">
 *     <img ... />
 *   </a>
 *
 * Left-click without modifier keys opens the lightbox; Cmd/Ctrl/Shift-click
 * falls through to default behavior (open raw image in new tab, etc.).
 */
(function () {
  function ensureOverlay() {
    var ovl = document.getElementById("pb-lightbox");
    if (ovl) return ovl;

    ovl = document.createElement("div");
    ovl.id = "pb-lightbox";
    ovl.className = "pb-lightbox-overlay";
    ovl.setAttribute("role", "dialog");
    ovl.setAttribute("aria-modal", "true");
    ovl.setAttribute("aria-hidden", "true");
    ovl.innerHTML =
      '<button type="button" class="pb-lightbox-close" aria-label="Close image viewer">&times;</button>' +
      '<img class="pb-lightbox-img" alt="">';
    document.body.appendChild(ovl);

    function close() {
      ovl.classList.remove("pb-lightbox-visible");
      ovl.setAttribute("aria-hidden", "true");
      document.removeEventListener("keydown", onKey);
      // Release src to stop large images lingering in memory
      var img = ovl.querySelector(".pb-lightbox-img");
      if (img) img.removeAttribute("src");
      // Restore scroll on body
      document.body.classList.remove("pb-lightbox-open");
    }

    function onKey(e) {
      if (e.key === "Escape" || e.keyCode === 27) close();
    }

    ovl.addEventListener("click", function (e) {
      var t = e.target;
      // Close on backdrop click or close button; ignore clicks on the image
      if (t === ovl || (t.classList && t.classList.contains("pb-lightbox-close"))) {
        close();
      }
    });

    ovl._open = function (src, alt) {
      var img = ovl.querySelector(".pb-lightbox-img");
      img.src = src;
      img.alt = alt || "";
      ovl.classList.add("pb-lightbox-visible");
      ovl.setAttribute("aria-hidden", "false");
      document.body.classList.add("pb-lightbox-open");
      document.addEventListener("keydown", onKey);
    };

    return ovl;
  }

  function shouldIntercept(event) {
    // Only plain left-clicks
    if (event.button !== 0) return false;
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return false;
    return true;
  }

  function initLightbox(root) {
    var scope = root || document;
    // Jupyter Book figure links wrap <img> with this anchor class pair.
    var anchors = scope.querySelectorAll("a.reference.image-reference");
    for (var i = 0; i < anchors.length; i++) {
      var a = anchors[i];
      if (a.dataset.pbLightbox === "1") continue;
      a.dataset.pbLightbox = "1";
      a.addEventListener("click", function (event) {
        if (!shouldIntercept(event)) return;
        var anchor = event.currentTarget;
        var href = anchor.getAttribute("href");
        if (!href) return;
        var img = anchor.querySelector("img");
        var alt = img ? img.getAttribute("alt") || "" : "";
        event.preventDefault();
        ensureOverlay()._open(href, alt);
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { initLightbox(); });
  } else {
    initLightbox();
  }

  // If the theme swaps content dynamically, rescan on DOM mutations.
  if (window.MutationObserver) {
    var observer = new MutationObserver(function (mutations) {
      for (var m = 0; m < mutations.length; m++) {
        var added = mutations[m].addedNodes;
        for (var n = 0; n < added.length; n++) {
          var node = added[n];
          if (node && node.nodeType === 1) initLightbox(node);
        }
      }
    });
    observer.observe(document.body || document.documentElement, { childList: true, subtree: true });
  }
})();
