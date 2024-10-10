import pytest
import allure
from selenium import webdriver
from config import URL
from pages.password_recovery_page import PasswordRecoveryPageBurger
from pages.login_page import LoginPageBurger
from pages.feed_page import FeedPageBurger
from locators import StellaburgerLocators
from data import EMAIL, PASSWORD

class TestStellaburgerPasswordRecovery:
    @allure.title('Переход на страницу Восстановить пароль')
    def test_check_link_password_recovery(self, driver):
        password_recovery_page = PasswordRecoveryPageBurger(driver)
        login_page = LoginPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        login_page.open_page(URL)
        feed_page.close_duplicate_window_with_increased_timeout()
        login_page.link_account_page()
        password_recovery_page.link_password_recovery()

        assert password_recovery_page.get_password_recovery_button_text() == 'Восстановить'

    @allure.title('Ввод почты и клик по кнопке Восстановить')
    def test_check_click_button_recovery(self, driver):
        password_recovery_page = PasswordRecoveryPageBurger(driver)
        login_page = LoginPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        login_page.open_page(URL)
        feed_page.close_duplicate_window_with_increased_timeout()
        login_page.link_account_page()
        password_recovery_page.link_password_recovery()
        password_recovery_page.enter_email_for_recovery()

        assert password_recovery_page.get_save_button_text() == 'Сохранить'

    @allure.title('Проверить, что при клике на иконку показать/скрыть пароль в режиме показать пароль поле ввода становится активным и подсвечивается')
    def test_click_icon_input_field_active(self, driver):
        password_recovery_page = PasswordRecoveryPageBurger(driver)
        login_page = LoginPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        login_page.open_page(URL)
        feed_page.close_duplicate_window_with_increased_timeout()
        login_page.link_account_page()
        password_recovery_page.link_password_recovery()
        password_recovery_page.enter_email_for_recovery()
        password_recovery_page.hide_show_password()
        type = password_recovery_page.get_type_field()
        assert type == 'text'

    @allure.title('Проверить, что при клике на иконку показать/скрыть пароль в режиме скрыть пароль поле ввода становится неактивным')
    def test_click_icon_input_field_inactive(self, driver):
        password_recovery_page = PasswordRecoveryPageBurger(driver)
        login_page = LoginPageBurger(driver)
        feed_page = FeedPageBurger(driver)
        login_page.open_page(URL)
        feed_page.close_duplicate_window_with_increased_timeout()
        login_page.link_account_page()
        password_recovery_page.link_password_recovery()
        password_recovery_page.enter_email_for_recovery()
        password_recovery_page.hide_show_password()
        password_recovery_page.link_password_recovery_title()
        type = password_recovery_page.get_type_field()
        assert type == 'password'