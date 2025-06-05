from .fetcher import fetch
from .parser import extract_info, parse_links
from .filter import should_visit
from .storage import save_to_csv
import time

class MiniCrawler:
    def __init__(self, seed_url, domain, max_pages=20, delay=1.0):
        self.queue = [seed_url]
        self.visited = set()
        self.results = []
        self.domain = domain
        self.max_pages = max_pages
        self.delay = delay

    def crawl(self):
        while self.queue and len(self.visited) < self.max_pages:
            url = self.queue.pop(0)
            if url in self.visited:
                continue

            soup = fetch(url)
            if not soup:
                continue

            page_data, links = extract_info(url, soup)
            self.results.append(page_data)
            self.visited.add(url)

            for link in links:
                if should_visit(link, self.visited, self.domain):
                    self.queue.append(link)

            time.sleep(self.delay)

    def save(self, filename="results.csv"):
        save_to_csv(self.results, filename)
