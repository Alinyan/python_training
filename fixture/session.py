
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username="admin", password="secret"):
        self.app.navigation.open_home_page()
        # Input userName
        self.app.wd.find_element_by_name("user").click()
        self.app.wd.find_element_by_name("user").clear()
        self.app.wd.find_element_by_name("user").send_keys(username)
        # Input Password
        self.app.wd.find_element_by_name("pass").click()
        self.app.wd.find_element_by_name("pass").clear()
        self.app.wd.find_element_by_name("pass").send_keys(password)
        # Click submit
        self.app.wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.app.navigation.go_to_page(page="home")

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()