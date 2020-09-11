from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time


class Boottems:
    def __init__(self,username,pasword):
        self.username = username
        self.pasword=pasword
        self.driver = webdriver.Firefox()
    def login(self):
        driver = self.driver
        driver.get("https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=0ac981d8-3927-4153-901b-e80c0bbfb5ec&&client-request-id=37da9ce5-acc2-4db5-b4f1-8dfdb5141e7f&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=c574d8f1-f4f6-4d4d-8298-6707493ed2cd&domain_hint=")
        email=driver.find_element_by_xpath('//*[@id="i0116"]');email.click()
        email.send_keys(self.username)
        entrar=driver.find_element_by_xpath('//*[@id="idSIButton9"]');entrar.click()
        time.sleep(10)
        senha=driver.find_element_by_xpath('//*[@id="passwordInput"]');senha.click()
        senha.send_keys(self.pasword)
        logar=driver.find_element_by_xpath('//*[@id="submitButton"]');logar.click()
        time.sleep(10)
        select=driver.find_element_by_xpath('//*[@id="idSIButton9"]');select.click()
        time.sleep(10)
        acess=driver.find_element_by_class_name('use-app-lnk');acess.click()
    def disparar(self):
        pass
        # parei aqui #

