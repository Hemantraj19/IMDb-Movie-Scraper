# IMDb Movie Scraper

This Python script scrapes movie data from IMDb based on user-selected genres and sorting preferences, and then sends the data to a Sheety endpoint to add the scraped data to a google sheet.

## Dependencies
- `selenium`: A web automation library for browser automation.
- `BeautifulSoup`: A library for parsing HTML and XML documents.
- `requests`: A library for making HTTP requests.

## Usage
1. Install the required dependencies using `pip install selenium beautifulsoup4 requests`.
2. Ensure you have the Chrome WebDriver installed and its path configured correctly.
3. Run the script and follow the prompts to select a genre and sorting preference.
4. The script will scrape movie data, including title, release year, and description, and send it to the specified Sheety endpoint.

## Instructions
1. The script opens IMDb, navigates to the genre selection page, and prompts the user to select a genre.
2. After selecting a genre, it scrolls down to load more movies and prompts the user to select a sorting preference.
3. Once the sorting preference is selected, it scrapes movie data and sends it to the Sheety endpoint.

## Note
- Adjust the `scroll_amount` variable based on your need for scrolling to load more movies.
- Replace `"your sheety endpoint"` with the actual Sheety endpoint URL.
