#!/usr/bin/env python

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import unittest

class FabLabLoginFuncTests(unittest.TestCase):
    """ class docstring go here """

    def setUp(self):
        """ Set stuff up.
            Todo: make_fakes, etc. (need fixture specifically for testing) 
        """
        # I believe there's a bug in the Python bindings with finding the Chrome
        # driver, even if it's on your paht, so must pass it to constructor explicitly:
        chromedriver = "./chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        # bring to front
        self.driver.maximize_window()
        self.driver.execute_script('window.focus()')

        # Get the page we need
        self.driver.get("localhost:5000")

    def tearDown(self):
        """ docstring go here """
        # TODO: tear stuff down
        print "Done - closing"
        self.driver.quit()

    def test_forgot_username(self):
        """ Various tests related to the "Can't remember your username?" functionality:
            - Does clicking on link pop up the dialog?
            - TODO: Does the dialog contain the autocomplete field, and does it work?
            - TODO: Does the dialog contain the div for browing through all
              usernames, and are they all there?
        """
        print 'finding and clicking the "Can\'t remember your username?" link'
        forgot_username_link = self.driver.find_element_by_id('username_finder')
        forgot_username_link.click()
        print 'did the dialog pop up?'
        forgot_username_popup = self.driver.find_element_by_class_name('ui-dialog-title')
        self.assertEqual('Look up your username', forgot_username_popup.text)

        """print "checking title"
        assert "Python" in driver.title
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN)
        assert "Google" in self.driver.title
        """

if __name__ == '__main__':
    unittest.main()
