from selenium import webdriver

browser = webdriver.ChromiumEdge()
browser.get('https://www.flashscore.com')

browser.maximize_window()
windows_before = browser.window_handles[0]
print(f'browser.title {browser.title}')