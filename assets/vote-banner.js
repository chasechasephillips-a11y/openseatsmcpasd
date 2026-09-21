/* Sitewide "the vote is <when>" banner.
 *
 * Most of the toolkit and circulator pages were written during the signature
 * drive and still say things like "sign by Aug 20". Rewriting all of that
 * print collateral the night before the vote is neither safe nor useful, but
 * landing on one of those pages with no idea the vote is imminent is bad. So
 * every secondary page gets this strip at the top, which states the current
 * phase and links home.
 *
 * Phases flip on CENTRAL-TIME CALENDAR MIDNIGHT, matching the homepage:
 *   out -> tomorrow -> today -> now -> after
 *
 * Drop-in: <script src="/assets/vote-banner.js" defer></script>
 */
(function () {
  var MEETING      = new Date('2026-09-22T19:00:00-05:00').getTime();
  var MEETING_ENDS = new Date('2026-09-22T21:00:00-05:00').getTime();
  var DAY_OF       = new Date('2026-09-22T00:00:00-05:00').getTime();
  var DAY_BEFORE   = new Date('2026-09-21T00:00:00-05:00').getTime();

  var WHERE = 'Middleton High School Performing Arts Center, 2100 Bristol St';

  function phase(now) {
    if (now >= MEETING_ENDS) return 'after';
    if (now >= MEETING) return 'now';
    if (now >= DAY_OF) return 'today';
    if (now >= DAY_BEFORE) return 'tomorrow';
    return 'out';
  }

  function copy(ph, now) {
    switch (ph) {
      case 'after':
        return {
          flag: '✓ THANK YOU',
          text: '<strong>The vote happened Tuesday night.</strong> Thank you to everyone who was in the room. Results posted as soon as the district confirms.',
          cta: 'Read more', bg: '#4F6B3E'
        };
      case 'now':
        return {
          flag: '🔴 HAPPENING NOW',
          text: '<strong>The Annual Meeting is underway</strong> at ' + WHERE + '. If you can still get there, go — only people in the room can vote.',
          cta: 'Directions', bg: '#9A3B2C'
        };
      case 'today':
        return {
          flag: '🗳️ THE VOTE IS TONIGHT',
          text: '<strong>Pizza 6:30 · Meeting 7:00</strong> · ' + WHERE + '. Only electors in the room can vote. Nothing to bring, kids welcome.',
          cta: 'Details', bg: '#14223E'
        };
      case 'tomorrow':
        return {
          flag: '🗳️ THE VOTE IS TOMORROW',
          text: '<strong>Tue Sept 22 · pizza 6:30, meeting 7:00</strong> · ' + WHERE + '. Only electors in the room can vote. Nothing to bring, kids welcome.',
          cta: 'Details', bg: '#14223E'
        };
      default:
        var d = Math.floor((MEETING - now) / 86400000);
        return {
          flag: '🗳️ THE VOTE',
          text: '<strong>Tue Sept 22, 7:00 PM</strong> · ' + WHERE + ' · ' + d + ' day' + (d === 1 ? '' : 's') + ' away. Only electors in the room can vote.',
          cta: 'Details', bg: '#14223E'
        };
    }
  }

  function render() {
    if (document.getElementById('os-vote-banner')) return;
    var now = Date.now();
    var c = copy(phase(now), now);

    var bar = document.createElement('div');
    bar.id = 'os-vote-banner';
    bar.setAttribute('role', 'region');
    bar.setAttribute('aria-label', 'Annual Meeting vote details');
    bar.style.cssText = [
      'background:' + c.bg, 'color:#FBF8EF', 'padding:11px 18px', 'text-align:center',
      'font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif',
      'font-size:14px', 'line-height:1.45', 'border-bottom:3px solid #B98521',
      'position:relative', 'z-index:9999'
    ].join(';');

    bar.innerHTML =
      '<strong style="color:#F0C24B;letter-spacing:.06em;">' + c.flag + '</strong>&nbsp; ' +
      c.text +
      ' <a href="/" style="color:#fff;font-weight:700;text-decoration:underline;white-space:nowrap;">' +
      c.cta + ' →</a>';

    // Some toolkit pages are print sheets — keep the banner off the paper.
    var st = document.createElement('style');
    st.textContent = '@media print{#os-vote-banner{display:none !important;}}';
    document.head.appendChild(st);

    document.body.insertBefore(bar, document.body.firstChild);
  }

  // Exported so pages can reuse these boundaries instead of redeclaring them.
  // One source of truth: if the meeting time ever moves, it moves here.
  window.OSVote = {
    MEETING: MEETING,
    MEETING_ENDS: MEETING_ENDS,
    phase: function () { return phase(Date.now()); },
    // "Tomorrow" / "Tonight" / ... as a display word.
    word: function () {
      var ph = phase(Date.now());
      if (ph === 'after') return 'Thank you';
      if (ph === 'now') return 'Happening now';
      if (ph === 'today') return 'Tonight';
      if (ph === 'tomorrow') return 'Tomorrow';
      return Math.floor((MEETING - Date.now()) / 86400000) + ' days away';
    }
  };

  // A page that only wants the phase logic (e.g. /sept22, which IS the
  // details page) opts out of the strip with data-no-banner on the tag.
  var tag = document.currentScript ||
            document.querySelector('script[src*="vote-banner"]');
  var suppressed = tag && tag.hasAttribute('data-no-banner');

  if (!suppressed) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', render);
    } else {
      render();
    }
  }
  document.dispatchEvent(new CustomEvent('osvote:ready'));
})();
