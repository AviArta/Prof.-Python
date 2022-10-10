from time import sleep

import unittest
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Yandex_Autorization_Check(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # если Chrome() - не работает.
        # убирает уведомление об использовании памяти с принудительным окончанием работы:
        # warnings.simplefilter('ignore', ResourceWarning)

    def test_check_yandex_autorization(self):
        driver = self.driver
        # запуск страницы:
        driver.get('https://passport.yandex.ru/auth/')
        sleep(2)

        # нахождение элемента и заполнение поля:
        email_input = driver.find_element(by='id', value='passp-field-login')
        email_input.clear()
        email_input.send_keys('buzlova.a@yandex.ru')
        sleep(2)

        # нажатие кнопки (xpath - правая кнопка по элементу в коде страницы):
        click_button_email = driver.find_element(by='xpath', value='//*[@id="passp:sign-in"]')
        click_button_email.click()

        # проверка наличия элемента на странице:
        self.assertTrue('Войдите' in driver.page_source.title())
        sleep(2)

        password_input = driver.find_element(by='id', value='passp-field-passwd')
        password_input.clear()
        password_input.send_keys('ArtAvia1711')
        sleep(2)

        click_button_password = driver.find_element(by='id', value='passp:sign-in')
        click_button_password.click()
        sleep(2)

        click_button_confirm = driver.find_element(by='xpath', value='// *[ @ id = "root"] / div / div[2] / div[2] / div / div / div[2] / div[3] / div / div / div / div[1] / form / \
                               div[2] / button')
        click_button_confirm.click()
        sleep(7)

        self.assertTrue('Введите код из СМС, отправленный на номер ' in driver.page_source)
        sleep(10)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()