
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        # init contact creation
        self.app.navigation.go_to_page("add new")
        # fill contact form
        self.app.page.fill_field(name="firstname", value=contact.firstname)
        self.app.page.fill_field(name="middlename", value=contact.middlename)
        self.app.page.fill_field(name="lastname", value=contact.lastname)
        self.app.page.fill_field(name="nickname", value=contact.nickname)
        self.app.page.fill_field(name="title", value=contact.title)
        self.app.page.fill_field(name="company", value=contact.company)
        self.app.page.fill_field(name="address", value=contact.address_company)
        self.app.page.fill_field(name="home", value=contact.home_phone)
        self.app.page.fill_field(name="mobile", value=contact.mobile_phone)
        self.app.page.fill_field(name="work", value=contact.work_phone)
        self.app.page.fill_field(name="fax", value=contact.fax)
        self.app.page.fill_field(name="email2", value=contact.email2)
        self.app.page.fill_field(name="email3", value=contact.email3)
        self.app.page.fill_field(name="homepage", value=contact.homepage)
        self.app.page.fill_field(name="address2", value=contact.address2)
        self.app.page.fill_field(name="phone2", value=contact.phone2)
        self.app.page.fill_field(name="notes", value=contact.notes)
        # Enter contact creation
        self.app.wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.navigation.go_to_page("home page")

    def delete_first_contact(self):
        self.app.navigation.go_to_page("home")
        # select first contact
        self.app.wd.find_element_by_name("selected[]").click()
        # submit deletion
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input[@value='Delete']").click()
        # confirm deletion
        self.app.wd.switch_to_alert().accept()
        self.app.navigation.go_to_page("home")

    def edit_first_contact(self, contact):
        self.app.navigation.go_to_page("home")
        # select first group
        self.app.wd.find_element_by_name("selected[]").click()
        # submit to edit
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/table/tbody/tr[2]/td[8]/a/img").click()
        # fill group form
        self.app.page.fill_field(name="firstname", value=contact.firstname)
        self.app.page.fill_field(name="middlename", value=contact.middlename)
        self.app.page.fill_field(name="lastname", value=contact.lastname)
        self.app.page.fill_field(name="nickname", value=contact.nickname)
        self.app.page.fill_field(name="title", value=contact.title)
        self.app.page.fill_field(name="company", value=contact.company)
        self.app.page.fill_field(name="address", value=contact.address_company)
        self.app.page.fill_field(name="home", value=contact.home_phone)
        self.app.page.fill_field(name="mobile", value=contact.mobile_phone)
        self.app.page.fill_field(name="work", value=contact.work_phone)
        self.app.page.fill_field(name="fax", value=contact.fax)
        self.app.page.fill_field(name="email2", value=contact.email2)
        self.app.page.fill_field(name="email3", value=contact.email3)
        self.app.page.fill_field(name="homepage", value=contact.homepage)
        self.app.page.fill_field(name="address2", value=contact.address2)
        self.app.page.fill_field(name="phone2", value=contact.phone2)
        self.app.page.fill_field(name="notes", value=contact.notes)
        # submit to update
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[1]/input[@name='update']").click()
        self.app.navigation.go_to_page(page="home")

    def count(self):
        self.app.navigation.go_to_page("home")
        return len(self.app.wd.find_elements_by_name("selected[]"))
