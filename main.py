import requests
from bs4 import BeautifulSoup


def scrape_quotes():
    # Target URL: a website created specifically for training web scrapers
    url = 'http://quotes.toscrape.com/'

    print(f"[*] Connecting to {url}...")

    try:
        # Step 1: Send a GET request to the website
        response = requests.get(url, timeout=10)

        # Step 2: Check if the connection was successful (Status code 200)
        if response.status_code == 200:
            print("[+] Connection successful! Parsing data...\n")

            # Step 3: Convert the HTML content to a searchable BeautifulSoup object
            soup = BeautifulSoup(response.text, 'html.parser')

            # Step 4: Find all blocks containing quotes (they have class 'quote')
            quotes = soup.find_all('div', class_='quote')

            # Step 5: Loop through each block to extract text and author
            for i, quote in enumerate(quotes, 1):
                text = quote.find('span', class_='text').text
                author = quote.find('small', class_='author').text

                # Output formatting
                print(f"Quote #{i}:")
                print(f"  > Author: {author}")
                print(f"  > Text: {text}")
                print("-" * 50)

            print("\n[+] Scraping completed successfully.")
        else:
            print(f"[-] Error: Website returned status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"[-] A critical error occurred: {e}")


# Entry point of the script
if __name__ == '__main__':
    scrape_quotes()