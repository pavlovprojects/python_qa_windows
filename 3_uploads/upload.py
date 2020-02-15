import os
import pytest
import time
from selenium import webdriver


@pytest.fixture
def chrome_browser():
    return webdriver.Chrome()


def test_download(chrome_browser):
    chrome_browser.get('http://demo.guru99.com/test/upload/')
    # Нужен абсолютный путь
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'selenium.png')
    # Получаем поле типа файл
    input_manager = chrome_browser.find_element_by_css_selector('input#uploadfile_0')
    input_manager.send_keys(filename)
    chrome_browser.find_element_by_id("submitbutton").click()
    time.sleep(10)
