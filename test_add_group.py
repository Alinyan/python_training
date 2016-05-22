# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from common import Common

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.common = Common()
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        wd = self.wd
        common = self.common
        common.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="Name_of_group", header="Header_of_group", footer="Footer_of_group"))
        common.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        common = self.common
        common.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="", header="", footer=""))
        common.logout(wd)

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        self.open_groups_page(wd)
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page(wd)

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
