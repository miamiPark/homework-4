import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from tests.folder_tests.src.auth_page import AuthPage
from tests.folder_tests.src.main_page import MainPage


class ToEditTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ['BROWSER']

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_1_close(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        main_page = MainPage(self.driver)
        main_form = main_page.main_form
        main_form.open_folder_editors()

        edit_form = main_page.edit_folder_form
        edit_form.close_folder_popup()

    def test_2_return(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        main_page = MainPage(self.driver)
        main_form = main_page.main_form
        main_form.open_folder_editor()

        edit_form = main_page.edit_folder_form
        edit_form.unavailable_pop3()
        edit_form.protected_by_password()
        edit_form.set_password_popup()
        edit_form.return_back()
        edit_form.close_folder_popup_by_cross()

    def test_3_success(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)

        main_page = MainPage(self.driver)
        main_form = main_page.main_form
        main_form.open_folder_editor()

        edit_form = main_page.edit_folder_form
        edit_form.unavailable_pop3()
        edit_form.save_folder_pwd()
