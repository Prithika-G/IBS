import time
from loginPage.LoginPage import LoginPage
from testcases.conftest import setup
from Utilities.CustomLogger import LogGen
from Utilities.ReadProperties import Readconfig
import pytest

class loginfunction:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()


    def login(self, setup):
        data = loginfunction.LaunchURL(self, setup)
        time.sleep(5)
        self.lp = LoginPage(data)
        self.logger.info("******* Enter the Username *******" + self.username)
        self.lp.setUserName(self.username)
        time.sleep(2)
        self.logger.info("******* Enter the Password *******" + self.password)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.logger.info("******* Click the Captcha checkbox *******")
        self.lp.clickCaptcha()
        time.sleep(2)
        self.logger.info("********** Click on Login button **************")
        self.lp.clickLogin()
        time.sleep(2)
        return data

    def LaunchURL(self, setup):
        self.logger.info("************ Launch the Browser **************")
        self.driver = setup
        self.driver.get(self.baseURL)

        return self.driver

