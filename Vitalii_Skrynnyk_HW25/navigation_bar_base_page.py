from selenium.webdriver.common.by import By
from button import Button
from base_page import BasePage


class NavigationBar(BasePage):
    def __init__(self):
        super().__init__()
        self.sign_in_button = lambda: Button(
            self._driver.find_element(By.XPATH, "//button[text()='Sign In']")
        )
        self.guest_log_in_button = lambda: Button(
            self._driver.find_element(By.XPATH, "//button[text()='Guest log in']")
        )
        self.contacts_button = lambda: Button(
            self._driver.find_element(By.XPATH, "//button[text()='Contacts']")
        )
        self.about_button = lambda: Button(
            self._driver.find_element(By.XPATH, "//button[text()='About']")
        )
        self.home_button = lambda: Button(
            self._driver.find_element(By.XPATH, "//a[text()='Home']")
        )
