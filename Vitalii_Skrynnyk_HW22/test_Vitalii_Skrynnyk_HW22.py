from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import requests
import json
import time


class UserLoginModel:
    """
    Data model for logging user.
    """

    def __init__(self, email: str, password: str, remember: bool):
        self.email = email
        self.password = password
        self.remember = remember


class TestLoginAndCreatingCar:
    """
    Class verifies login via UI for existing user, creating card via UI, checking card via UI and via API
    """

    def setup_class(self):
        """
        User data gets from test_data.json file
        :return: None
        """
        self.driver = webdriver.Chrome()
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

        with open("test_data.json") as config:
            lines = json.loads(config.read())

        self.session = requests.session()
        self.user_mail = lines["test_user_1_email"]
        self.user_password = lines["test_user_1_password"]
        self.base_url = "https://qauto2.forstudy.space/api"
        self.car_brand = lines["test_user_1_car_brand"]
        self.car_model = lines["test_user_1_car_model"]
        self.mileage = lines["test_user_1_car_mileage"]

        success_registration_test_data = {
            "name": "John",
            "lastName": "Dou",
            "email": self.user_mail,
            "password": self.user_password,
            "repeatPassword": self.user_password,
        }
        self.session.post(
            url=f"{self.base_url}/auth/signup", json=success_registration_test_data
        )

    def test_login_success_ui(self):
        """
        The method verifies successful user login via UI.
        :return: None
        """
        sign_in_button = self.driver.find_element(
            By.XPATH, "//button[text()='Sign In']"
        )
        sign_in_button.click()

        email_field = self.driver.find_element(By.ID, "signinEmail")
        password_field = self.driver.find_element(By.ID, "signinPassword")
        log_in_button = self.driver.find_element(By.XPATH, "//button[text()='Login']")

        email_field.send_keys(self.user_mail)
        password_field.send_keys(self.user_password)
        log_in_button.click()

        time.sleep(1)

        assert self.driver.find_element(
            By.XPATH, "//button[text()='Add car']"
        ).is_displayed()

    def test_add_car_ui(self):
        """
        The method verifies successful adding car via UI.
        :return: None
        """
        add_car_button = self.driver.find_element(
            By.XPATH, "//button[text()='Add car']"
        )
        add_car_button.click()

        brand_field = self.driver.find_element(By.XPATH, "//select[@name='carBrandId']")
        model_field = self.driver.find_element(By.XPATH, "//select[@name='carModelId']")
        mileage_field = self.driver.find_element(By.ID, "addCarMileage")
        add_car_submit_button_ = self.driver.find_element(
            By.XPATH, "//button[text()='Add']"
        )

        Select(brand_field).select_by_visible_text(self.car_brand)
        time.sleep(0.2)
        Select(model_field).select_by_visible_text(self.car_model)
        mileage_field.send_keys(self.mileage)
        add_car_submit_button_.click()

        time.sleep(1)

        assert f"{self.car_brand} {self.car_model}" in self.driver.page_source

    def test_check_car_api(self):
        """
        The method checks the car by API created via UI
        :return:
        """
        login_user = UserLoginModel(self.user_mail, self.user_password, False)

        self.session.post(url=f"{self.base_url}/auth/signin", json=login_user.__dict__)
        result = self.session.get(url=f"{self.base_url}/cars")

        assert (
            result.json()["data"][0]["brand"] == f"{self.car_brand}"
            and result.json()["data"][0]["model"] == f"{self.car_model}"
        )

    def teardown_class(self):
        """
        The method deletes user created during the test
        :return: None
        """
        login_user = UserLoginModel(self.user_mail, self.user_password, False)
        self.session.post(url=f"{self.base_url}/auth/signin", json=login_user.__dict__)

        self.session.delete(url=f"{self.base_url}/users")
