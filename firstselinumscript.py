from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.get("https://youtube.com")
searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.sendkeys('Hitessh Choudhary')
searchButton = driver.find_element_by_xpath('//*[@id ="search_icon_legacy"]')
searchButton.click()
