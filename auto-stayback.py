from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")
button = (By.ID, "idSIButton9")
submit = (By.NAME, "login")

browser = webdriver.Chrome()
browser.get('https://my.amrita.ac.in/index/index')

WebDriverWait(browser, 10).until(EC.element_to_be_clickable(submit)).click()

# wait for email field and enter email
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys("your username")

# Click Next
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

# wait for password field and enter password
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys("your password")

# Click Login - same id?
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(button)).click()

browser.get('https://my.amrita.ac.in/index/index?key=585356-bfrth6gfv44k875-5jghtgf58ddfrtt&mode=in')

stayback = (By.XPATH, '//*[@id="content"]/div[2]/div/div/div[6]/div/h2/a')
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(stayback)).click()

purpose = (By.XPATH, '//*[@id="normal_stayback"]/form/fieldset/section[1]/div/label[2]/i')
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(purpose)).click()

approval_from = (By.XPATH, '//*[@id="staff_id"]/option[1108]')
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(approval_from)).click()

date = (By.NAME, "stayback_date")
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(date)).send_keys(datetime.today().strftime('%Y-%m-%d'))

lt = (By.ID, "clockpicker1")
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(lt)).send_keys("10:30")

at = (By.ID, "clockpicker2")
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(at)).send_keys("11:00")

reason = (By.NAME, "reason")
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(reason)).click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(reason)).send_keys("amfoss")

submit = (By.ID, "stayback_normal_save")
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(submit)).click()

#browser.__exit__()
