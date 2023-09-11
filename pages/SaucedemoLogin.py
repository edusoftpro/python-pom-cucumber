from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base import BasePage
from time import sleep


class SaucedemoLoginPage(BasePage):
    username_field_selector = (By.ID, "user-name")
    password_field_selector = (By.ID, "password")
    login_button_selector = (By.ID, "login-button")
    shopping_cart_selector = (By.CLASS_NAME, "shopping_cart_link")
    error_button_selector = (By.CLASS_NAME, "error-button")

    title_text = "Swag Labs"

    def get_title(self):
        WebDriverWait(self.driver, 10).until(EC.title_contains(self.title_text))

    def enter_valid_username(self, username):
        self.driver.find_element(*self.username_field_selector).send_keys(username)

    def enter_invalid_username(self, username):
        self.driver.find_element(*self.username_field_selector).send_keys(username)

    def enter_valid_password(self, password):
        self.driver.find_element(*self.password_field_selector).send_keys(password)

    def enter_valid_credentials(self, username, password):
        self.driver.find_element(*self.username_field_selector).send_keys(username)
        self.driver.find_element(*self.password_field_selector).send_keys(password)

    def send_login_form(self):
        self.driver.find_element(*self.login_button_selector).click()
        sleep(1)

    def check_if_logged_in(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.shopping_cart_selector))

    def check_if_error_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.error_button_selector))
