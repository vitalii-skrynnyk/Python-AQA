from selenium.webdriver.common.by import By
from text_box import TextBox
from button import Button
from base_page import BasePage


class AddCarPage(BasePage):
    def __init__(self):
        super().__init__()
        self.brand_field = lambda: self._driver.find_element(
            By.XPATH, "//select[@name='carBrandId']"
        )
        self.model_field = lambda: self._driver.find_element(
            By.XPATH, "//select[@name='carModelId']"
        )
        self.mileage_field = lambda: TextBox(
            self._driver.find_element(By.ID, "addCarMileage")
        )
        self.add_car_submit_button = lambda: Button(
            self._driver.find_element(By.XPATH, "//button[text()='Add']")
        )
