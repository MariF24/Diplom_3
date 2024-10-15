import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from locators import StellaburgerLocators
from data import EMAIL, PASSWORD

class LoginPageBurger(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем браузер Chrome')
    def open_page(self,url):
       self.navigate(url)


    @allure.step('Получить URL страницы История заказов')
    def get_current_url_history(self, url):
        self.get_current_url(url)
        return url


    @allure.step('Перейти по кнопке в личный кабинет для авторизации')
    def link_account_page(self):
        self.click_element(StellaburgerLocators.ACCOUNT_BUTTON)
        self.wait_for_element_visible(StellaburgerLocators.LOGIN_BUTTON)

    @allure.step('Найти кнопку Войти и получить ее текст')
    def get_login_button_text(self):
        element = self.find_element(StellaburgerLocators.LOGIN_BUTTON).text
        return element

    @allure.step('Ввести емейл')
    def enter_email(self, EMAIL):
        self.enter_text(StellaburgerLocators.EMAIL_FIELD, EMAIL)

    @allure.step('Ввести пароль')
    def enter_password(self, PASSWORD):
        self.enter_text(StellaburgerLocators.PASSWORD_FIELD, PASSWORD)

    @allure.step('Кликнуть по кнопке Войти')
    def click_login_button(self):
        self.click_element(StellaburgerLocators.LOGIN_BUTTON)
        self.wait_for_element_visible(StellaburgerLocators.CHECKOUT_BUTTON)


    @allure.step('Найти кнопку История заказов и получить ее текст')
    def get_orders_history_button_text(self):
        element = self.find_element(StellaburgerLocators.LINK_ORDERS_HISTORY).text
        return element

    @allure.step('Перейти по кнопке в личный кабинет зарегистрированного пользователя')
    def link_account_user(self):
        self.click_element(StellaburgerLocators.ACCOUNT_BUTTON)
        self.wait_for_element_visible(StellaburgerLocators.CANCEL_BUTTON)

    @allure.step('Перейти в раздел История заказов')
    def link_orders_history(self):
        self.click_element(StellaburgerLocators.LINK_ORDERS_HISTORY)

    @allure.step('Выйти из аккаунта')
    def click_logout_button(self):
        self.click_element(StellaburgerLocators.LOGOUT_BUTTON)
        self.wait_for_element_visible(StellaburgerLocators.LOGIN_BUTTON)