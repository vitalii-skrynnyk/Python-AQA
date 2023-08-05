import requests
import json


class UserLoginModel:
    """
    Data model for logging user.
    """

    def __init__(self, email: str, password: str, remember: bool):
        self.email = email
        self.password = password
        self.remember = remember


class TestRegistration:
    """
    Class verifies the successful user login and happy pass for GET /users/profile
    """

    def setup_class(self):
        """
        User data gets from test_data.json file
        :return: None
        """
        with open("test_data.json") as config:
            lines = json.loads(config.read())

        self.session = requests.session()
        self.user_mail = lines["test_user_1_email"]
        self.user_password = lines["test_user_1_password"]
        self.base_url = "https://qauto2.forstudy.space/api"

    def test_registration_success(self):
        """
        The method verifies the successful user login.
        :return: None
        """
        success_registration_test_data = {
            "name": "John",
            "lastName": "Dou",
            "email": self.user_mail,
            "password": self.user_password,
            "repeatPassword": self.user_password,
        }
        result = self.session.post(
            url=f"{self.base_url}/auth/signup", json=success_registration_test_data
        )
        assert result.json()["status"] == "ok"

    def test_user_profile(self):
        """
        The method verifies the happy pass for GET /users/profile
        :return: None
        """
        login_user = UserLoginModel(self.user_mail, self.user_password, False)

        self.session.post(url=f"{self.base_url}/auth/signin", json=login_user.__dict__)
        result = self.session.get(url=f"{self.base_url}/users/profile")

        assert result.json()["status"] == "ok"

    def teardown_class(self):
        """
        The method deletes user created during the test
        :return: None
        """
        login_user = UserLoginModel(self.user_mail, self.user_password, False)
        self.session.post(url=f"{self.base_url}/auth/signin", json=login_user.__dict__)

        self.session.delete(url=f"{self.base_url}/users")
