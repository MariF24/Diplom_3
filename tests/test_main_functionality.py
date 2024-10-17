import pytest
import allure
from selenium import webdriver
from config import URL
from pages.login_page import LoginPageBurger
from pages.main_page import MainPageBurger
from pages.header_page import HeaderPageBurger
from pages.feed_page import FeedPageBurger
from locators import StellaburgerLocators
from data import EMAIL, PASSWORD, PAGE_ORDERS_FEED

class TestStellaburgerMainPage:
    @allure.title('Переход по клику к Конструктору с переходом до этого к Ленте заказов для фиксации перехода')
    def test_check_link_feed_to_constructor(self, driver):
        main_page = MainPageBurger(driver)
        header_page = HeaderPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        main_page.open_page(URL)
        feed_page.close_duplicate_window()
        header_page.link_feed()
        header_page.link_constructor()

        assert main_page.get_login_account_button_text() == 'Войти в аккаунт'


    @allure.title('Переход по клику к Ленте заказов')
    def test_check_link_to_feed(self, driver):
        main_page = MainPageBurger(driver)
        header_page = HeaderPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        main_page.open_page(URL)
        feed_page.close_duplicate_window()
        header_page.link_feed()

        assert main_page.get_current_url(PAGE_ORDERS_FEED) == 'https://stellarburgers.nomoreparties.site/feed'

    @allure.title('Кликнуть на ингредиент и увидеть всплывающее окно с деталями')
    def test_click_open_popup_ingredient(self, driver):
        main_page = MainPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        main_page.open_page(URL)
        feed_page.close_duplicate_window()
        main_page.click_ingredient_open_popup_with_details()
        assert 'Детали ингредиента' in main_page.get_popup_ingredient_text()

    @allure.title('Закрыть всплывающее окно кликом по крестику')
    def test_click_close_popup_ingredient(self, driver):
        main_page = MainPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        main_page.open_page(URL)
        feed_page.close_duplicate_window()
        main_page.click_ingredient_open_popup_with_details()
        main_page.close_popup_with_details()
        assert main_page.get_login_account_button_text() == 'Войти в аккаунт'


    @allure.title('Добавить ингредиент и увеличить счетчик этого ингредиента')
    def test_add_and_increase_ingredient(self, driver):
        main_page = MainPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        main_page.open_page(URL)
        feed_page.close_duplicate_window_with_increased_timeout()
        main_page.add_one_ingredient_in_order()

        assert main_page.get_about_ingredient() == '2'

    @allure.title('Оформить заказ от зарегистрированного пользователя')
    def test_create_order_user(self, driver):
        main_page = MainPageBurger(driver)
        login_page = LoginPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        login_page.open_page(URL)
        feed_page.close_duplicate_window_with_increased_timeout()
        login_page.link_account_page()
        login_page.enter_email(EMAIL)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()
        main_page.add_one_ingredient_in_order()
        main_page.click_checkout_open_popup_with_identifier()

        assert 'идентификатор заказа' in main_page.get_identifier()
