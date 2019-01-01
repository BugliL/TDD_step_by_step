from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class TestCase(LiveServerTestCase):
    """
        LiveServerTestCase
        inherits unittest, it let using assertion
        and open the project in the browser

        To make it automatic test, I'm using the
        Selenium package

        10) Install firefox
        20) Install geckodriver (https://github.com/mozilla/geckodriver/releases)
        25) Add geckodriver to PATH environment variable
        30) pip install selenium
    """

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def test_true(self):
        self.assertTrue(True)
