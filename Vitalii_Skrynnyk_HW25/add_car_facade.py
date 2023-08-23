import allure
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from custom_web_driver import Driver
from add_car_page import AddCarPage
from user_credentials import CAR_BRAND_1_MAIN_USER, CAR_MODEL_1_MAIN_USER, CAR_MILEAGE_1_MAIN_USER


class AddCarFacade:
    def __init__(self):
        self.add_car_page = AddCarPage()
        self.driver = Driver().driver

    def fill_all_fields_on_add_car_form(self,
                                        car_brand=CAR_BRAND_1_MAIN_USER,
                                        car_model=CAR_MODEL_1_MAIN_USER,
                                        car_mileage=CAR_MILEAGE_1_MAIN_USER,
                                        is_click=True):

        self.fill_car_brand_field_on_add_car_form(car_brand)
        self.fill_car_model_on_add_car_form(car_model)
        self.fill_car_mileage_on_add_car_form(car_mileage)

        if is_click:
            self.click_add_car_submit_button()

    @allure.step("Adding car UI full cycle")
    def add_car_full_cycle(self,
                           car_brand=CAR_BRAND_1_MAIN_USER,
                           car_model=CAR_MODEL_1_MAIN_USER,
                           car_mileage=CAR_MILEAGE_1_MAIN_USER):
        self.click_add_car_button()
        self.fill_all_fields_on_add_car_form(car_brand, car_model, car_mileage)
        self.click_add_car_submit_button()

    def fill_car_brand_field_on_add_car_form(self, car_brand):
        Select(self.add_car_page.brand_field()).select_by_visible_text(car_brand)

    def fill_car_model_on_add_car_form(self, car_model):
        Select(self.add_car_page.model_field()).select_by_visible_text(car_model)

    def fill_car_mileage_on_add_car_form(self, car_mileage):
        self.add_car_page.mileage_field().send_keys(car_mileage)

    def click_add_car_button(self):
        self.driver.find_element(By.XPATH, "//button[text()='Add car']").click()

    def click_add_car_submit_button(self):
        self.add_car_page.add_car_submit_button().click()
