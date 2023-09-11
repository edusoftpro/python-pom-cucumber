from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    products_tab_selector = (By.XPATH, "//*[@href='/products']")

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def close_add(self):
        self.driver.find_element(*self.products_tab_selector).click()
        self.driver.refresh()
