from login_page import LoginPage
from navigation_bar_base_page import NavigationBar


class BaseFacade:
    def __init__(self):
        self.navigation_bar_base_page = NavigationBar()
        self.login_page = LoginPage()
