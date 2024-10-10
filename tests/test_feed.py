import pytest
import allure
from selenium import webdriver
from config import URL
from pages.login_page import LoginPageBurger
from pages.main_page import MainPageBurger
from pages.header_page import HeaderPageBurger
from pages.feed_page import FeedPageBurger
from locators import StellaburgerLocators
from data import EMAIL, PASSWORD
from helpers import get_registration_data
class TestStellaburgerFeedPage:
    @allure.title('Кликнуть на заказ и открыть всплывающее окно с деталями')
    def test_click_order_open_order_details(self, driver):
        feed_page = FeedPageBurger(driver)
        header_page = HeaderPageBurger(driver)
        feed_page.open_page(URL)
        feed_page.close_duplicate_window()
        header_page.link_feed()
        feed_page.click_order_open_popup_with_details()
        assert 'Cостав\n' in feed_page.get_order_details()


    @allure.title('Оформить заказ от зарегистрированного пользователя и увидеть его номер в разделе В работе')
    def test_check_order_in_progress(self, driver):
        main_page = MainPageBurger(driver)
        login_page = LoginPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        header_page = HeaderPageBurger(driver)
        login_page.open_page(URL)
        feed_page.close_duplicate_window_with_increased_timeout()
        login_page.link_account_page()
        login_page.enter_email(EMAIL)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()
        main_page.add_four_ingredients_in_order()
        main_page.click_checkout_open_popup_with_identifier()
        expected_result = feed_page.get_order_identifier_with_decreased_timeout()
        feed_page.close_popup_with_order_identifier_with_decreased_timeout()
        header_page.link_feed_for_decreased_timeout()
        assert expected_result == feed_page.get_order_identifier_in_progress()


    @allure.title('Проверить, что заказы пользователя из Истории заказов отображаются в Ленте заказов')
    def test_check_user_orders_in_history_and_feed(self, driver):
        name,email = get_registration_data()
        main_page = MainPageBurger(driver)
        login_page = LoginPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        header_page = HeaderPageBurger(driver)
        feed_page.open_page(URL)
        feed_page.close_duplicate_window_with_increased_timeout()
        login_page.link_account_page()
        feed_page.link_to_registration()
        feed_page.enter_name_for_registration(name)
        feed_page.enter_email_for_registration(email)
        login_email = feed_page.get_email()
        feed_page.enter_password_for_registration(PASSWORD)
        feed_page.registration_account()
        feed_page.link_to_login()
        login_page.link_account_page()
        login_page.enter_email(login_email)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()
        main_page.add_two_ingredients_in_order()
        main_page.click_checkout_open_popup_with_identifier()
        feed_page.wait_window_invisible_with_very_increased_timeout()
        feed_page.close_popup_with_order_identifier()
        login_page.link_account_user()
        login_page.get_orders_history_button_text()
        login_page.link_orders_history()
        order_identifier_history = feed_page.get_order_identifier_history()
        header_page.link_feed()
        assert order_identifier_history == feed_page.get_order_identifier_feed()


    @allure.title('Проверить, что при создании нового заказа счетчик Выполнено за все время увеличивается')
    def test_check_count_orders_all(self, driver):
        main_page = MainPageBurger(driver)
        login_page = LoginPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        header_page = HeaderPageBurger(driver)
        header_page.open_page(URL)
        feed_page.close_duplicate_window_with_increased_timeout()
        header_page.link_feed()
        count_orders_all_expected = feed_page.get_order_identifier_count_orders_all()
        login_page.link_account_page()
        login_page.enter_email(EMAIL)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()
        main_page.add_two_ingredients_in_order()
        main_page.click_checkout_open_popup_with_identifier()
        feed_page.wait_window_invisible_with_very_increased_timeout()
        feed_page.close_popup_with_order_identifier()
        header_page.link_feed()
        count_orders_all_actual = feed_page.get_order_identifier_count_orders_all()
        assert int(count_orders_all_expected) < int(count_orders_all_actual)


    @allure.title('Проверить, что при создании нового заказа счетчик Выполнено за сегодня увеличивается')
    def test_check_count_orders_today(self, driver):
        main_page = MainPageBurger(driver)
        login_page = LoginPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        header_page = HeaderPageBurger(driver)
        header_page.open_page(URL)
        feed_page.close_duplicate_window_with_increased_timeout()
        header_page.link_feed()
        feed_page.scroll_to_count_orders_today()
        count_orders_today_expected = feed_page.get_order_identifier_count_orders_today()
        login_page.link_account_page()
        login_page.enter_email(EMAIL)
        login_page.enter_password(PASSWORD)
        login_page.click_login_button()
        main_page.add_two_ingredients_in_order()
        main_page.click_checkout_open_popup_with_identifier()
        feed_page.wait_window_invisible_with_increased_timeout()
        feed_page.close_popup_with_order_identifier()
        header_page.link_feed()
        feed_page.scroll_to_count_orders_today()
        count_orders_today_actual = feed_page.get_order_identifier_count_orders_today()
        assert int(count_orders_today_expected) < int(count_orders_today_actual)