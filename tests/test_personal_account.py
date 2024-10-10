import pytest
import allure
from selenium import webdriver
from config import URL
from pages.login_page import LoginPageBurger
from pages.feed_page import FeedPageBurger
from locators import StellaburgerLocators
from data import EMAIL, PASSWORD, PAGE_ORDERS_HISTORY
class TestStellaburgerLogin:
    @allure.title('Проверка перехода по клику на Личный кабинет')
    def test_check_link_login(self, driver):
        login_page = LoginPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        login_page.open_page(URL)
        feed_page.close_duplicate_window_with_increased_timeout()
        login_page.link_account_page()

        assert login_page.get_login_button_text() == 'Войти'

    @allure.title('Переход в раздел История заказов')
    def test_check_link_orders_history(self, driver):
        login_page = LoginPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        login_page.open_page(URL)
        feed_page.close_duplicate_window_with_increased_timeout()
        login_page.link_account_page()
        login_page.enter_email(EMAIL)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()
        feed_page.close_duplicate_window_with_increased_timeout()
        login_page.link_account_user()
        login_page.get_orders_history_button_text()
        feed_page.close_duplicate_window_with_increased_timeout()
        login_page.link_orders_history()

        assert login_page.get_current_url(PAGE_ORDERS_HISTORY) == 'https://stellarburgers.nomoreparties.site/account/order-history'

    @allure.title('Выход из аккаунта')
    def test_check_logout(self, driver):
        login_page = LoginPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        login_page.open_page(URL)
        feed_page.close_duplicate_window_with_increased_timeout()
        login_page.link_account_page()
        login_page.enter_email(EMAIL)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()
        login_page.link_account_user()
        login_page.click_logout_button()

        assert login_page.get_login_button_text() == 'Войти'
