from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base import BasePage
from time import sleep


class LoginPage(BasePage):
    login_tab_selector = (By.XPATH, "//a[@href='/login']")
    email_field_selector = (By.NAME, "email")
    password_field_selector = (By.NAME, "password")
    login_button_selector = (By.XPATH, "//button[@data-qa='login-button']")
    user_tab_selector = (By.CSS_SELECTOR, ".fa-user")
    wrong_password_selector = (By.CSS_SELECTOR, ".login-form p")

    def login_with_email(self, email, password):
        self.driver.find_element(*self.login_tab_selector).click()
        self.driver.find_element(*self.email_field_selector).send_keys(email)
        self.driver.find_element(*self.password_field_selector).send_keys(password)
        self.driver.find_element(*self.login_button_selector).click()
        sleep(2)

    def check_if_logged_in(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.user_tab_selector))

    def check_error_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.wrong_password_selector))

    def check_password_field_validation(self):
        password_field = self.driver.find_element(*self.password_field_selector)
        return password_field.get_property("validity")["valueMissing"]
