from selenium import webdriver
from time import sleep


class BadooBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self,username,pw):
        self.driver.get("https://badoo.com/signin/")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/section/div/div/div[1]/form/div[1]/div[2]/div/input") \
            .send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/section/div/div/div[1]/form/div[2]/div[2]/div/input") \
            .send_keys(pw)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/section/div/div/div[1]/form/div[5]/div/div[1]/button') \
            .click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')
        like_btn.click()


    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div/section/div/div/div/div[1]/div')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = BadooBot()
bot.login("mailadresshere", pw="passwordhere")
sleep(6)
bot.auto_swipe()