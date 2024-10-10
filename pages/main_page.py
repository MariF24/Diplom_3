import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from locators import StellaburgerLocators

class MainPageBurger(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем браузер')
    def open_page(self,url):
       self.navigate(url)


    @allure.step('Получать URL текущей страницы')
    def get_current_url(self, url):
        self.driver.get(url)
        return self.driver.current_url


    @allure.step('Найти кнопку Войти в аккаунт и получить ее текст')
    def get_login_account_button_text(self):
        element = self.find_element(StellaburgerLocators.LOGIN_ACCOUNT_BUTTON).text
        return element

    @allure.step('Кликнуть на ингредиент и увидеть всплывающее окно с деталями')
    def click_ingredient_open_popup_with_details(self):
        self.click_element(StellaburgerLocators.CLICK_INGREDIENT_BUN)
        self.wait_for_element_visible(StellaburgerLocators.POPUP_INGREDIENT)

    @allure.step('Найти и получить текст всплывающее окно с деталями')
    def get_popup_ingredient_text(self):
        element = self.find_element(StellaburgerLocators.POPUP_INGREDIENT).text
        return element

    @allure.step('Закрыть всплывающее окно с деталями об ингредиенте')
    def close_popup_with_details(self):
        self.click_element(StellaburgerLocators.CLOSE_POPUP_INGREDIENT)
        self.click_element(StellaburgerLocators.LOGO_FIELD)

    @allure.step('Получить информацию о количестве ингредиента')
    def get_about_ingredient(self):
        element = self.find_element(StellaburgerLocators.COUNT_INGREDIENT).text
        return element

    @allure.step('Добавить один ингредиент в заказ')
    def add_one_ingredient_in_order(self):
        self.drag_and_drop_to_element(StellaburgerLocators.CLICK_INGREDIENT_BUN, StellaburgerLocators.DRAG_FIELD, StellaburgerLocators.DRAG_INGREDIENT_BUN)


    @allure.step('Добавить два ингредиента в заказ')
    def add_two_ingredients_in_order(self):
        self.drag_and_drop_to_element(StellaburgerLocators.CLICK_INGREDIENT_BUN, StellaburgerLocators.DRAG_FIELD, StellaburgerLocators.DRAG_INGREDIENT_BUN)
        self.click_element(StellaburgerLocators.SECTION_SAUCES)
        self.drag_and_drop_to_element(StellaburgerLocators.CLICK_INGREDIENT_SAUCE, StellaburgerLocators.DRAG_FIELD_WITH_BUN, StellaburgerLocators.DRAG_INGREDIENT_SAUCE)
    @allure.step('Добавить три ингредиента в заказ')
    def add_three_ingredients_in_order(self):
        self.drag_and_drop_to_element(StellaburgerLocators.CLICK_INGREDIENT_BUN, StellaburgerLocators.DRAG_FIELD,
                                      StellaburgerLocators.DRAG_INGREDIENT_BUN)
        self.click_element(StellaburgerLocators.SECTION_SAUCES)
        self.drag_and_drop_to_element(StellaburgerLocators.CLICK_INGREDIENT_SAUCE,
                                      StellaburgerLocators.DRAG_FIELD_WITH_BUN,
                                      StellaburgerLocators.DRAG_INGREDIENT_SAUCE)
        self.click_element(StellaburgerLocators.SECTION_FILLINGS)
        self.drag_and_drop_to_element(StellaburgerLocators.CLICK_INGREDIENT_FILLING,
                                      StellaburgerLocators.DRAG_FIELD_WITH_BUN,
                                      StellaburgerLocators.DRAG_INGREDIENT_FILLING)

    @allure.step('Добавить четыре ингредиента в заказ')
    def add_four_ingredients_in_order(self):
        self.drag_and_drop_to_element(StellaburgerLocators.CLICK_INGREDIENT_BUN, StellaburgerLocators.DRAG_FIELD,
                                      StellaburgerLocators.DRAG_INGREDIENT_BUN)
        self.click_element(StellaburgerLocators.SECTION_SAUCES)
        self.drag_and_drop_to_element(StellaburgerLocators.CLICK_INGREDIENT_SAUCE,
                                      StellaburgerLocators.DRAG_FIELD_WITH_BUN,
                                      StellaburgerLocators.DRAG_INGREDIENT_SAUCE)
        self.click_element(StellaburgerLocators.SECTION_FILLINGS)
        self.drag_and_drop_to_element(StellaburgerLocators.CLICK_INGREDIENT_FILLING,
                                      StellaburgerLocators.DRAG_FIELD_WITH_BUN,
                                      StellaburgerLocators.DRAG_INGREDIENT_FILLING)
        self.click_element(StellaburgerLocators.SECTION_SAUCES)
        self.drag_and_drop_to_element(StellaburgerLocators.CLICK_INGREDIENT_SAUCE,
                                      StellaburgerLocators.DRAG_FIELD_WITH_BUN,
                                      StellaburgerLocators.DRAG_INGREDIENT_SAUCE)

    @allure.step('Нажать на кнопку оформить заказ и увидеть всплывающее окно с идентификатором заказа')
    def click_checkout_open_popup_with_identifier(self):
        self.click_element(StellaburgerLocators.CHECKOUT_BUTTON)

    @allure.step('Получить текст всплывающего окна с идентификатором заказа')
    def get_identifier(self):
        element = self.find_element(StellaburgerLocators.POPUP_ID_ORDER).text
        return element

    @allure.step('Закрыть всплывающее окно с идентификатором заказа')
    def close_popup_with_identifier(self):
        self.click_element(StellaburgerLocators.CLOSE_POPUP_ID_ORDER)
        self.click_element(StellaburgerLocators.LOGO_FIELD)