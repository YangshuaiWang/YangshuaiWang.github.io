// Preserve truthful labels across midnight and when a scheduled refresh is late.
document.querySelectorAll('.visitor-stats[data-report-date]').forEach(card => {
  try {
    const parts = new Intl.DateTimeFormat('en-CA', {timeZone: card.dataset.timezone,
      year: 'numeric', month: '2-digit', day: '2-digit'}).formatToParts(new Date());
    const value = type => parts.find(part => part.type === type).value;
    const today = `${value('year')}-${value('month')}-${value('day')}`;
    if (today !== card.dataset.reportDate) {
      card.querySelector('[data-today-label]').textContent = `Visits on ${card.dataset.reportDate}`;
    }
  } catch (_) { /* The report date and update time remain visible without Intl support. */ }
});
