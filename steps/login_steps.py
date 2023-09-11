from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.login import LoginPage


@when('I login using "{email}"/"{password}"')
def step_impl(context, email, password):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.implicitly_wait(10)
    context.driver.get("https://automationexercise.com/")
    context.login_page = LoginPage(context.driver)
    context.login_page.login_with_email(email, password)


@then("I'm logged in")
def step_impl(context):
    context.login_page.check_if_logged_in()
