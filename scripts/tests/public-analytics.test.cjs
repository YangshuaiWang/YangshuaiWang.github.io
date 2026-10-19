const assert = require('node:assert/strict');
const test = require('node:test');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const context = vm.createContext({});
vm.runInContext(fs.readFileSync(path.join(__dirname, '../public-analytics/Code.gs'), 'utf8'), context);
const report = (names, rows) => ({dimensionHeaders: names.map(name => ({name})),
  metricHeaders: [{name: 'sessions'}], rows: rows.map(row => ({
    dimensionValues: row.slice(0, -1).map(value => ({value})),
    metricValues: [{value: String(row.at(-1))}]
  }))});
const clock = {generated_at: '2026-10-19T05:00:00Z', date: '2026-10-19', timezone: 'Asia/Singapore'};
test('keeps website totals separate and publishes only aggregate fields', () => {
  const today = report(['hostName'], [['yangshuaiwang.github.io', 2], ['sites.google.com', 3], ['unrelated.example', 1000]]);
  const total = report(['hostName'], [['yangshuaiwang.github.io', 8], ['sites.google.com', 9]]);
  // Reversed headers verify that positions are not assumed.
  const countries = report(['country', 'hostName'], [['Singapore', 'yangshuaiwang.github.io', 8],
    ['(not set)', 'sites.google.com', 2], ['China', 'sites.google.com', 7], ['Secret', 'unrelated.example', 1000]]);
  countries.privateInformation = 'must not be published';
  const result = JSON.parse(JSON.stringify(context.buildPublicSummary(today, total, countries, clock)));
  assert.equal(result.sites.github.total_sessions, 8);
  assert.equal(result.sites.google_sites.today_sessions, 3);
  assert.equal(result.sites.google_sites.country_count, 1);
  assert.deepEqual(result.sites.google_sites.top_countries, [{name:'China', sessions:7}]);
  assert.ok(!JSON.stringify(result).includes('must not be published'));
  assert.ok(!JSON.stringify(result).includes('unrelated.example'));
});
test('empty successful reports produce measured zeroes, while bad metrics fail', () => {
  const empty = report(['hostName'], []);
  assert.equal(context.buildPublicSummary(empty, empty, report(['hostName','country'], []), clock).sites.github.today_sessions, 0);
  assert.throws(() => context.reportRows(report(['hostName'], [['yangshuaiwang.github.io', -1]])));
});
test('crossing midnight relabels the previous snapshot instead of calling it today', () => {
  const label = {textContent: 'Visits today'};
  const card = {dataset: {timezone:'Asia/Singapore', reportDate:'2000-01-01'}, querySelector: () => label};
  vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../../static/js/visitor-stats.js'), 'utf8'), {
    document: {querySelectorAll: () => [card]}, Intl, Date
  });
  assert.equal(label.textContent, 'Visits on 2000-01-01');
});
