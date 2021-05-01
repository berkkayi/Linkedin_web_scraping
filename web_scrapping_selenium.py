from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import json
import time


class Linkedin:
    def __init__(self,browser,url,email,password,search_pattern):
        self.browser = browser
        self.url = url
        self.email = email
        self.password = password
        self.search_pattern = search_pattern
    def login(self):
        self.browser.get(self.url)
        time.sleep(5)
        self.browser.maximize_window()
        self.browser.find_element_by_id('username').send_keys(self.email)
        time.sleep(2)
        self.browser.find_element_by_id('password').send_keys(self.password)
        time.sleep(2)
        self.browser.find_element_by_id('password').send_keys(Keys.RETURN)
        time.sleep(2)

    def search(self):
        time.sleep(5)
        try:
            self.browser.find_element_by_xpath('/html/body/div[8]/header/div[2]/div/div/div[1]/div[2]/input').send_keys(self.search_pattern)
            time.sleep(2)
            self.browser.find_element_by_xpath('/html/body/div[8]/header/div[2]/div/div/div[1]/div[2]/input').send_keys(Keys.RETURN)
        except:
            self.browser.find_element_by_xpath('/html/body/div[7]/header/div[2]/div/div/div[1]/div[2]/input').send_keys(self.search_pattern)
            time.sleep(2)
            self.browser.find_element_by_xpath('/html/body/div[7]/header/div[2]/div/div/div[1]/div[2]/input').send_keys(Keys.RETURN)
        time.sleep(2)
        time.sleep(2)
        time.sleep(5)
    def close(self):
        self.browser.close()
    def rolling_window(self,scroll_count):
        javascript = "window.scrollTo(0,1000)"
        for i in range(1, scroll_count):
            self.browser.execute_script(javascript)
        time.sleep(5)
    def scrapping_employee(self,seperator_str="\n\n\n"):
        followe_list = []
        follower = self.browser.find_elements_by_class_name('mb1')
        for i in follower:
            followe_list.append(i.text)
        with open("employees.txt", "w", encoding="utf-8") as file:
            file.write(seperator_str.join(bot.scrapping_employee()))
#ember671
'''try:

    #browser
    time.sleep(60)
    #for i in range(1, 3):
        #browser.execute_script("window.scrollTo(0,scrollHeight)")
    print("complated")
    time.sleep(5)
    browser.close()

except:
    browser.close()
pattern.find_element_by_xpath('//*[@id="global-nav-typeahead"]').click().send_keys(Keys.RETURN)
time.sleep(5)
pattern.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div/div[1]/main/div/div/div[1]/div/a').click()
#scroll command
time.sleep(3)
for i in range(1,3):
    browser.execute_script("window.scrollTo(0,scrollHeight)")'''

def main():
    with open("passwd.json","r") as f:
        passwd = json.load(f)
    with open("search_pattern.json") as f:
        search_pattern = json.load(f)

    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    url = "https://www.linkedin.com/login"
    email = passwd["email"]
    password = passwd["password"]
    search_pattern = search_pattern["search_pattern"]
    seperator_txt = "\n\n\n-------------------------"
    for pattern in search_pattern:
        bot = Linkedin(browser,url,email,password,pattern)
        bot.login()
        bot.search()
        bot.rolling_window(3)
        time.sleep(5)
        bot.scrapping_employee(seperator_txt)
        print(f" {pattern} complated !")
    bot.close()

if __name__ == '__main__':
    main()