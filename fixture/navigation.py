
class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_start_page(self):
        self.app.wd.get("http://localhost/addressbook/")

    def go_to_home_page(self):
        if not (len(self.app.wd.find_elements_by_name("MainForm")) > 0):
            self.app.wd.find_element_by_link_text("home").click()

    def go_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("group.php") and len(wd.find_elements_by_name("new")) > 0):
            self.app.wd.find_element_by_link_text("groups").click()
