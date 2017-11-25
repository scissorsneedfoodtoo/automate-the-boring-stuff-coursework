from selenium import webdriver

browser = webdriver.Chrome('/usr/bin/chromedriver')
browser.get('https://automatetheboringstuff.com')

# elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(18) > li:nth-child(1) > a')

# elem.click()

# pCount = browser.find_elements_by_css_selector('p')
#
# print(len(pCount))

# browser.get('https://google.com')

# searchElem = browser.find_element_by_css_selector('#lst-ib')
# searchElem.send_keys('test')
# searchElem.submit()

# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()

# elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > p:nth-child(6)')
# print(elem.text)

elem = browser.find_element_by_css_selector('html')
print(elem.text)
browser.quit()
