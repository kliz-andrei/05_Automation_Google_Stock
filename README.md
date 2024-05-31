# 05_Automation_Google_Stock
Automating Google Stock Data Extraction and Visualization with Plotly

This Python script retrieves real-time information about Google's stock (GOOGL) from Yahoo Finance and displays it in the console. It utilizes web scraping techniques to extract the following data:

- **Stock Title:** The name of the stock, extracted from the webpage header.
- **Current Price:** The current price of the stock.
- **Price Change:** The change in the stock price since the last trading session.
- **Percentage Change:** The percentage change in the stock price since the last trading session.
- **Market Time Notice:** Information about the market time status, indicating whether it's open or closed.

**How to Use:**
1. Ensure you have the required Python libraries installed: `requests`, `bs4` (BeautifulSoup).
2. Copy and paste the provided code into a Python script file or a Jupyter Notebook.
3. Run the script or execute the cells to see the real-time stock information printed in the console or output cell.

**Dependencies:**
- `requests`: Used to send HTTP requests to the Yahoo Finance website.
- `BeautifulSoup` (from `bs4`): Used for web scraping, parsing HTML content, and extracting desired information from the webpage.
- `lxml`: Parser library for BeautifulSoup.
- Internet connection: Required to fetch data from the Yahoo Finance website.

**Note:**
- Ensure you are allowed to scrape data from Yahoo Finance according to their terms of service.
- This script provides a simple demonstration of web scraping and may require adjustments if the structure of the Yahoo Finance webpage changes.
- Real-world usage may involve further processing of the extracted data, such as storing it in a database, visualizing it with charts, or integrating it into a larger financial analysis system.
