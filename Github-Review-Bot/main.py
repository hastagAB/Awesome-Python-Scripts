# Python Script to review all the pull request of mentioned repository

from selenium.webdriver import Firefox, ActionChains
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.common.keys import Keys

username = None
password = None

class Github:

    def __init__(self, repo_owner, repo_name):
        self.base_url = "https://github.com/"
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.isLogin = False
        self.driver = Firefox()
        self.pull_requests = None

    def login(self):
        self.driver.get(self.base_url+"/login")
        self.driver.find_element(by=By.ID, value="login_field").send_keys(username)
        self.driver.find_element(by=By.ID, value="password").send_keys(password)
        self.driver.find_element(by=By.NAME, value="commit").click()
        self.isLogin = True
    
    def writeReview(self):
        if not self.isLogin:
            self.login()

        self.driver.get(self.base_url+self.repo_owner+"/"+self.repo_name+"/pulls")
        self.driver.implicitly_wait(10)
        pull_requests = self.driver.find_elements(by=By.XPATH, value="//a[@data-hovercard-type='pull_request']")
        self.pull_requests = [pull_request.get_attribute("href") for pull_request in pull_requests]

        for pull_request in self.pull_requests:
            self.driver.get(pull_request+"/files")
            self.driver.implicitly_wait(10)
            self.driver.find_element(by=By.ID, value="review-changes-modal").click()
            self.driver.implicitly_wait(10)
            self.driver.find_element(by=By.ID, value="pull_request_review[event]_approve").click()
            self.driver.implicitly_wait(10)
            self.driver.find_element(by=By.ID, value="pull_request_review_body").send_keys(random.choice(["LGTM", "Looks good to me", "LGTM, thanks for the contribution", "Seems good to me!"]))
            self.driver.implicitly_wait(10)
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
            self.driver.implicitly_wait(10)


if __name__ == "__main__":
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    github_owner = input("Enter the repository owner: ")
    github_repo = input("Enter the repository name: ")
    github = Github(github_owner, github_repo)
    github.writeReview()