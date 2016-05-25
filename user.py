from selenium.webdriver.firefox.webdriver import WebDriver

class User():

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def login(self, username="admin", password="secret"):
        self.open_home_page()
        # Input userName
        self.wd.find_element_by_name("user").click()
        self.wd.find_element_by_name("user").clear()
        self.wd.find_element_by_name("user").send_keys(username)
        # Input Password
        self.wd.find_element_by_name("pass").click()
        self.wd.find_element_by_name("pass").clear()
        self.wd.find_element_by_name("pass").send_keys(password)
        # Click submit
        self.wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.go_to_page(page="home")

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/")

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()

    def go_to_page(self, page):
        self.wd.find_element_by_link_text(page).click()

    def create_group(self, group):
        self.go_to_page(page="groups")
        # init group creation
        self.wd.find_element_by_name("new").click()
        # fill group form
        self.wd.find_element_by_name("group_name").click()
        self.wd.find_element_by_name("group_name").clear()
        self.wd.find_element_by_name("group_name").send_keys(group.name)
        self.wd.find_element_by_name("group_header").click()
        self.wd.find_element_by_name("group_header").clear()
        self.wd.find_element_by_name("group_header").send_keys(group.header)
        self.wd.find_element_by_name("group_footer").click()
        self.wd.find_element_by_name("group_footer").clear()
        self.wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        self.wd.find_element_by_name("submit").click()
        self.go_to_page(page="group page")

    def create_contact(self, contact):
        # init contact creation
        self.go_to_page(page="add new")
        # fill contact form
        self.wd.find_element_by_name("firstname").click()
        self.wd.find_element_by_name("firstname").clear()
        self.wd.find_element_by_name("firstname").send_keys(contact.firstname)
        self.wd.find_element_by_name("middlename").click()
        self.wd.find_element_by_name("middlename").clear()
        self.wd.find_element_by_name("middlename").send_keys(contact.middlename)
        self.wd.find_element_by_name("lastname").click()
        self.wd.find_element_by_name("lastname").clear()
        self.wd.find_element_by_name("lastname").send_keys(contact.lastname)
        self.wd.find_element_by_name("nickname").click()
        self.wd.find_element_by_name("nickname").clear()
        self.wd.find_element_by_name("nickname").send_keys(contact.nickname)
        self.wd.find_element_by_name("title").click()
        self.wd.find_element_by_name("title").clear()
        self.wd.find_element_by_name("title").send_keys(contact.title)
        self.wd.find_element_by_name("company").click()
        self.wd.find_element_by_name("company").clear()
        self.wd.find_element_by_name("company").send_keys(contact.company)
        self.wd.find_element_by_name("address").click()
        self.wd.find_element_by_name("address").clear()
        self.wd.find_element_by_name("address").send_keys(contact.address_company)
        self.wd.find_element_by_name("home").click()
        self.wd.find_element_by_name("home").clear()
        self.wd.find_element_by_name("home").send_keys(contact.home_phone)
        self.wd.find_element_by_name("mobile").click()
        self.wd.find_element_by_name("mobile").clear()
        self.wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        self.wd.find_element_by_name("work").click()
        self.wd.find_element_by_name("work").clear()
        self.wd.find_element_by_name("work").send_keys(contact.work_phone)
        self.wd.find_element_by_name("fax").click()
        self.wd.find_element_by_name("fax").clear()
        self.wd.find_element_by_name("fax").send_keys(contact.fax)
        self.wd.find_element_by_name("email2").click()
        self.wd.find_element_by_name("email2").clear()
        self.wd.find_element_by_name("email2").send_keys(contact.email2)
        self.wd.find_element_by_name("email3").click()
        self.wd.find_element_by_name("email3").clear()
        self.wd.find_element_by_name("email3").send_keys(contact.email3)
        self.wd.find_element_by_name("homepage").click()
        self.wd.find_element_by_name("homepage").clear()
        self.wd.find_element_by_name("homepage").send_keys(contact.homepage)
        self.wd.find_element_by_name("address2").click()
        self.wd.find_element_by_name("address2").clear()
        self.wd.find_element_by_name("address2").send_keys(contact.address2)
        self.wd.find_element_by_name("phone2").click()
        self.wd.find_element_by_name("phone2").clear()
        self.wd.find_element_by_name("phone2").send_keys(contact.phone2)
        self.wd.find_element_by_name("notes").click()
        self.wd.find_element_by_name("notes").clear()
        self.wd.find_element_by_name("notes").send_keys(contact.notes)
        # Enter contact creation
        self.wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.go_to_page(page="home")

    def destroy(self):
        self.wd.quit()

