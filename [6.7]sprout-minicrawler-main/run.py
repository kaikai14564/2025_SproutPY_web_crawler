from minicrawler.crawler import MiniCrawler
from minicrawler import config

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if __name__ == "__main__":
    crawler = MiniCrawler(
        seed_url=config.SEED_URL,
        domain=config.DOMAIN,
        max_pages=config.MAX_PAGES,
        delay=config.SLEEP_SECONDS
    )
    crawler.crawl()
    crawler.save(config.OUTPUT_FILE)
    print("✅ Crawl complete.")