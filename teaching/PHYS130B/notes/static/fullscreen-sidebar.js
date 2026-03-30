/**
 * Fullscreen mode: collapse primary (left) sidebar when entering fullscreen,
 * restore the user's prior sidebar state on exit.
 *
 * - Hides the sidebar immediately on fullscreen-button click (before the async
 *   Fullscreen API completes) so there is no visible flash.
 * - Uses the theme checkbox + change events so PyData / Book theme stay in sync.
 */
(function () {
  /** true = sidebar was open (visible) before we auto-collapsed for fullscreen */
  var savedSidebarOpen = null;

  var fullscreenTriggerState = null;

  function getFullscreenElement() {
    return (
      document.fullscreenElement ||
      document.webkitFullscreenElement ||
      document.mozFullScreenElement ||
      document.msFullscreenElement ||
      null
    );
  }

  function rememberFullscreenTriggerState() {
    var scroller = document.scrollingElement || document.documentElement;
    var docH = scroller ? scroller.scrollHeight : document.documentElement.scrollHeight;
    var viewportH = window.innerHeight;
    var maxScroll = Math.max(1, docH - viewportH);
    fullscreenTriggerState = {
      scrollY: window.scrollY,
      scrollRatio: window.scrollY / maxScroll,
      triggerDocHeight: docH,
      triggerViewportHeight: viewportH
    };
  }

  function restoreScrollToTrigger() {
    if (!fullscreenTriggerState || typeof fullscreenTriggerState.scrollY !== "number") return;
    var maxAttempts = 12;
    var attempt = 0;
    var ratio = typeof fullscreenTriggerState.scrollRatio === "number" ? fullscreenTriggerState.scrollRatio : null;
    var targetY = fullscreenTriggerState.scrollY;

    function computeTargetY() {
      var scroller = document.scrollingElement || document.documentElement;
      var docH = scroller ? scroller.scrollHeight : document.documentElement.scrollHeight;
      var maxScroll = Math.max(0, docH - window.innerHeight);
      if (ratio !== null) {
        return Math.max(0, Math.min(maxScroll, Math.round(maxScroll * ratio)));
      }
      return Math.max(0, Math.min(maxScroll, targetY));
    }

    function applyScrollTarget() {
      targetY = computeTargetY();
      var scroller = document.scrollingElement || document.documentElement;
      if (scroller) scroller.scrollTop = targetY;
      document.documentElement.scrollTop = targetY;
      if (document.body) document.body.scrollTop = targetY;
      window.scrollTo(0, targetY);
    }

    (function retryRestore() {
      applyScrollTarget();
      attempt += 1;
      var delta = window.scrollY - targetY;
      if (Math.abs(delta) <= 2 || attempt >= maxAttempts) return;
      requestAnimationFrame(retryRestore);
    })();
  }

  function notifySidebarCheckbox(checkbox) {
    if (!checkbox) return;
    try {
      checkbox.dispatchEvent(new Event("input", { bubbles: true }));
      checkbox.dispatchEvent(new Event("change", { bubbles: true }));
    } catch (e) {
      /* IE / very old engines */
      var ev;
      if (document.createEvent) {
        ev = document.createEvent("HTMLEvents");
        ev.initEvent("change", true, false);
        checkbox.dispatchEvent(ev);
      }
    }
  }

  function collapsePrimarySidebarForFullscreen(checkbox) {
    if (!checkbox) return;
    /* Theme custom.css: checked => primary sidebar collapsed */
    checkbox.checked = true;
    notifySidebarCheckbox(checkbox);
  }

  function handleFullscreenChange() {
    var checkbox = document.getElementById("pst-primary-sidebar-checkbox");
    if (!checkbox) return;

    var inFullscreen = !!getFullscreenElement();

    if (inFullscreen) {
      if (savedSidebarOpen === null) {
        /* Entered fullscreen without our button capture (rare) */
        savedSidebarOpen = !checkbox.checked;
      }
      collapsePrimarySidebarForFullscreen(checkbox);
      restoreScrollToTrigger();
    } else {
      if (savedSidebarOpen !== null) {
        /* Restore: checked => hidden; was open => unchecked */
        checkbox.checked = !savedSidebarOpen;
        savedSidebarOpen = null;
        notifySidebarCheckbox(checkbox);
      }
      restoreScrollToTrigger();
    }
  }

  document.addEventListener("fullscreenchange", handleFullscreenChange);
  document.addEventListener("webkitfullscreenchange", handleFullscreenChange);
  document.addEventListener("mozfullscreenchange", handleFullscreenChange);
  document.addEventListener("MSFullscreenChange", handleFullscreenChange);

  document.addEventListener(
    "click",
    function (event) {
      var trigger = event.target && event.target.closest ? event.target.closest(".btn-fullscreen-button") : null;
      if (!trigger) return;

      rememberFullscreenTriggerState();

      var checkbox = document.getElementById("pst-primary-sidebar-checkbox");
      if (!checkbox) return;

      /* If not currently in fullscreen, the theme button will enter fullscreen */
      if (!getFullscreenElement()) {
        savedSidebarOpen = !checkbox.checked;
        collapsePrimarySidebarForFullscreen(checkbox);
      }
    },
    true
  );
})();
