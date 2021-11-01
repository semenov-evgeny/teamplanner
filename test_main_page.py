import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


@pytest.mark.login_guest
class TestMainPage():

    def test_go_to_team_tab(self, browser):
        link = "https://dev-dev.tp.insitech.live/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_team_tab()

    def test_go_to_team_tab1(self, browser):
        link = "https://planner-dev.x5.ru/"
        page = MainPage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.click_login_form()
        login_page.click_password_form()
        login_page.click_submit()
