from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import requests
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from custom_web_driver import Driver
from login_page import LoginPage
from navigation_bar_base_page import NavigationBar
from add_car_page import AddCarPage


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
        self.driver = Driver().driver
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        self.navigation_bar_base_page = NavigationBar()
        self.login_page = LoginPage()
        self.add_car_page = AddCarPage()

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

        self.navigation_bar_base_page.sign_in_button().click()

        self.login_page.email_field().send_keys(self.user_mail)
        self.login_page.password_field().send_keys(self.user_password)

        self.login_page.log_in_button().click()

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

        # select brand = Porsche; model = Cayenne
        Select(self.add_car_page.brand_field()).select_by_visible_text(self.car_brand)
        Select(self.add_car_page.model_field()).select_by_visible_text(self.car_model)

        self.add_car_page.mileage_field().send_keys(self.mileage)

        self.add_car_page.add_car_submit_button().click()

        WebDriverWait(driver=self.driver, timeout=1).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, f"//p[text()='{self.car_brand} {self.car_model}']")
            )
        )

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
