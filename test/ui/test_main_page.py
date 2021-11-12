from time import sleep

import pytest
from utils.ui.pages.main_page import MainPage
from utils.ui.pages.login_page import LoginPage
from utils.ui.pages.personal_area_page import PersonalAreaPage


@pytest.mark.login_guest
class TestMainPage:

    def test_go_to_personal_area(self, browser):
        link = "https://planner-dev.x5.ru/"
        page = MainPage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.click_login_form()
        login_page.click_password_form()
        login_page.click_submit()
        #page.go_to_team_tab()
        #page.go_to_personal_area()
        #page.go_to_login_page()
        #personal_area = PersonalAreaPage(browser, browser.current_url)
        #personal_area.go_to_personal_area()
        sleep(15)
