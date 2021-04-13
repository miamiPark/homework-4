from selenium.webdriver.support.ui import WebDriverWait
from tests.folder_tests.page_component import Page, Component


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    @property
    def top_menu(self):
        return TopMenu(self.driver)


class AuthForm(Component):
    LOGIN = '//input[@name="username"]'
    NEXT = '//span[text()="Ввести пароль"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//span[text()="Войти"]'

    def set_login(self, login):
        iframe = self.driver.find_element_by_class_name('ag-popup__frame__layout__iframe')
        self.driver.switch_to.frame(iframe)
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOGIN)
        )
        button.send_keys(login)
        # self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def next(self):
        self.driver.find_element_by_xpath(self.NEXT).click()

    def set_password(self, pwd):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PASSWORD)
        )
        button.send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def authorize(self, login, password):
        self.set_login(login)
        self.next()
        self.set_password(password)
        self.submit()


class TopMenu(Component):
    USERNAME = 'PH_user-email'

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(self.USERNAME).text
        )