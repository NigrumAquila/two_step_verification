import time, pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://mail.ru/')

username = 'mmmail@bk.ru'
driver.find_element_by_name('login').send_keys(username)
driver.find_element_by_id('auth').click()

time.sleep(1)
password = 'pass'
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_id('auth').click()

time.sleep(3)
driver.find_element_by_xpath("//button[@type='button']").click()

time.sleep(3)
pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))
driver.close()


# auth_code = str(input('input auth code: '))
# driver.find_element_by_name('AuthCode').send_keys(auth_code)
# driver.find_element_by_xpath("//button[@data-name='user-login']").click()



