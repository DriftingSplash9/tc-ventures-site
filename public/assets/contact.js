(function () {
  /* Local time in Grande Prairie. Without JS the span reads "Mountain Time",
     which is still true. */
  var el = document.getElementById('local-time');
  if (el && window.Intl && Intl.DateTimeFormat) {
    var fmt = new Intl.DateTimeFormat('en-CA', {
      timeZone: 'America/Edmonton', hour: 'numeric', minute: '2-digit', hour12: false,
      weekday: 'long', timeZoneName: 'short'
    });
    var tick = function () {
      var parts = {};
      fmt.formatToParts(new Date()).forEach(function (p) { parts[p.type] = p.value; });
      el.textContent = parts.hour + ':' + parts.minute + ' ' + parts.timeZoneName + ', ' + parts.weekday;
      el.setAttribute('datetime', new Date().toISOString());
    };
    tick();
    setInterval(tick, 30000);
  }

  /* Copy the address. The button only appears if the clipboard API exists. */
  var btn = document.getElementById('copy-email');
  if (btn && navigator.clipboard && navigator.clipboard.writeText) {
    btn.hidden = false;
    var label = btn.textContent;
    var status = document.getElementById('copy-status');
    btn.addEventListener('click', function () {
      navigator.clipboard.writeText('thomas@tc-ventures.ca').then(function () {
        btn.textContent = 'Copied';
        if (status) status.textContent = 'Address copied to the clipboard.';
        setTimeout(function () { btn.textContent = label; if (status) status.textContent = ''; }, 1800);
      });
    });
  }
})();
