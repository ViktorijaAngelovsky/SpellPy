import unittest
from nose.tools import assert_equal, assert_true
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SpellLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)

    def spell_login(self, ):
        self.driver.get("https://demo.ourspell.com")
        self.driver.find_element_by_id("input-email").send_keys("mybrand@ourspell.com")
        self.driver.find_element_by_id("input-password").send_keys("testpassword")
        self.driver.find_element_by_id("btn-login").click()

    def closeBrowser(self):
        self.driver.quit()
