import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

html_page = requests.get(url, headers=headers)
soup = BeautifulSoup(html_page.content, 'lxml')

stock_section = soup.find_all(attrs={"data-testid": "quote-hdr"})
stock_title = stock_section[0].find('h1').text if stock_section else 'N/A'
print("Stock Title:", stock_title)

# Extract current price
current_price = soup.find(attrs={"data-testid": "qsp-price"}).find('span').text
print(f"Current Price: $",current_price)

# Extract price change
price_change = soup.find(attrs={"data-testid": "qsp-price-change"}).find('span').text
print("Price Change:", price_change)

# Extract percentage change
percentage_change = soup.find(attrs={"data-testid": "qsp-price-change-percent"}).find('span').text
print("Percentage Change:", percentage_change)

# Extract market time notice
market_time_notice = soup.find('div', slot='marketTimeNotice').find('span').text
print("Market Time Notice:", market_time_notice)
