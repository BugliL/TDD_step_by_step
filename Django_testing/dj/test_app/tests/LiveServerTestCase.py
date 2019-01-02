from django.test import LiveServerTestCase
from django.urls import reverse
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

    def test_as_student_I_want_to_search_solos_so_I_can_improve_my_improvisation(self):
        """
            As: Student Steve
            I want to : search solos
            So that: I can improve my improvisation
        """

        # Actions to perform:
        #   Visit homepage
        #   Provide a search form in page
        #   Provide Steve instrument
        #   Provide Steve instrument and singer
        #   Steve clicks on search results
        #   The page contains has solo data

        home_page = self.browser.get(self.live_server_url + reverse('test_app:LiveServerTestCase'))
        brand_element = self.browser.find_element_by_css_selector('.navbar_brand')
        self.assertEqual('JMAD', brand_element.text)

    def tearDown(self):
        self.browser.quit()
