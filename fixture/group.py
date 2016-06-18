
from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        self.app.navigation.go_to_group_page()
        # init group creation
        self.app.wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        self.app.wd.find_element_by_name("submit").click()
        self.app.navigation.go_to_group_page()

    def delete_first_group(self):
        self.app.navigation.go_to_group_page()
        self.select_first_group()
        # submit deletion
        self.app.wd.find_element_by_name("delete").click()
        self.app.navigation.go_to_group_page()

    def edit_first_group(self, new_group_data):
        self.app.navigation.go_to_group_page()
        self.select_first_group()
        # open modification form
        self.app.wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        self.app.wd.find_element_by_name("update").click()
        self.app.navigation.go_to_group_page()

    def select_first_group(self):
        self.app.wd.find_element_by_name("selected[]").click()

    def fill_group_form(self, group):
        # fill group form
        self.app.page.fill_field(name="group_name", value=group.name)
        self.app.page.fill_field(name="group_header", value=group.header)
        self.app.page.fill_field(name="group_footer", value=group.footer)

    def count(self):
        self.app.navigation.go_to_group_page()
        return len(self.app.wd.find_elements_by_name("selected[]"))

    def get_list_groups(self):
        self.app.navigation.go_to_group_page()
        list_groups = []
        for element in self.app.wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            list_groups.append(Group(name=text, id=id))
        return list_groups



