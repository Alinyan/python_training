
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username="admin", password="secret"):
        self.app.navigation.open_start_page()
        # Input userName
        self.app.page.fill_field("user", username)
        # Input Password
        self.app.page.fill_field("pass", password)
        # Click submit
        self.app.wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.app.navigation.go_to_home_page()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()

    def is_logged_in(self):
        return len(self.app.wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        return self.app.wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+username+")"

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
