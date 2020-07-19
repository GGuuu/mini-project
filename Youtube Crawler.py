from selenium import webdriver
import numpy as np
import pandas as pd
import time
from konlpy.tag import Hannanum
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from collections import Counter

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)

url = 'https://www.youtube.com/watch?v=v5MACmCGEc4&t=13s'
num_scroll = 1000

browser = Chrome()
browser.get(url)
browser.implicitly_wait(1)

body = browser.find_element_by_tag_name('body')

comments_list = []

while (num_scroll):
  if (num_scroll%100==0):
    print(num_scroll)
  body.send_keys(Keys.PAGE_DOWN)
  time.sleep(0.3)
  num_scroll -= 1

html0 = browser.page_source
html = BeautifulSoup(html0, 'html.parser')
browser.close()

result = html.find_all('yt-formatted-string', {'id':'content-text'})

for i in range(len(result)) :
  comment = result[i].text
  comments_list.append(comment)

print(len(comments_list))

comment_data = pd.DataFrame(comments_list, columns=['comments'])
comment_data.to_csv('data', index=False)