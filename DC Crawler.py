from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

data = []

try:
    for page in range(1, 6000):
        if page%100 == 0:
            print(page)

        url = 'https://gall.dcinside.com/board/lists/?id=extra&page='+str(page)
        driver.get(url=url)

        html0 = driver.page_source
        html = BeautifulSoup(html0, 'html.parser')

        result = html.find_all('td', {'class':'gall_tit ub-word'})

        for i in range(len(result)):
            if result[i].text not in data:
                data.append(result[i].text)
except:
    print('done: {}'.format(page))

print(len(data))
print(data)

DC_data = pd.DataFrame(data, columns=['comments'])
DC_data.to_csv('DC_health_data.csv', index=False)

driver.close()