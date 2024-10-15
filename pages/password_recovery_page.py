import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from locators import StellaburgerLocators
from data import EMAIL, PASSWORD

class PasswordRecoveryPageBurger(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем браузер Chrome')
    def open_page(self,url):
       self.navigate(url)

    @allure.step('Перейти по ссылке восстановления пароля на страницу восстановления пароля')
    def link_password_recovery(self):
        self.click_element(StellaburgerLocators.PASSWORD_RECOVERY_LINK)
        self.wait_for_element_visible(StellaburgerLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Найти кнопку Восстановить и получить ее текст')
    def get_password_recovery_button_text(self):
        element = self.find_element(StellaburgerLocators.PASSWORD_RECOVERY_BUTTON).text
        return element

    @allure.step('Ввести емейл для восстановления')
    def enter_email_for_recovery(self):
        self.enter_text(StellaburgerLocators.EMAIL_FIELD, EMAIL)
        self.click_element(StellaburgerLocators.PASSWORD_RECOVERY_BUTTON)
        self.wait_for_element_visible(StellaburgerLocators.SAVE_BUTTON)

    @allure.step('Найти кнопку Сохранить и получить ее текст')
    def get_save_button_text(self):
        element = self.find_element(StellaburgerLocators.SAVE_BUTTON).text
        return element

    @allure.step('Нажать на иконку Скрыть/Показать пароль')
    def hide_show_password(self):
        self.click_element(StellaburgerLocators.FIELD_ICON_SHOW_HIDE_PASSWORD)

    @allure.step('Перейти к надписи Восстановление пароля')
    def link_password_recovery_title(self):
        self.click_element(StellaburgerLocators.PASSWORD_RECOVERY_TITLE)

    @allure.step('Получить аттрибут тип для проверки активности или неактивности поля ввода пароля')
    def get_type_field(self):
        element = self.find_element(StellaburgerLocators.PASSWORD_RECOVERY_FIELD)
        return element.get_attribute('type')