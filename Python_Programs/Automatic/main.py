import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the relevant HTML elements containing the data you want to scrape
        article_titles = soup.find_all('h2', class_='article-title')

        # Extract and print the titles
        for title in article_titles:
            print(title.text.strip())
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Replace this URL with the actual URL of the website you want to scrape
url_to_scrape = 'https://www.google.com'  # Replace with the actual URL
scrape_website(url_to_scrape)
