
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        self.app.navigation.go_to_page(page="groups")
        # init group creation
        self.app.wd.find_element_by_name("new").click()
        # fill group form
        self.app.page.fill_field(name="group_name", value=group.name)
        self.app.page.fill_field(name="group_header", value=group.header)
        self.app.page.fill_field(name="group_footer", value=group.footer)
        # submit group creation
        self.app.wd.find_element_by_name("submit").click()
        self.app.navigation.go_to_page(page="groups")

    def delete_first_group(self):
        self.app.navigation.go_to_page(page="groups")
        # select first group
        self.app.wd.find_element_by_name("selected[]").click()
        # submit deletion
        self.app.wd.find_element_by_name("delete").click()
        self.app.navigation.go_to_page(page="groups")


    def edit_first_group(self, group):
        self.app.navigation.go_to_page(page="groups")
        # select first group
        self.app.wd.find_element_by_name("selected[]").click()
        # submit to edit
        self.app.wd.find_element_by_name("edit").click()
        # fill group form
        self.app.page.fill_field(name="group_name", value=group.name)
        self.app.page.fill_field(name="group_header", value=group.header)
        self.app.page.fill_field(name="group_footer", value=group.footer)
        # submit to update
        self.app.wd.find_element_by_name("update").click()
        self.app.navigation.go_to_page(page="groups")



