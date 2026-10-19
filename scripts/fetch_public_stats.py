#!/usr/bin/env python3
"""Fetch the allowlisted public summary; retain the last snapshot on an outage."""
import json
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
HOSTS = {"github": "yangshuaiwang.github.io", "google_sites": "sites.google.com"}
FALLBACK = "https://yangshuaiwang.github.io/visitor-stats.json"


def validate(raw):
    # Construct a new document: never publish arbitrary upstream fields.
    if raw.get("version") != 1 or raw.get("status") != "ok" or raw.get("metric") != "sessions":
        raise ValueError("No usable public summary")
    since = date.fromisoformat(raw["since"])
    if since.isoformat() != "2026-10-19":
        raise ValueError("Unexpected collection start")
    reporting_date = date.fromisoformat(raw["date"])
    generated = datetime.fromisoformat(raw["generated_at"].replace("Z", "+00:00"))
    if generated.tzinfo is None or generated > datetime.now(timezone.utc) + timedelta(minutes=10):
        raise ValueError("Invalid snapshot timestamp")
    zone = ZoneInfo(raw["timezone"])
    if generated.astimezone(zone).date() != reporting_date or reporting_date < since:
        raise ValueError("Inconsistent reporting date")
    result = {"version": 1, "status": "ok", "source": "Google Analytics 4", "metric": "sessions",
              "since": since.isoformat(), "date": reporting_date.isoformat(),
              "generated_at": generated.isoformat(), "timezone": zone.key, "sites": {}}
    def count(value):
        if type(value) is not int or not 0 <= value <= 10**12:
            raise ValueError("Invalid count")
        return value
    for key, host in HOSTS.items():
        entry = raw["sites"][key]
        if entry["host"] != host:
            raise ValueError("Unexpected website")
        today, total = count(entry["today_sessions"]), count(entry["total_sessions"])
        country_count = count(entry["country_count"])
        if today > total or country_count > 300:
            raise ValueError("Inconsistent counts")
        countries = entry["top_countries"]
        if not isinstance(countries, list) or len(countries) > min(5, country_count):
            raise ValueError("Invalid country summary")
        safe_countries = []
        for row in countries:
            name = row["name"]
            if not isinstance(name, str) or not 1 <= len(name) <= 80 or any(ord(c) < 32 for c in name):
                raise ValueError("Invalid country name")
            safe_countries.append({"name": name, "sessions": count(row["sessions"])})
        result["sites"][key] = {"host": host, "today_sessions": today, "total_sessions": total,
                                "country_count": country_count, "top_countries": safe_countries}
    return result


def download(url):
    with urlopen(Request(url, headers={"User-Agent": "YangshuaiWang-PublicStats/1"}), timeout=35) as response:
        body = response.read(65537)
    if len(body) > 65536:
        raise ValueError("Summary too large")
    return validate(json.loads(body))


def main():
    endpoint = json.loads((ROOT / "config/public-stats.json").read_text())["endpoint"]
    if not endpoint:
        print("Public statistics are not connected yet; preserving the pending state.")
        return
    parsed = urlsplit(endpoint)
    if parsed.scheme != "https" or parsed.netloc != "script.google.com" or not parsed.path.startswith("/macros/s/") or not parsed.path.endswith("/exec") or parsed.query:
        raise SystemExit("Unexpected statistics endpoint")
    snapshot = None
    for label, url in [("source", endpoint), ("last published snapshot", FALLBACK)]:
        try:
            snapshot = download(url)
            print(f"Loaded public statistics from {label}; generated {snapshot['generated_at']}.")
            break
        except Exception as error:
            print(f"::warning::Could not read {label} ({type(error).__name__}); trying retained data.")
    if snapshot is None:
        print("::warning::No fresh snapshot; leaving the local snapshot unchanged.")
        return
    output = json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n"
    (ROOT / "data/visitor_stats.json").write_text(output)
    (ROOT / "static/visitor-stats.json").write_text(output)


if __name__ == "__main__":
    main()
