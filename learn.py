

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_drvier():
  # Set options to make browsing easie
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://titan22.com/account/login?return_url=%2Faccount")
  return driver

def main():
  driver = get_drvier()
  driver.find_element(by="id", value="CustomerEmail").send_keys("temedia005@gmailcom" )
  time.sleep(2)
  driver.find_element(by="id", value="CustomerPassword").send_keys("temini2006" + Keys.RETURN)
  time.sleep(2)
  driver.find_element(by="xpath", value='//*[@id="shopify-section-footer"]/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()
  print(driver.current_url)

print(main())

<<<<<<< HEAD
=======
import requests
from datetime import datetime
import time

ticker = input("Enter the ticker symbol: ")
from_date = input('Enter start date in yyyy/mm/dd format:')
to_date = input('Enter end date in yyyy/mm/dd format:')

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))


url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

content = requests.get(url, headers=headers).content
print(content)

with open('data.csv', 'wb') as file:
  file.write(content)
>>>>>>> 9675cf2cfd6bba5414dad84e3c37c194382bac73
