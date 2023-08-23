from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from custom_web_driver import Driver
from login_page import LoginPage
from navigation_bar_base_page import NavigationBar
from add_car_page import AddCarPage
import allure
from user_credentials import USER_NAME_MAIN_USER, USER_LAST_NAME_MAIN_USER, \
    USER_EMAIL_MAIN_USER, USER_PASSWORD_MAIN_USER, CAR_BRAND_1_MAIN_USER, CAR_MODEL_1_MAIN_USER, CAR_MILEAGE_1_MAIN_USER
from login_facade import LogInFacade
from add_car_facade import AddCarFacade


class UserLoginModel:
    """
    Data model for logging user.
    """

    def __init__(self, email: str, password: str, remember: bool):
        self.email = email
        self.password = password
        self.remember = remember


@allure.suite("LogIn and creating a car")
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
        self.login_facade = LogInFacade()
        self.navigation_bar_base_page = NavigationBar()
        self.login_page = LoginPage()
        self.add_car_page = AddCarPage()
        self.add_car_facade = AddCarFacade()

        self.session = requests.session()
        self.user_name = USER_NAME_MAIN_USER
        self.user_last_name = USER_LAST_NAME_MAIN_USER
        self.user_mail = USER_EMAIL_MAIN_USER
        self.user_password = USER_PASSWORD_MAIN_USER
        self.base_url = "https://qauto2.forstudy.space/api"
        self.car_brand = CAR_BRAND_1_MAIN_USER
        self.car_model = CAR_MODEL_1_MAIN_USER
        self.mileage = CAR_MILEAGE_1_MAIN_USER

        success_registration_test_data = {
            "name": self.user_name,
            "lastName": self.user_last_name,
            "email": self.user_mail,
            "password": self.user_password,
            "repeatPassword": self.user_password,
        }
        self.session.post(
            url=f"{self.base_url}/auth/signup", json=success_registration_test_data
        )

    @allure.feature("LogIn UI")
    @allure.link("https://www.google.com", name="UI LogIN")
    def test_login_success_ui(self):
        """
        The method verifies successful user login via UI.
        :return: None
        """
        self.login_facade.login_full_cycle()

        allure.attach(self.driver.get_screenshot_as_png(), name="LogInSuccess", attachment_type=AttachmentType.PNG)

        assert self.driver.find_element(
            By.XPATH, "//button[text()='Add car']"
        ).is_displayed()

    @allure.feature("Adding car UI")
    @allure.link("https://www.google.com", name="Adding a car UI")
    def test_add_car_ui(self):
        """
        The method verifies successful adding car via UI.
        :return: None
        """
        self.add_car_facade.add_car_full_cycle()

        WebDriverWait(driver=self.driver, timeout=1).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, f"//p[text()='{self.car_brand} {self.car_model}']")
            )
        )

        allure.attach(self.driver.get_screenshot_as_png(), name="AddingCarSuccess", attachment_type=AttachmentType.PNG)

        assert f"{self.car_brand} {self.car_model}" in self.driver.page_source

    @allure.feature("Get Car info API")
    @allure.link("https://www.google.com", name="GET /cars")
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
