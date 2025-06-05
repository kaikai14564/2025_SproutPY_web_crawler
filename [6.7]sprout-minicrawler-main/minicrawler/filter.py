from urllib.parse import urlparse

def should_visit(url, visited, domain):
    # TODO: Skip if already visited
    # TODO: Use urlparse() to check:
    #   - same domain
    #   - path starts with /wiki/
    #   - path does NOT contain ":"
    if url in visited:
        return False
    parsed = urlparse(url)
    if parsed.netloc != domain:
        return False
    if not parsed.path.startswith('/wiki/'):
        return False
    if ':' in parsed.path:
        return False        
    return True