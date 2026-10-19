/** Public aggregates for the two personal websites. No request parameters are used. */
const PROPERTY = 'properties/559511734';
const SINCE = '2026-10-19';
const HOSTS = {
  github: 'yangshuaiwang.github.io',
  google_sites: 'sites.google.com'
};

function doGet() {
  const cache = CacheService.getScriptCache();
  let output = cache.get('public-summary-v1');
  if (!output) {
    const lock = LockService.getScriptLock();
    if (!lock.tryLock(10000)) return jsonOutput({status: 'unavailable'});
    try {
      output = cache.get('public-summary-v1');
      if (!output) {
        output = JSON.stringify(fetchPublicSummary());
        cache.put('public-summary-v1', output, 1800);
      }
    } catch (error) {
      // Do not expose account details, credentials or internal errors publicly.
      console.error('Unable to refresh public statistics.');
      return jsonOutput({status: 'unavailable'});
    } finally {
      lock.releaseLock();
    }
  }
  return ContentService.createTextOutput(output).setMimeType(ContentService.MimeType.JSON);
}

function jsonOutput(value) {
  return ContentService.createTextOutput(JSON.stringify(value))
    .setMimeType(ContentService.MimeType.JSON);
}

function fetchPublicSummary() {
  const query = (startDate, dimensions) => AnalyticsData.Properties.runReport({
    dateRanges: [{startDate: startDate, endDate: 'today'}],
    dimensions: dimensions.map(name => ({name: name})),
    metrics: [{name: 'sessions'}],
    dimensionFilter: {filter: {
      fieldName: 'hostName',
      inListFilter: {values: Object.values(HOSTS), caseSensitive: false}
    }},
    limit: 1000,
    keepEmptyRows: false
  }, PROPERTY);
  const today = query('today', ['hostName']);
  const total = query(SINCE, ['hostName']);
  const countries = query(SINCE, ['hostName', 'country']);
  const timezone = total.metadata && total.metadata.timeZone;
  if (!timezone) throw new Error('Missing property timezone');
  if ((countries.rowCount || 0) > 1000) throw new Error('Country report truncated');
  const now = new Date();
  return buildPublicSummary(today, total, countries, {
    generated_at: now.toISOString(),
    date: Utilities.formatDate(now, timezone, 'yyyy-MM-dd'),
    timezone: timezone
  });
}

function reportRows(report) {
  const dimensions = (report.dimensionHeaders || []).map(h => h.name);
  const metrics = (report.metricHeaders || []).map(h => h.name);
  return (report.rows || []).map(row => {
    const values = {};
    dimensions.forEach((name, i) => { values[name] = row.dimensionValues[i].value; });
    metrics.forEach((name, i) => {
      const value = Number(row.metricValues[i].value);
      if (!Number.isSafeInteger(value) || value < 0) throw new Error('Invalid metric');
      values[name] = value;
    });
    return values;
  });
}

function buildPublicSummary(todayReport, totalReport, countryReport, clock) {
  const today = reportRows(todayReport);
  const total = reportRows(totalReport);
  const countries = reportRows(countryReport);
  const sites = {};
  Object.entries(HOSTS).forEach(([key, host]) => {
    const todayRow = today.find(row => row.hostName === host);
    const totalRow = total.find(row => row.hostName === host);
    const regions = countries.filter(row => row.hostName === host && row.sessions > 0 &&
      row.country && row.country !== '(not set)' && row.country.length <= 80);
    regions.sort((a, b) => b.sessions - a.sessions || a.country.localeCompare(b.country));
    sites[key] = {
      host: host,
      today_sessions: todayRow ? todayRow.sessions : 0,
      total_sessions: totalRow ? totalRow.sessions : 0,
      country_count: regions.length,
      top_countries: regions.slice(0, 5).map(row => ({name: row.country, sessions: row.sessions}))
    };
  });
  return {
    version: 1, status: 'ok', source: 'Google Analytics 4', metric: 'sessions',
    since: SINCE, generated_at: clock.generated_at, date: clock.date,
    timezone: clock.timezone, sites: sites
  };
}
