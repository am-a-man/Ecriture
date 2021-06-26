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






import time
import sys
import selenium 
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


time.sleep(10)
'============================================================================================================================================START'
print("till here")
'==============================================================================================================================================END'


driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME
    )

'============================================================================================================================================START'
print("till here 2")
'==============================================================================================================================================END'

search_url='https://careers.microsoft.com/students/us/en/search-results'
print("wow")
print("============================"+sys.argv[1]+"===========================")
print(search_url)
driver.get(search_url)
'============================================================================================================================================START'

print("till here 4")
print(driver.find_element_by_tag_name('body').text)

print("till here 3")

'==============================================================================================================================================END'

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
    file = open('./api_outlet/content.txt', 'w', encoding='utf-8')
#============================================================================================================================================START'
    print("check content start")
#==============================================================================================================================================END'
   
    for items in text:
        
#============================================================================================================================================START'
        print("loop start")
#==============================================================================================================================================END'

        header = items.find_element_by_css_selector("h2 a")
       
      
   

        title = header.find_element_by_tag_name('span').text
        link = header.get_attribute('href')

        file.write('=====================\n')
        file.write(title+'\n')
        file.write(link+'\n')

        driver2 = webdriver.Remote(
         command_executor='http://selenium:4444/wd/hub',
         desired_capabilities=DesiredCapabilities.CHROME
        )
        driver2.get(link)

#============================================================================================================================================START'
        print('================')
        print(title+'\n'+link+'\n')
#==============================================================================================================================================END'
        time.sleep(5)

        info = driver2.find_elements_by_xpath("//div[@class='job-description']/div[@class='jd-info']")

        responsibility = info[0]
        qualification = info[1]
        try:
            for i in responsibility.find_element_by_tag_name("h2").text:
                file.write(i)
            file.write('\n\n')
            
            for i in responsibility.find_element_by_tag_name("p").text:
                file.write(i)
            file.write('\n\n')

            for i in qualification.find_element_by_tag_name("h2").text:
                file.write(i)
            file.write('\n\n')

            for i in qualification.find_element_by_tag_name("p").text:
                file.write(i)
            file.write('\n\n')
        except Exception as e:
            print("error")
            print(e)
            return True
        print("writing into file.....")
        driver2.quit()


    file.close()
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



