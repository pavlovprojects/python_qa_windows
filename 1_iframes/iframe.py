from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get("http://0.0.0.0:8000/")

frames = chrome.find_elements_by_css_selector("iframe")

chrome.switch_to.frame(frames[0])
chrome.find_element_by_css_selector("button.header2__auth").click()
chrome.switch_to.default_content()
chrome.find_element_by_link_text("here3").click()

chrome.switch_to.frame("avito")
chrome.find_element_by_link_text("Личные вещи").click()
chrome.switch_to.default_content()
chrome.find_element_by_link_text("here2").click()

chrome.switch_to.frame(frames[1])
chrome.find_element_by_css_selector("#cn-accept-cookie").click()
chrome.switch_to.default_content()
chrome.find_element_by_link_text("here1").click()
