from urllib.parse import urljoin

BASE = "https://en.wikipedia.org"

def parse_links(soup):
    links = []
    # TODO: Find all <a> tags and extract href
    # TODO: Only keep internal links that start with "/wiki/" and do not contain ":"
    # TODO: Use urljoin to resolve full URL
    for tag in soup.find_all('a', href=True):
        href = tag['href']
        if href.startswith("/wiki/") and ":" not in href:
            full_url = urljoin(BASE, href)
            links.append(full_url)
    return links

def extract_info(url, soup):
    # TODO: Extract <title> tag text (if exists)
    # TODO: Call parse_links() to get valid internal links
    # TODO: Return both the page info dict and the link list
    title_tag = soup.find('title')
    title = title_tag.text.strip() if title_tag else "No Title"

    links = parse_links(soup)

    # 傳回格式為 dict + links list
    page_info = {
        "url": url,
        "title": title,
        "n_links": len(links)
    }
    return page_info, links
