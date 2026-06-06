# Web Scraper
# Data Extraction: Use libraries like Beautiful Soup or Scrapy to extract
# data from websites.
# ShadowFox Integration: Utilize our ShadowFox website for practicing
# data extraction.
# Implementation: Write Python code to scrape desired information from
# web pages.
# Data Storage: Save scraped data in appropriate formats for further
# analysis or use.
# Error Handling: Implement mechanisms to handle errors gracefully
# during scraping.

import requests
from bs4 import BeautifulSoup

try:
    url = "https://www.shadowfox.org.in/"

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.text

    headings = soup.find_all(["h1", "h2"])

    paragraphs = soup.find_all("p")

    print("\nWebsite Title:")
    print(title)

    print("\nHeadings:")
    for heading in headings:
        print("-", heading.text.strip())

    print("\nParagraphs:")
    for paragraph in paragraphs[:10]:
        text = paragraph.text.strip()
        if text:
            print("-", text)

    with open("shadowfox_data.txt", "w", encoding="utf-8") as file:

        file.write("SHADOWFOX WEBSITE DATA\n")
        file.write("=" * 50 + "\n\n")

        file.write("Website Title:\n")
        file.write(title + "\n\n")

        file.write("Headings:\n")
        for heading in headings:
            file.write(heading.text.strip() + "\n")

        file.write("\nParagraphs:\n")
        for paragraph in paragraphs:
            text = paragraph.text.strip()
            if text:
                file.write(text + "\n")

    print("\nData saved successfully to shadowfox_data.txt")

except requests.exceptions.RequestException as e:
    print("Website connection error:", e)

except Exception as e:
    print("An error occurred:", e)
