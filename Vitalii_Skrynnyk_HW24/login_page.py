from selenium.webdriver.common.by import By

# create files for web_elements
# (see https://github.com/OleksiiKhatuntsev/Group22_05_repo/blob/master/Selenium/registration_page.py)
# and rewrite code below for the LoginPage
from text_box import TextBox
from button import Button
from base_page import BasePage
from check_box import CheckBox


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.email_field = lambda: TextBox(
            self._driver.find_element(By.ID, "signinEmail")
        )
        self.password_field = lambda: TextBox(
            self._driver.find_element(By.ID, "signinPassword")
        )
        self.remember_check_box = lambda: CheckBox(
            self._driver.find_element(By.ID, "remember")
        )
        self.forgot_password_button = lambda: Button(
            self._driver.find_element(By.XPATH, "//button[text()='Forgot password']")
        )
        self.registration_button = lambda: Button(
            self._driver.find_element(By.XPATH, "//button[text()='Registration']")
        )
        self.log_in_button = lambda: Button(
            self._driver.find_element(By.XPATH, "//button[text()='Login']")
        )
