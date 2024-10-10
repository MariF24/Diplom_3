import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from locators import StellaburgerLocators
class HeaderPageBurger(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем браузер')
    def open_page(self,url):
       self.navigate(url)

    @allure.step('Получать URL текущей страницы')
    def get_current_url(self, url):
        self.driver.get(url)
        return self.driver.current_url

    @allure.step('Перейти по клику на Конструктор')
    def link_constructor(self):
        self.click_element(StellaburgerLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_element_visible(StellaburgerLocators.LOGIN_ACCOUNT_BUTTON)

    @allure.step('Перейти по клику на Лента заказов')
    def link_feed(self):
        self.click_element_with_adjustable_timeout(StellaburgerLocators.FEED_BUTTON, 3)
        self.wait_for_element_visible_with_adjustable_timeout(StellaburgerLocators.IN_PROGRESS_TEXT, 4)

    @allure.step('Перейти по клику на Лента заказов с уменьшенным таймаутом')
    def link_feed_for_decreased_timeout(self):
        self.click_element_with_adjustable_timeout(StellaburgerLocators.FEED_BUTTON, 1)
