from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd 

driver = webdriver.Chrome()
driver.get('https://www.cian.ru/cat.php?deal_type=sale&offer_type=flat&region=1')
time.sleep(5)

for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

cards = soup.find_all('div', {'data-name': 'LinkArea'})

all_data = []
for card in cards:
    data = {
        'price': card.find('span', {'data-mark': 'MainPrice'}),
        'discount_price': card.find('span', {'data-mark': 'DiscountPrice'}),
        'area_price': card.find('p', {'data-mark': 'PriceInfo'}),
        'subtitle': card.find('span', {'data-mark': 'OfferSubtitle'}),
        'address': card.find('a', {'data-mark': 'GeoLabel'})
    }
    
    data = {k: v.text.strip() if v else None for k, v in data.items()}
    all_data.append(data)

driver.quit()

df = pd.DataFrame(all_data)
df.to_csv('cian_data.csv', index=False, encoding='utf-8-sig')