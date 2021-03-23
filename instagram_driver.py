import time
from selenium import webdriver
from instascrape import Profile


class InstagramDriver():
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.driver = self.get_webdriver()
        self._retrieve_cookies()
        self.complete_login()

    def get_all_followers(self):
        followers = {}
        self.driver.get('https://www.instagram.com/imperiumpiekna_atelier/')
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        ).click()
        time.sleep(2)

        divs = self.driver.find_elements_by_tag_name("div")
        follower_dialog = list(
            filter(lambda elem: elem.get_attribute("role") == "dialog",
                   divs))[0]
        follower_list = follower_dialog.find_elements_by_tag_name("li")

        for follower in follower_list:
            buttons = follower.find_elements_by_tag_name("button")
            remove_button = list(
                filter(lambda elem: elem.text == "Remove", buttons))[0]
            username = follower.find_elements_by_tag_name('span')
            username = list(filter(lambda elem: len(elem.text) > 0,
                                   username))[0]
            followers[username.text] = remove_button

        return followers

    def scrape_users(self, usernames: list):
        users = []
        for username in usernames:
            profile = Profile(username)
            profile.scrape(headers=self.headers, webdriver=self.driver)
            users.append(profile)
        return users

    def get_webdriver(self):
        self.driver = webdriver.Chrome("/Users/ihologa/Documents/chromedriver")
        self.driver.get('http://www.instagram.com/')
        time.sleep(2)
        return self.driver

    def accept_cockies(self):
        cockies_prompt_accept = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/button[1]")
        cockies_prompt_accept.click()

    def log_in(self):
        login_form = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        login_form.send_keys(self.username)
        login_form2 = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_form2.send_keys(self.password)
        log_in_button = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button')
        log_in_button.click()

    def remember_login(self, on=True):
        time.sleep(3)
        all_buttons = self.driver.find_elements_by_tag_name("button")
        if on:
            button = list(
                filter(lambda elem: elem.text == "Save Info", all_buttons))[0]
        else:
            button = list(
                filter(lambda elem: elem.text == "Not Now", all_buttons))[0]
        button.click()

    def set_notifications(self, on=False):
        time.sleep(3)
        all_buttons = self.driver.find_elements_by_tag_name("button")
        if on:
            button = list(
                filter(lambda elem: elem.text == "Turn On", all_buttons))[0]
        else:
            button = list(
                filter(lambda elem: elem.text == "Not Now", all_buttons))[0]
        button.click()

    def complete_login(self):
        self.accept_cockies()
        self.log_in()
        self.remember_login(on=True)
        self.set_notifications(on=False)

    def _retrieve_cookies(self):
        all_cookies = self.driver.get_cookies()
        session_id = list(
            filter(lambda cookie: cookie["name"] == "sessionid",
                   all_cookies))[0]
        self.headers = {
            "user-agent":
            "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
            "cookie": f"sessionid={session_id.value};"
        }

    def close(self):
        self.driver.quit()
