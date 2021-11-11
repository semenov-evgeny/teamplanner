from .base_page import BasePage
from .locators import PersonaAreaPageLocators


class PersonalAreaPage(BasePage):

    # передаем полученные аргументы в родительский класс
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_personal_area(self):
        personal_name_menu = self.browser.find_element(*PersonaAreaPageLocators.PERSONAL_AREA_MENU_NAME)
        personal_name = self.browser.find_element(*PersonaAreaPageLocators.PERSONAL_AREA_NAME)
        print(f'{personal_name}')
        print(f'{personal_name_menu}')
        assert f'{personal_name} == {personal_name_menu} Имена не соответствуют'
