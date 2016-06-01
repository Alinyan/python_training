
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username="admin", password="secret"):
        self.app.navigation.open_home_page()
        # Input userName
        self.app.page.fill_field("user", username)
        # Input Password
        self.app.page.fill_field("pass", password)
        # Click submit
        self.app.wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.app.navigation.go_to_page("home")

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()
