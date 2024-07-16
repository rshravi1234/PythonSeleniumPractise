from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.mark.usefixtures('setUp')
class TestSearcFlight:
    def test_click_on_link(self):
        more = self.driver.find_element(By.XPATH, "//span[@class='more-arr']")
        act = ActionChains(self.driver)
        act.move_to_element(more).perform()
        # spjrny=self.driver.find_element(By.XPATH, "//span[normalize-space()='Spiritual Journey']")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Spiritual Journey']")))
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Spiritual Journey']").click()
        self.wait.until(EC.title_contains('Flight'))
        print(self.driver.title)