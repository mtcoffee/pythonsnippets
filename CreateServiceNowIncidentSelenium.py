#variables
import sys
if len(sys.argv) < 4:
	warning = """
	Please provide 3 parameters in the format instancename, user, password
	e.g. dev1234 itiluser itiluserpassword
	"""
	print(warning)
	sys.exit()

sninstance = "https://" + sys.argv[1] + ".service-now.com"
sninstanceuser = sys.argv[2]
sninstancepwd = sys.argv[3]

#selenium setup
print('start of login')
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

#chrome setup
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
import time
browser = webdriver.Chrome(options=chrome_options)
browser.get(str(sninstance) + "/login.do")
time.sleep(5)

#login to ServiceNow Instnace
username = browser.find_element(By.ID, "user_name")
password = browser.find_element(By.ID, "user_password")
username.send_keys(str(sninstanceuser))
password.send_keys(str(sninstancepwd))
login_attempt = browser.find_element(By.ID, "sysverb_login")
login_attempt.click()
print('end of login')

#confirm login
time.sleep(5)
#move to new incident page
browser.get(str(sninstance) + "/incident.do")
print('current url after login is ' + browser.current_url)
expected = 'incident.do'
print('expected url after login is ' + expected)
if expected in browser.current_url:
    print ('login success!')
else:
    print ('could not access incident page, check login details')
    exit(1)
print('end of login')

#create incident
print('logged in, now creating incident')
time.sleep(5)
browser.get(str(sninstance) + "/incident.do")
assignmentGroup = browser.find_element(By.ID,"sys_display.incident.assignment_group")
assignmentGroup.send_keys('Help Desk',Keys.RETURN)
callerId = browser.find_element(By.ID,"sys_display.incident.caller_id")
callerId.send_keys('Abel Tuter',Keys.RETURN)
contactType = Select(browser.find_element(By.ID,"incident.contact_type"))
contactType.select_by_visible_text('Walk-in')
shortDescription = browser.find_element(By.ID, "incident.short_description")
shortDescription.send_keys("Testing Incident creation with Selenium")
numberField = browser.find_element(By.ID, "incident.number")
number = numberField.get_attribute('value')
browser.find_element(By.ID, "sysverb_insert").click() #insert record

print('Completed incident creation for ' + number )
