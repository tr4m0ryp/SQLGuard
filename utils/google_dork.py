import requests
from bs4 import BeautifulSoup
from loguru import logger

def find_websites(search_term):
    query = f'inurl:"php?" {search_term}'
    url = f"https://www.google.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        filtered_links = filter_links(links)
        return filtered_links
    except requests.RequestException as e:
        logger.error(f"Error fetching websites: {e}")
        return []

def filter_links(links):
    # Filter the Google search result links to find actual URLs
    valid_links = []
    for link in links:
        if "url?q=" in link and "webcache.googleusercontent.com" not in link:
            start = link.find("url?q=") + 6
            end = link.find("&", start)
            url = link[start:end]
            if url.startswith("http"):
                valid_links.append(url)
    return valid_links
