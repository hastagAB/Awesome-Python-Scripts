from selenium import webdriver
import getpass
import time

username = "username"
password = getpass.getpass("Password:")

problem = 'TEST'

code = """
#include <iostream>
 
int main(void) {
char c, d=10;
while(std::cin.get(c) && (c!='2' || d!='4') && std::cout.put(d))
d=c;
} 
"""

browser = webdriver.Firefox()

browser.get('https://www.codechef.com')

nameElem = browser.find_element_by_id('edit-name')
nameElem.send_keys(username)

passElem = browser.find_element_by_id('edit-pass')
passElem.send_keys(password)

browser.find_element_by_id('edit-submit').click()

browser.get("https://www.codechef.com/submit/" + problem)

time.sleep(20)

browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

inputElem = browser.find_element_by_id('edit-program')
inputElem.send_keys(code)

browser.find_element_by_id("edit-submit").click()

