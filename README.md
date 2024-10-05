# Web-Scraper

# Newegg Product Scraper

This script scrapes product information from Newegg's website based on a search term provided by the user. The script fetches multiple pages of search results, extracts the product names, prices, and links, and then sorts the products by price in ascending order. Finally, it displays the sorted product information in the terminal.

DO NOT USE THIS SCRIPT IT IS FOR EDUCATIONAL PURPOSES ONLY. I HAVE BEEN BLOCKED BY NEWEGG FOR WEB SCRAPPING SO CANNOT TEST THIS SCRIPT ANYMORE.
USE WITH CAUTION

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- `requests` library
- `BeautifulSoup` from the `bs4` library
- `re` library (included in Python's standard library)

You can install the required libraries using pip:

```sh
pip install requests beautifulsoup4
```

3. **Input the Search Term:**

   The script will prompt you to enter the name of the product you want to search for. Type the product name and press `Enter`.

4. **View the Results:**

   The script will scrape the Newegg website, find products matching your search term, and display the following information for each product in ascending order by price:

   - Product name
   - Price
   - URL link to the product

   The output format will look like this:

   ```sh
   Product Name
   $Price
   https://link.to.product
   -------------------------------
   ```
    and it will sort the product according to its prices so you can fidn the cheapest one
## How It Works

1. **Search Term Input:**

   The user inputs a product name, which the script uses to build a search URL for Newegg.

2. **Web Scraping:**

   The script makes HTTP requests to Newegg, fetching the HTML content of the search results pages using the `requests` library. It then parses the HTML using `BeautifulSoup`.

3. **Pagination:**

   The script determines the number of result pages by scraping the pagination information from the first page.

4. **Product Extraction:**

   The script iterates over all result pages, extracting product names, prices, and links that match the search term.

5. **Sorting and Display:**

   The extracted products are stored in a dictionary, sorted by price in ascending order, and then printed to the terminal.

## Notes

- The script only extracts products with visible prices. If a product's price is hidden or unavailable, it will not be included in the results.
- The script is designed to work with Newegg's current website structure. If Newegg changes its HTML layout, the script may need to be updated accordingly.

## Disclaimer

This script is for educational purposes only. Scraping websites can be against the terms of service of some websites, including Newegg. Use this script responsibly and ensure you are not violating any legal agreements or terms of service.
USE WITH CAUTION
This was a college project that i did for time pass. Did not expect to be IP Blocked by newegg if any newegg employees are reading this pls unban me. i love your site
