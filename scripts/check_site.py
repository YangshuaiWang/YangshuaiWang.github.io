#!/usr/bin/env python3
"""Check a production Hugo build: archives, local links, headings, remote assets."""
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "public"
ORIGIN = "https://yangshuaiwang.github.io"


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.remote_assets = []
        self.ids = set()
        self.duplicate_ids = []
        self.h1 = 0
        self.citations = []
        self.in_citation = False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            if a["id"] in self.ids:
                self.duplicate_ids.append(a["id"])
            self.ids.add(a["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "article" and "academic-citation" in a.get("class", ""):
            self.in_citation = True
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
            if self.in_citation and a["href"].startswith("/publications/"):
                self.citations.append(a["href"])
        if tag in ("script", "img", "source", "iframe"):
            asset = a.get("src", "")
        elif tag == "link" and a.get("rel") in ("stylesheet", "preload", "modulepreload"):
            asset = a.get("href", "")
        else:
            asset = ""
        if asset:
            self.links.append(asset)
            u = urlsplit(asset)
            if u.netloc and u.netloc != urlsplit(ORIGIN).netloc:
                self.remote_assets.append(asset)

    def handle_endtag(self, tag):
        if tag == "article":
            self.in_citation = False


def main():
    errors = []
    pages = {p: Page(p.read_text()) for p in SITE.rglob("*.html")}
    if not pages:
        raise SystemExit("No HTML build found. Run hugo --cleanDestinationDir first.")
    for file, page in pages.items():
        relative = file.relative_to(SITE).as_posix()
        base = ORIGIN + "/" + relative.removesuffix("index.html")
        for href in page.links:
            url = urlsplit(urljoin(base, href))
            if url.scheme not in ("http", "https") or url.netloc != urlsplit(ORIGIN).netloc:
                continue
            target = SITE / unquote(url.path).lstrip("/")
            if target.is_dir() or url.path.endswith("/"):
                target /= "index.html"
            if not target.exists():
                errors.append(f"{relative}: missing local target {href}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"{relative}: missing anchor {href}")
        for duplicate in page.duplicate_ids:
            errors.append(f"{relative}: duplicate element id {duplicate}")
        for url in page.remote_assets:
            errors.append(f"{relative}: external runtime asset {url}")

    source = json.loads((ROOT / "_extraction/source-data.json").read_text())
    for path in ["index.html", "publications/index.html", "preprints/index.html", "teaching/index.html", "conferences/index.html"]:
        page = pages.get(SITE / path)
        if not page or page.h1 != 1:
            errors.append(f"{path}: expected exactly one h1")

    for path, records in [("publications/index.html", source["publications"]),
                          ("preprints/index.html", source["preprints"] + [source["book"], source["thesis"]])]:
        expected = [f"/publications/{r['slug']}/" for r in records]
        page = pages.get(SITE / path)
        if not page or page.citations != expected:
            errors.append(f"{path}: archive order or membership differs from checked source")

    if errors:
        print("\n".join(sorted(set(errors))))
        return 1
    print(f"PASS: {len(pages)} HTML files; internal links and anchors resolve; runtime assets are local.")
    print(f"PASS: {len(source['publications'])} publications, {len(source['preprints'])} preprints, book and thesis appear in the correct archives and order.")
    print("PASS: each main page has one h1.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
