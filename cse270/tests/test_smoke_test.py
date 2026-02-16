import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestSmokeTest():

    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self, method):
        self.driver.quit()

    def test_smoke(self):
        driver = self.driver

        # Open Home Page
        driver.get("http://127.0.0.1:5500/cse270/teton/1.6/")

        # Verify Logo
        assert driver.find_element(By.CSS_SELECTOR, ".header-logo img")

        # Verify Heading
        assert driver.find_element(By.CSS_SELECTOR, ".header-title > h1")

        # Verify Title
        assert "Teton Idaho CoC" in driver.title

        # Go to Directory
        driver.find_element(By.LINK_TEXT, "Directory").click()

        # Verify Grid Button
        assert driver.find_element(By.ID, "directory-grid")

        # Go to Join Page
        driver.find_element(By.LINK_TEXT, "Join").click()

        

        # Verify First Name Input
        assert driver.find_element(By.NAME, "fname")

        # Go to Admin Page
        driver.find_element(By.LINK_TEXT, "Admin").click()

        # Verify Username Field
        assert driver.find_element(By.ID, "username")
