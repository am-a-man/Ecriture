#type:ignore


#start 
# import selenium 
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# driver = webdriver.Remote(
#     'http://selenium:4444/wd/hub',
#     desired_capabilities = DesiredCapabilities.CHROME
# )

# driver.get("https://python.org")
# print(driver.find_element_by_tag_name('body').text)

# end




import json

import time
import sys
import selenium 
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
print("--------------------------------------------------------")

time.sleep(10)

driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME
    )



search_url='https://careers.microsoft.com/students/us/en/search-results'

try:
    print("============================"+sys.argv[1]+"===========================")
except Exception as e:
    None


print(search_url)
driver.get(search_url)
name = "microsoft"

# opening json and retreiving data


with open("./api_outlet/content.json","r",encoding='utf-8') as jsonData:
    details = json.load(jsonData)
details[name] = {"url":search_url, "jobs":{}}


def openOptions(driver):
    try:
        driver.find_element_by_xpath("//button[@aria-label='toggle refine search']").click()
        return True
    except:
        print("check openOptions")
        return True

def dropDown(driver):
    try:
        driver.find_element_by_xpath("//button[@aria-label='Country/Region']").click()
        return True
    except:
        WebDriverWait(driver, timeout = 10).until(openOptions)

def setCountry(driver):
    try:
       
        driver.find_element_by_xpath("//label[input/@data-ph-at-text='India']").click()
       
        return True
    except:
        WebDriverWait(driver, timeout=10).until(dropDown)
        setCountry(driver)


def checkContent(driver):
    

    text = driver.find_elements_by_xpath("//ul[@data-ph-at-id='jobs-list']/li")

    

    for items in text:
        header = items.find_element_by_css_selector("h2 a")
        title = header.find_element_by_tag_name('span').text
        link = header.get_attribute('href')

        try:
            #file.write(title+'\n')
           
            titleCache = title
            i = 1
            while(title in details[name]["jobs"].keys()):
                title = titleCache + ' ' +str(i)
                i+=1


            details[name]["jobs"][title]={"url":link}
            #file.write(link+'\n')

            driver2 = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
            )
            driver2.get(link)


            time.sleep(3)

            info = driver2.find_elements_by_xpath("//div[@class='job-description']/div[@class='jd-info']")

            responsibility = info[0].find_element_by_tag_name("p").text
            qualification = info[1].find_element_by_tag_name("p").text
            print(f"=========================================={title}==========================")

            responsibilityText = ''
            qualificationText = ''    
            for i in responsibility:
                responsibilityText+=i
            for i in qualification:
                qualificationText+=i
            details[name]["jobs"][title]["responsibility"] = responsibilityText
            details[name]["jobs"][title]["qualifications"] = qualificationText
                
        except Exception as e:
            print("error")
            print(e)
            driver2.quit()
            return True
        print("writing into file.....")
        driver2.quit()
    try:
        print(details)
        jsondata = json.dumps(details, indent=4)
        with open("./api_outlet/content.json", 'w', encoding="utf-8") as outfile:
            outfile.write(jsondata)
        print("done")
    except Exception as e:
        print(e)
    return True



def getList(driver):
    try:
        setCountry(driver)
        time.sleep(3)
        checkContent(driver)
        return True
    except KeyboardInterrupt:
        driver.quit()
        exit()
    except:
        getList(driver)


print("wait...")
getList(driver)
driver.quit()



