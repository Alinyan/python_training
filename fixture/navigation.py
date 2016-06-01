
class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        self.app.wd.get("http://localhost/addressbook/")

    def go_to_page(self, page):
        self.app.wd.find_element_by_link_text(page).click()

