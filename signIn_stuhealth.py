#Before using this script,you need to ensure you have signed in stuhealth system at least 1 times.
#Because this script will not help you to full the content which should be cached at your data first time
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

#driver=webdriver.Chrome()   #Desktop Environment

noGUI=webdriver.ChromeOptions() #Headless
noGUI.add_argument("headless")
noGUI.add_argument("--no-sandbox")
driver=webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=noGUI)

driver.get("https://stuhealth.jnu.edu.cn/")
accountId=driver.find_element_by_id("zh")
accountId.send_keys("")   #Your Account ID
elem=driver.find_element_by_id("passw")
elem.send_keys("")      #Your password
clickYes=driver.find_element_by_tag_name("button")
clickYes.click()
time.sleep(10)

countryInOut=driver.find_element_by_xpath("//*[@class='form-group'][13]/div[1]/span[1]")
countryInOut.click()

addrProv=Select(driver.find_element_by_id("selectProvinceJtzz"))
addrProv.select_by_value("")     #Your Province ID

addrCity=Select(driver.find_element_by_id("selectCityJtzz"))
addrCity.select_by_value("")     #Your City ID

addrDistrict=Select(driver.find_element_by_id("selectDistrictJtzz"))
addrDistrict.select_by_value("") #Your District ID

driver.find_element_by_id('jtxxdz').send_keys("") #Your home location details

#Add Vaccine record.
vaccine=driver.find_element_by_xpath("//label[contains(text(), '新冠疫苗接种情况')]/../div[1]/span[1]")
vaccine.click()

checkReal=driver.find_element_by_id("10000")
checkReal.click()

submitHealth=driver.find_element_by_id("tj")
submitHealth.click()

time.sleep(8)

check=driver.find_element_by_tag_name("label")

with open("/usr/local/bin/JNUAutoSignInStuheal/logCheck",'a') as fLog:
    print(time.asctime(time.localtime()),check.text,file=fLog)

driver.quit()
