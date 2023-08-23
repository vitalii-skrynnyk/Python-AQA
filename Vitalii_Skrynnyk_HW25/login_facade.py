import allure

from user_credentials import USER_EMAIL_MAIN_USER, USER_PASSWORD_MAIN_USER
from base_facacde import BaseFacade


class LogInFacade(BaseFacade):
    def __init__(self):
        super().__init__()

    def fill_all_fields_on_login_form_with_correct_data(self,
                                                        email=USER_EMAIL_MAIN_USER,
                                                        password=USER_PASSWORD_MAIN_USER,
                                                        is_click=True):

        self.fill_email_field_on_login_form(email)
        self.fill_password_field_on_login_form(password)

        if is_click:
            self.click_login_button_on_login_form()

    @allure.step("LogIN UI full cycle ")
    def login_full_cycle(self,
                         email=USER_EMAIL_MAIN_USER,
                         password=USER_PASSWORD_MAIN_USER):
        self.click_sign_in_button_on_main_page()
        self.fill_all_fields_on_login_form_with_correct_data(email, password)
        self.click_login_button_on_login_form()

    def fill_email_field_on_login_form(self, email):
        self.login_page.email_field().send_keys(email)

    def fill_password_field_on_login_form(self, password):
        self.login_page.password_field().send_keys(password)

    def click_sign_in_button_on_main_page(self):
        self.navigation_bar_base_page.sign_in_button().click()

    def click_login_button_on_login_form(self):
        self.login_page.log_in_button().click()
