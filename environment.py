from browser import Browser
from pages.search_page import SearchPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.cart_page import CartPage

def before_all(context):
    context.browser = Browser()
    context.search_page = SearchPage()
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    context.cart_page = CartPage()

def after_all(context):
    context.browser.close()
