from pyvirtualdisplay import Display
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

n = []
c = []
present = []
with open('/home/gokul/Desktop/cred.txt') as input:
    for line in input:
        c.append(line.rstrip())
with open('/home/gokul/Desktop/attendancelog.txt') as input:
    for line in input:
        e = line.replace(" ", "")
        n.append(e.rstrip())
for i in c:
    o = i.split(" ; ")
    if o[0] in n:
        present.append(i)

for i in present:
    i = i.split(" ; ")
    email = (By.ID, "i0116")
    password = (By.ID, "i0118")
    next = (By.ID, "idSIButton9")
    button = (By.ID, "idSIButton9")
    signin = (By.NAME, "login")

    display = Display(visible=0, size=(800, 600)) # hides the browser (runs the process in the background)
    display.start()

    browser = webdriver.Chrome()
    browser.get('https://my.amrita.ac.in/index/index') # opens my amrita homepage

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(signin)).click() # waits for the submit button and clicks

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(email)).send_keys(i[1]) # wait for email field and enter email

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(next)).click() # click next

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(password)).send_keys(i[2]) # wait for password field and enter password

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(next)).click() # Click next

    browser.get('https://my.amrita.ac.in/index/index?key=585356-bfrth6gfv44k875-5jghtgf58ddfrtt&mode=in') # Once logged in opens AHMS homepage

    stayback = (By.XPATH, '//*[@id="content"]/div[2]/div/div/div[6]/div/h2/a') # clicks on the stayback option
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(stayback)).click()

    purpose = (By.XPATH, '//*[@id="normal_stayback"]/form/fieldset/section[1]/div/label[2]/i') # fills in the form
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

    submit = (By.ID, "stayback_normal_save") # clicks on the submit button
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(submit)).click()

    browser.__exit__() # exits the browser once the application is submitted
