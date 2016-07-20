# -*- coding: utf-8 -*-
from model.contact import Contact
from selenium.webdriver.support.select import Select
import re
import random


class ContactHelper:

    contact_cache = None

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        self.app.navigation.go_to_home_page()
        # init contact creation
        self.app.wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.app.page.fill_field(name="firstname", value=contact.firstname)
        self.app.page.fill_field(name="middlename", value=contact.middlename)
        self.app.page.fill_field(name="lastname", value=contact.lastname)
        self.app.page.fill_field(name="nickname", value=contact.nickname)
        self.app.page.fill_field(name="title", value=contact.title)
        self.app.page.fill_field(name="company", value=contact.company)
        self.app.page.fill_field(name="address", value=contact.address1)
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
        self.app.navigation.go_to_home_page()
        self.contact_cache = None

    def create_with_add_group(self, contact, name_group):
        self.app.navigation.go_to_home_page()
        # init contact creation
        self.app.wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.app.page.fill_field(name="firstname", value=contact.firstname)
        self.app.page.fill_field(name="middlename", value=contact.middlename)
        self.app.page.fill_field(name="lastname", value=contact.lastname)
        self.app.page.fill_field(name="nickname", value=contact.nickname)
        self.app.page.fill_field(name="title", value=contact.title)
        self.app.page.fill_field(name="company", value=contact.company)
        self.app.page.fill_field(name="address", value=contact.address1)
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
        # choose group
        Select(self.app.wd.find_element_by_xpath("//select[@name='new_group']")).select_by_visible_text(name_group)
        # Enter contact creation
        self.app.wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.navigation.go_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_random_contact(0)

    def delete_random_contact(self, index):
        self.app.navigation.go_to_home_page()
        # select random contact
        self.app.wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input[@value='Delete']").click()
        # confirm deletion
        self.app.wd.switch_to_alert().accept()
        self.app.navigation.go_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        self.app.navigation.go_to_home_page()
        # select random contact
        self.app.wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # submit deletion
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input[@value='Delete']").click()
        # confirm deletion
        self.app.wd.switch_to_alert().accept()
        self.app.navigation.go_to_home_page()
        self.contact_cache = None

    def delete_contact_from_group(self, contact_id,  name_group):
        self.app.navigation.go_to_home_page()
        # choose group
        Select(self.app.wd.find_element_by_xpath("//select[@name='group']")).select_by_visible_text(name_group)
        # select random contact
        self.app.wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()
        # submit deletion
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[3]/input[@name='remove']").click()
        # confirm removing
        self.app.navigation.go_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_random_contact(0, contact)

    def edit_random_contact(self, index, contact):
        self.app.navigation.go_to_edit_contact_page_by_index(index)
        # fill group form
        self.app.page.fill_field(name="firstname", value=contact.firstname)
        self.app.page.fill_field(name="middlename", value=contact.middlename)
        self.app.page.fill_field(name="lastname", value=contact.lastname)
        self.app.page.fill_field(name="nickname", value=contact.nickname)
        self.app.page.fill_field(name="title", value=contact.title)
        self.app.page.fill_field(name="company", value=contact.company)
        self.app.page.fill_field(name="address", value=contact.address1)
        self.app.page.fill_field(name="home", value=contact.home_phone)
        self.app.page.fill_field(name="mobile", value=contact.mobile_phone)
        self.app.page.fill_field(name="work", value=contact.work_phone)
        self.app.page.fill_field(name="fax", value=contact.fax)
        self.app.page.fill_field(name="email", value=contact.email)
        self.app.page.fill_field(name="email2", value=contact.email2)
        self.app.page.fill_field(name="email3", value=contact.email3)
        self.app.page.fill_field(name="homepage", value=contact.homepage)
        self.app.page.fill_field(name="address2", value=contact.address2)
        self.app.page.fill_field(name="phone2", value=contact.phone2)
        self.app.page.fill_field(name="notes", value=contact.notes)
        # submit to update
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[1]/input[@name='update']").click()
        self.app.navigation.go_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, contact):
        self.app.navigation.go_to_edit_contact_page_by_id(contact.id)
        # fill group form
        self.app.page.fill_field(name="firstname", value=contact.firstname)
        self.app.page.fill_field(name="middlename", value=contact.middlename)
        self.app.page.fill_field(name="lastname", value=contact.lastname)
        self.app.page.fill_field(name="nickname", value=contact.nickname)
        self.app.page.fill_field(name="title", value=contact.title)
        self.app.page.fill_field(name="company", value=contact.company)
        self.app.page.fill_field(name="address", value=contact.address1)
        self.app.page.fill_field(name="home", value=contact.home_phone)
        self.app.page.fill_field(name="mobile", value=contact.mobile_phone)
        self.app.page.fill_field(name="work", value=contact.work_phone)
        self.app.page.fill_field(name="fax", value=contact.fax)
        self.app.page.fill_field(name="email", value=contact.email)
        self.app.page.fill_field(name="email2", value=contact.email2)
        self.app.page.fill_field(name="email3", value=contact.email3)
        self.app.page.fill_field(name="homepage", value=contact.homepage)
        self.app.page.fill_field(name="address2", value=contact.address2)
        self.app.page.fill_field(name="phone2", value=contact.phone2)
        self.app.page.fill_field(name="notes", value=contact.notes)
        # submit to update
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[1]/input[@name='update']").click()
        self.app.navigation.go_to_home_page()
        self.contact_cache = None

    def count(self):
        self.app.navigation.go_to_home_page()
        return len(self.app.wd.find_elements_by_name("selected[]"))

    def get_list_contacts(self):
        if self.contact_cache is None:
            self.app.navigation.go_to_home_page()
            self.contact_cache = []
            for element in self.app.wd.find_elements_by_css_selector("tr[name=entry]"):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text.encode('utf-8')
                firstname = cells[2].text.encode('utf-8')
                address1 = cells[3].text.encode('utf-8')
                all_emails = cells[4].text.encode('utf-8')
                all_phones = cells[5].text.encode('utf-8')
                id = element.find_element_by_name("selected[]").get_attribute("value").encode('utf-8')
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address1=address1, id=id,
                                                  all_phones=all_phones, all_emails=all_emails))
        return list(self.contact_cache)

    def get_contact_from_edit_page(self, index):
        self.app.navigation.go_to_edit_contact_page_by_index(index)
        id = self.app.wd.find_element_by_name("id").get_attribute("value")
        firstname = self.app.wd.find_element_by_name("firstname").get_attribute("value")
        lastname = self.app.wd.find_element_by_name("lastname").get_attribute("value")
        address1 = self.app.wd.find_element_by_name("address").get_attribute("value")
        email = self.app.wd.find_element_by_name("email").get_attribute("value")
        email2 = self.app.wd.find_element_by_name("email2").get_attribute("value")
        email3 = self.app.wd.find_element_by_name("email3").get_attribute("value")
        work_phone = self.app.wd.find_element_by_name("work").get_attribute("value")
        home_phone = self.app.wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = self.app.wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = self.app.wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(lastname=lastname, firstname=firstname, id=id, address1=address1, email=email, email2=email2,
                       email3=email3, home_phone=home_phone, work_phone=work_phone, mobile_phone=mobile_phone, phone2=phone2)

    def get_contact_from_view_page(self, index):
        self.app.navigation.go_to_view_contact_page(index)
        text = self.app.wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone, mobile_phone=mobile_phone, phone2=phone2)

    def merge_phones(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None, [contact.home_phone, contact.mobile_phone,
                                                                     contact.work_phone, contact.phone2]))))

    def merge_emails(self, contact):
        return "\n".join(filter(lambda x: x != "",
                            map(lambda x: self.clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))

    def clear(self, str):
        return re.sub("() -\s", "", str)

    def add_group(self, contact_id,  name_group):
        self.app.navigation.go_to_home_page()
        # select contact by id
        self.app.wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()
        # choose group by name
        Select(self.app.wd.find_element_by_xpath("//select[@name='to_group']")).select_by_visible_text(name_group)
        # submit add to group
        self.app.wd.find_element_by_xpath("//input[@name='add']").click()
        # confirm deletion
        self.app.navigation.go_to_home_page()
        self.contact_cache = None




