import time, pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://mail.ru')
cookies = pickle.load(open("cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(2)
driver.get("https://auth.mail.ru/cgi-bin/secstep?send_sms=1")

time.sleep(2)
auth_code = str(input('input auth code: '))
driver.find_element_by_name('AuthCode').send_keys(auth_code)
driver.find_element_by_xpath("//button[@data-name='user-login']").click()