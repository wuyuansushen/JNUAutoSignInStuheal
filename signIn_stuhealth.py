#Before using this script,you need to ensure you have signed in stuhealth system at least 1 times.
#Because this script will not help you to full the content which should be cached at your data first time
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

def setAddressID(broser,elementID,addressID):
    addr=Select(broser.find_element_by_id(elementID))
    addr.select_by_value(addressID)
    return

#driver=webdriver.Chrome()   #Desktop Environment

noGUI=webdriver.ChromeOptions() #Headless
noGUI.add_argument("headless")
noGUI.add_argument("--no-sandbox")
driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=noGUI)

driver.get("https://stuhealth.jnu.edu.cn/")
accountId=driver.find_element_by_id("zh")
accountId.send_keys(" ")   #Your Account ID
elem=driver.find_element_by_id("passw")
elem.send_keys(" ")      #Your password
clickYes=driver.find_element_by_tag_name("button")
clickYes.click()
time.sleep(4)

setAddressID(driver,"selectProvince"," ") #Your Province ID

setAddressID(driver,"selectCity"," ")  #Your City ID

setAddressID(driver,"selectDistrict"," ")  #Your District ID

checkReal=driver.find_element_by_id("10000")
checkReal.click()

submitHealth=driver.find_element_by_id("tj")
submitHealth.click()

time.sleep(4)

check=driver.find_element_by_tag_name("label")

with open("/usr/local/bin/JNUAutoSignInStuheal/logCheck",'a') as fLog:
    print(time.asctime(time.localtime()),check.text,file=fLog)

driver.close()
