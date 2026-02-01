#!/usr/bin/env python3
"""
Fetch all Ultimate Brain documentation pages from thomasjfrank.com
"""

import os
import re
import time
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path

BASE_URL = "https://thomasjfrank.com"
DOCS_BASE = "/docs/ultimate-brain/"
OUTPUT_DIR = Path(__file__).parent.parent / "docs"
DELAY_BETWEEN_REQUESTS = 1  # seconds, be polite to the server


def get_sidebar_links(soup: BeautifulSoup) -> list[dict]:
    """Extract all documentation links from the sidebar navigation."""
    links = []
    seen_urls = set()

    # Find the documentation menu sidebar
    sidebar = soup.find("aside", class_="documentation-menu")
    if not sidebar:
        # Try alternative selectors
        sidebar = soup.find("nav", class_="docs-nav") or soup.find("div", class_="sidebar")

    if not sidebar:
        print("Warning: Could not find sidebar navigation, searching entire page for doc links")
        sidebar = soup

    # Find all links that point to ultimate-brain docs
    for link in sidebar.find_all("a", href=True):
        href = link["href"]

        # Filter for ultimate-brain doc links
        if DOCS_BASE in href or href.startswith(DOCS_BASE):
            full_url = urljoin(BASE_URL, href)

            # Avoid duplicates
            if full_url in seen_urls:
                continue
            seen_urls.add(full_url)

            # Get the link text
            text = link.get_text(strip=True)

            links.append({
                "url": full_url,
                "path": href,
                "title": text
            })

    return links


def fetch_page(url: str) -> tuple[str, BeautifulSoup] | None:
    """Fetch a page and return its HTML and parsed soup."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return response.text, soup
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def extract_main_content(soup: BeautifulSoup) -> str:
    """Extract the main content from a documentation page."""
    # Try to find the main content area
    content = (
        soup.find("article") or
        soup.find("main") or
        soup.find("div", class_="documentation-content") or
        soup.find("div", class_="content")
    )

    if content:
        # Remove navigation, scripts, styles
        for tag in content.find_all(["script", "style", "nav", "aside"]):
            tag.decompose()
        return content.get_text(separator="\n", strip=True)

    return soup.get_text(separator="\n", strip=True)


def url_to_filename(url: str) -> str:
    """Convert a URL to a safe filename."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    # Get the last part of the path as the filename
    name = path.split("/")[-1] or "index"
    # Clean up the name
    name = re.sub(r"[^\w\-]", "_", name)
    return name


def save_page(url: str, html: str, text: str, metadata: dict):
    """Save the fetched page content."""
    filename = url_to_filename(url)

    # Save HTML
    html_dir = OUTPUT_DIR / "html"
    html_dir.mkdir(parents=True, exist_ok=True)
    (html_dir / f"{filename}.html").write_text(html, encoding="utf-8")

    # Save plain text
    text_dir = OUTPUT_DIR / "text"
    text_dir.mkdir(parents=True, exist_ok=True)
    (text_dir / f"{filename}.txt").write_text(text, encoding="utf-8")

    # Save metadata
    meta_dir = OUTPUT_DIR / "metadata"
    meta_dir.mkdir(parents=True, exist_ok=True)
    (meta_dir / f"{filename}.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )


def main():
    """Main function to fetch all documentation pages."""
    print("=" * 60)
    print("Ultimate Brain Documentation Fetcher")
    print("=" * 60)

    # Start with the known first page
    start_url = f"{BASE_URL}{DOCS_BASE}start-using-ultimate-brain-the-simple-way/"

    print(f"\nFetching starting page: {start_url}")
    result = fetch_page(start_url)
    if not result:
        print("Failed to fetch starting page!")
        return

    html, soup = result

    # Get all sidebar links
    print("\nExtracting sidebar navigation links...")
    links = get_sidebar_links(soup)
    print(f"Found {len(links)} documentation pages")

    # Save the index of all pages
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    index_file = OUTPUT_DIR / "index.json"
    index_file.write_text(json.dumps(links, indent=2), encoding="utf-8")
    print(f"Saved page index to {index_file}")

    # Fetch each page
    print("\n" + "-" * 60)
    print("Fetching all documentation pages...")
    print("-" * 60)

    successful = 0
    failed = 0

    for i, link in enumerate(links, 1):
        url = link["url"]
        title = link["title"]
        print(f"\n[{i}/{len(links)}] {title}")
        print(f"    URL: {url}")

        result = fetch_page(url)
        if result:
            page_html, page_soup = result
            text = extract_main_content(page_soup)

            # Extract page title from the page itself if available
            page_title = page_soup.find("h1")
            if page_title:
                link["page_title"] = page_title.get_text(strip=True)

            metadata = {
                **link,
                "fetched_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "content_length": len(text)
            }

            save_page(url, page_html, text, metadata)
            print(f"    ✓ Saved ({len(text)} chars)")
            successful += 1
        else:
            print(f"    ✗ Failed to fetch")
            failed += 1

        # Be polite to the server
        if i < len(links):
            time.sleep(DELAY_BETWEEN_REQUESTS)

    # Summary
    print("\n" + "=" * 60)
    print("COMPLETE")
    print("=" * 60)
    print(f"Successfully fetched: {successful}")
    print(f"Failed: {failed}")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
