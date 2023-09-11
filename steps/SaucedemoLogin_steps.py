from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.SaucedemoLogin import SaucedemoLoginPage


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.implicitly_wait(5)
    context.driver.get("https://www.saucedemo.com/")
    context.login_page = SaucedemoLoginPage(context.driver)
    context.login_page.get_title()


@when('I enter a valid "{username}"')
def step_impl(context, username):
    context.login_page.enter_valid_username(username)


@when('I enter an invalid "{username}"')
def step_impl(context, username):
    context.login_page.enter_invalid_username(username)


@when('I enter a "{password}"')
def step_impl(context, password):
    context.login_page.enter_valid_password(password)


@when('I click the login button')
def step_impl(context):
    context.login_page.send_login_form()


@then('I should see a shopping cart')
def step_impl(context):
    context.login_page.check_if_logged_in()


@then('I should see an error message')
def step_impl(context):
    context.login_page.check_if_error_message()


@when('I enter a valid credentials "{username}" / "{password}"')
def step_impl(context, username, password):
    context.login_page.enter_valid_username(username)
    context.login_page.enter_valid_password(password)


@when('I enter an invalid credentials "{invalid_username}" / "{invalid_password}"')
def step_impl(context, invalid_username, invalid_password):
    context.login_page.enter_invalid_username(invalid_username)
    context.login_page.enter_valid_password(invalid_password)
