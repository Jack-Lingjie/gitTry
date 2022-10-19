from selenium import webdriver

driver = webdriver.Chrome()
url = 'http://libzw.csu.edu.cn/web/seat3?area=101&segment=1470545&day=2022-10-1&startTime=12:20&endTime=22:00'

driver.get(url)
