import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ActionChains
class BasePage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    @allure.step('Переходим по URL')
    def navigate(self, url:str):
        self.driver.get(url)

    @allure.step('Получить URL текущей страницы')
    def get_current_url(self, url:str):
        self.driver.get(url)
        return self.driver.current_url

    @allure.step('Находим элемент по локатору')
    def find_element(self, locator:tuple, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))


    @allure.step('Находим и кликаем на элемент')
    def click_element(self, locator:tuple, timeout: int = 10):
        element = self.find_element(locator,timeout)
        element.click()

    @allure.step('Находим элемент, очищаем поле ввода и вводим текст')
    def enter_text(self, locator:tuple, text: str, timeout: int = 10):
        element = self.find_element(locator,timeout)
        element.clear()
        element.send_keys(text)

    @allure.step('Проверяем видимость элемента на странице')
    def wait_for_element_visible(self, locator:tuple, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))


    @allure.step('Проверяем невидимость элемента на странице')
    def wait_for_element_invisible(self, locator:tuple, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))


    @allure.step('Проверяем кликабельность элемента на странице')
    def wait_for_element_clickable(self, locator:tuple, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))


    @allure.step('Находим элемент посредством скроллинга')
    def scroll_to_element(self, locator:tuple):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step('Находим элемент и двигаем его')
    def drag_and_drop_to_element(self, locator_first:tuple, locator_double:tuple, locator_third:tuple, timeout: int = 10):
        element = self.find_element(locator_first)
        target = self.find_element(locator_double)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator_third))



