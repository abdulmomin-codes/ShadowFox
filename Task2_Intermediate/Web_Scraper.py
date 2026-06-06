import requests
from bs4 import BeautifulSoup

try:
    # Website URL
    url = "https://www.shadowfox.org.in/"

    # Send request
    response = requests.get(url)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Get website title
    title = soup.title.text

    # Get headings
    headings = soup.find_all(["h1", "h2"])

    # Get paragraphs
    paragraphs = soup.find_all("p")

    # Display extracted data
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

    # Save data to file
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
