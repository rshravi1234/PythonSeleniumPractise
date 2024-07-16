import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='class')
def setUp(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.yatra.com")
    driver.maximize_window()
    wait=WebDriverWait(driver,10)
    request.cls.driver=driver
    request.cls.wait = wait
    yield
    driver.close()
