import allure
import time

from allure_commons.types import AttachmentType
from selenium import webdriver

exec_path='drivers/chromedriver.exe'

class TestPageSearch:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=exec_path)

    def teardown(self):
        self.driver.quit()

    # blocker  critical normal minor trivial

    @allure.feature('Open pages')
    @allure.story('Открываем страницу google.com')
    @allure.severity('blocker')
    def test_google_search(self):
        self.driver.get('https://google.com')
        with allure.step('Делаем скриншот'):
            assert self.driver.title == 'Google'

    @allure.feature('Open pages')
    @allure.story('Открываем страницу yandex.ru')
    @allure.severity('critical')
    def test_yandex_search(self):
        self.driver.get('https://yandex.ru')
        with allure.step('Делаем скриншот'):
            assert self.driver.title == 'Дзен'

    @allure.feature('Open pages')
    @allure.story('Открываем страницу yahoo.com')
    @allure.severity('trivial')
    def test_yahoo_search(self):
        self.driver.get('https://yahoo.com')
        with allure.step('Делаем скриншот'):
            assert self.driver.title == 'Yahoo | Mail, Weather, Search, Politics, News, Finance, Sports & Videos'

    @allure.feature('Open pages')
    @allure.story('Открываем страницу mail.ru')
    @allure.severity('normal')
    def test_mail_search(self):
        self.driver.get('https://mail.ru')
        with allure.step('Делаем скриншот'):
            assert self.driver.title == 'Mail.ru: почта, поиск в интернете, новости, игры'
