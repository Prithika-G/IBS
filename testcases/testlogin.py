
import time
import pytest
from commonFunction.Login import loginfunction
from testcases.conftest import setup
from Utilities.ReadProperties import Readconfig
from Utilities.CustomLogger import LogGen
from selenium import webdriver


class Test_001_Login(loginfunction):
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        data = loginfunction.LaunchURL(self, setup)
        time.sleep(5)
        act_title = data.title
        time.sleep(3)

        if act_title == "Infoquick - Login":
            data.save_screenshot("/home/ticvictech/PycharmProjects/IBS/Screenshots" + "Pass_test_homepageTitle.png")
            assert True
            data.close()
            self.logger.info("*************Home Page Title verification is passed *************")
        else:
            data.save_screenshot("/home/ticvictech/PycharmProjects/IBS/Screenshots" + "Fail_test_homepageTitle.png")
            data.close()
            self.logger.info("********** Home Page Title verification is Failed***************")
            assert False

    def test_login(self, setup):
        data = loginfunction.login(self, setup)
        time.sleep(5)
        act_title = data.title
        print("act_title --", act_title)
        time.sleep(3)
        data.close()
        if act_title != "Infoquick - System Resources":
            self.logger.info("************** Login Page URL Title verification Passed***************")
            print("************** Login Page URL Title verification Passed***************")
            assert True
        else:
            self.logger.info("*************** Login Page Title verification ******************** ")
            print("*************** Login Page Title verification ******************** ")
            assert False
