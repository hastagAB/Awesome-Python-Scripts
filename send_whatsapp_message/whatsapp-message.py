from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
a=1
while a!=0:
    input('Scan QR code first and hit enter')
    name = input('Enter the name of user or group : ')
    msg = input('Enter your message : ')
    count = int(input('Enter the count : '))
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name('_3u328')
    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
    a=int(input("Wanna text any other guy?(0/1):"))
if a==0:
    print("Bye!\nSee you soon.")
