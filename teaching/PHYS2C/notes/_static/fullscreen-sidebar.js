/**
 * Fullscreen mode: collapse primary sidebar on entry, restore state on exit.
 * Uses the theme's checkbox so the toggle button remains functional in fullscreen.
 */
(function () {
  var sidebarWasOpen = false;
  var fullscreenTriggerState = null;

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

  function handleFullscreenChange() {
    var checkbox = document.getElementById("pst-primary-sidebar-checkbox");
    if (!checkbox) return;

    var inFullscreen =
      document.fullscreenElement || document.webkitFullscreenElement;

    if (inFullscreen) {
      /* Theme: checked = sidebar hidden, unchecked = visible. Store visibility to restore on exit. */
      sidebarWasOpen = !checkbox.checked;
      checkbox.checked = true;
      restoreScrollToTrigger();
    } else {
      checkbox.checked = !sidebarWasOpen;
      restoreScrollToTrigger();
    }
  }

  document.addEventListener("fullscreenchange", handleFullscreenChange);
  document.addEventListener("webkitfullscreenchange", handleFullscreenChange);
  document.addEventListener("click", function (event) {
    var trigger = event.target && event.target.closest ? event.target.closest(".btn-fullscreen-button") : null;
    if (trigger) rememberFullscreenTriggerState();
  }, true);
})();
