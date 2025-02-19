import requests
from bs4 import BeautifulSoup


def scrape_example_website():
    url = 'http://example.com'
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        # Assume article titles are in h2 tags with class 'article - title'
        article_titles = soup.find_all('h2', class_='article - title')
        for title in article_titles:
            clean_title = title.get_text().strip()
            print(clean_title)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


scrape_example_website()