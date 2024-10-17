import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from locators import StellaburgerLocators
from data import EMAIL, PASSWORD
class FeedPageBurger(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем браузер')
    def open_page(self,url):
       self.navigate(url)


    @allure.step('Кликнуть на заказ и увидеть всплывающее окно с деталями')
    def click_order_open_popup_with_details(self):
        self.click_element(StellaburgerLocators.IDENTIFIER_ORDER_IN_FEED_AND_HISTORY)
        self.wait_for_element_visible(StellaburgerLocators.POPUP_ORDER_IN_FEED_HISTORY)

    @allure.step('Получить текст всплывающего окна с деталями заказа')
    def get_order_details(self):
        element = self.find_element(StellaburgerLocators.POPUP_ORDER_IN_FEED_HISTORY).text
        return element

    @allure.step('Получить идентификатор созданного заказа')
    def get_order_identifier(self):
        self.wait_for_element_invisible(StellaburgerLocators.DUPLICATE_MODAL_ID_ORDER)
        element = self.find_element(StellaburgerLocators.IDENTIFIER_ORDER, 3).text
        return f'0{element}'

    @allure.step('Дождаться, что дублирующее окно будет невидимым с очень увеличенным таймаутом')
    def wait_window_invisible_with_very_increased_timeout(self):
        self.wait_for_element_invisible(StellaburgerLocators.DUPLICATE_MODAL_ID_ORDER, 20)
        self.find_element(StellaburgerLocators.IDENTIFIER_ORDER)

    @allure.step('Дождаться, что дублирующее окно будет невидимым с увеличенным таймаутом')
    def wait_window_invisible_with_increased_timeout(self):
        self.wait_for_element_invisible(StellaburgerLocators.DUPLICATE_MODAL_ID_ORDER, 15)
        self.find_element(StellaburgerLocators.IDENTIFIER_ORDER)

    @allure.step('Закрыть всплывающее окно с идентификатором заказа')
    def close_popup_with_order_identifier(self):
        self.click_element(StellaburgerLocators.CLOSE_BUTTON_POPUP_ID_ORDER, 10)

    @allure.step('Закрыть всплывающее окно с идентификатором заказа с уменьшенным таймаутом')
    def close_popup_with_order_identifier_with_decreased_timeout(self):
        self.click_element(StellaburgerLocators.CLOSE_BUTTON_POPUP_ID_ORDER, 3)

    @allure.step('Получить идентификатор заказа в работе')
    def get_order_identifier_in_progress(self):
        element = self.find_element(StellaburgerLocators.IDENTIFIER_ORDER_IN_PROGRESS, 5).text
        return element

    @allure.step('Перейти по ссылке к регистрации')
    def link_to_registration(self):
        self.click_element(StellaburgerLocators.REGISTRATION_LINK)

    @allure.step('Ввести имя при регистрации')
    def enter_name_for_registration(self, name):
        self.enter_text(StellaburgerLocators.NAME_FIELD, name)

    @allure.step('Ввести емейл при регистрации')
    def enter_email_for_registration(self, email):
        self.enter_text(StellaburgerLocators.EMAIL_FIELD, email)

    @allure.step('Получить емейл, использованный при регистрации')
    def get_email(self):
        element = self.find_element(StellaburgerLocators.EMAIL_FIELD)
        return element.get_attribute('value')

    @allure.step('Ввести пароль при регистрации')
    def enter_password_for_registration(self, PASSWORD):
        self.enter_text(StellaburgerLocators.PASSWORD_FIELD, PASSWORD)


    @allure.step('Нажать на кнопку регистрации')
    def registration_account(self):
        self.click_element(StellaburgerLocators.REGISTRATION_BUTTON)

    @allure.step('Перейти по ссылке для авторизации')
    def link_to_login(self):
        self.click_element(StellaburgerLocators.LOGIN_LINK)
        self.wait_for_element_visible(StellaburgerLocators.LOGIN_BUTTON)

    @allure.step('Получить идентификатор заказа в Истории заказов')
    def get_order_identifier_history(self):
        element = self.find_element(StellaburgerLocators.IDENTIFIER_ORDER_IN_FEED_AND_HISTORY).text
        return element

    @allure.step('Получить идентификатор заказа в Ленте заказов')
    def get_order_identifier_feed(self):
        element = self.find_element(StellaburgerLocators.IDENTIFIER_ORDER_IN_FEED_AND_HISTORY).text
        return element

    @allure.step('Получить количество заказов, выполненых за все время')
    def get_order_identifier_count_orders_all(self):
        element = self.find_element(StellaburgerLocators.COUNT_ORDERS_ALL).text
        return element

    @allure.step('Перейти к количеству заказов, выполненных за сегодня')
    def scroll_to_count_orders_today(self):
        self.scroll_to_element(StellaburgerLocators.COUNT_ORDERS_TODAY)
        self.wait_for_element_visible(StellaburgerLocators.COUNT_ORDERS_TODAY)
    @allure.step('Получить количество заказов, выполненых за сегодня')
    def get_order_identifier_count_orders_today(self):
        element = self.find_element(StellaburgerLocators.COUNT_ORDERS_TODAY).text
        return element

    @allure.step('Закрыть блокирующее окно для тестирования в Firefox')
    def close_duplicate_window(self):
        self.wait_for_element_invisible(StellaburgerLocators.DUPLICATE_MODAL_ID_ORDER)

    @allure.step('Закрыть блокирующее окно для тестирования в Firefox с увеличенным таймаутом')
    def close_duplicate_window_with_increased_timeout(self):
        self.wait_for_element_invisible(StellaburgerLocators.DUPLICATE_MODAL_ID_ORDER, 20)