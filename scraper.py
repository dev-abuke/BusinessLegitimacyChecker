from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#make the driver headless
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
# TIN = "0007149558" #shamil
TIN = "0002493362" 
# Open the page
url = f"https://etrade.gov.et/business-license-checker?tin={TIN}"
driver.get(url)

# Wait for the page to load completely
driver.implicitly_wait(30) 
 # seconds

try:
    CurrentLanguage = driver.find_element(By.XPATH, '//app-lang-switcher/button//span/div/span').text
    print("Current Language is ::", CurrentLanguage)

    if(CurrentLanguage != "English"):
        ChangeLanguage = driver.find_element(By.XPATH, '//app-lang-switcher/button')
        ChangeLanguage.click()

        driver.implicitly_wait(1)

        LanguageDropDown = driver.find_element(By.ID, 'cdk-overlay-1').find_element(By.XPATH, '//div/div/button[2]')
        # LanguageDropDown.find_element(By.XPATH, '/div/button[2]').click()
        LanguageDropDown.click()

    driver.implicitly_wait(10)

    RegisteredNo = driver.find_element(By.XPATH, '//div/div/div/div/div/div/span').text
    print("Registered No ::", RegisteredNo)

    Tin = driver.find_element(By.XPATH, '//div/div/div/div/div/div[2]/span').text
    print("Tin No ::", Tin)

    BusinessPersonNameAmharic = driver.find_element(By.XPATH, '//div/div/div/div/div/div[3]/span').text
    print("Business / Person Name Amharic ::", BusinessPersonNameAmharic)

    # too large to show
    # OwnerImage = driver.find_element(By.XPATH, '//div/div/div[last()]/img').get_attribute('src')
    # print("Owner Image Url ::", OwnerImage)

    BusinessPersonNameEnglish = driver.find_element(By.XPATH, '//div/div/div/div/div/div[4]/span').text
    print("Business / Person Name English ::", BusinessPersonNameEnglish)

    LegalCondition = driver.find_element(By.XPATH, '//div/div/div/div/div/div[5]/p/span').text
    print("Legal Condition ::", LegalCondition)

    Capital = driver.find_element(By.XPATH, '//div/div/div/div/div/div[6]/span').text
    print("Capital ::", Capital)

    RegisteredDate = driver.find_element(By.XPATH, '//div/div/div/div/div/div[7]/span').text
    print("Registered Date ::", RegisteredDate)

    try:
        ViewMoreData = driver.find_element(By.XPATH, '//div/div/div/table/tbody/tr[1]/td[last()]/button')
        ViewMoreData.click()

        LicenseStatus = driver.find_element(By.XPATH, '//div/div/app-business-license/div/div/div/div[last() - 1]/span').text
        print("License Status is ::", LicenseStatus)
        
        ValidThrough = driver.find_element(By.XPATH, '//div/div/app-business-license/div/div/div/div[5]/span').text
        ValidThrough = ValidThrough.split(" - ")
        print(f"Valid From {ValidThrough[0]} To {ValidThrough[1]}")

        BusinessSector = driver.find_element(By.XPATH, '//div/div/app-business-license/div/div/div[last()]/mat-list/mat-list-item//span/p').text
        print("Business Sector is ::", BusinessSector)

        # Address
        Region = driver.find_element(By.XPATH, '//div/div/app-business-license/div/div/div[2]/div[1]/p[last()]').text
        print("Region is ::", Region)
        
        Zone = driver.find_element(By.XPATH, '//div/div/app-business-license/div/div/div[2]/div[2]/p[last()]').text
        print("Zone is ::", Zone)
        
        Woreda = driver.find_element(By.XPATH, '//div/div/app-business-license/div/div/div[2]/div[3]/p[last()]').text
        print("Woreda is ::", Woreda)
        
        Kebele = driver.find_element(By.XPATH, '//div/div/app-business-license/div/div/div[2]/div[4]/p[last()]').text
        print("Kebele is ::", Kebele)
        
        HouseNo = driver.find_element(By.XPATH, '//div/div/app-business-license/div/div/div[2]/div[5]/p[last()]').text
        print("House Number is ::", HouseNo)
        
        MobileNo = driver.find_element(By.XPATH, '//div/div/app-business-license/div/div/div[2]/div[6]/p[last()]').text
        print("Mobile Number is ::", MobileNo)
        
        RegularNo = driver.find_element(By.XPATH, '//div/div/app-business-license/div/div/div[2]/div[7]/p[last()]').text
        print("Regular Phone Number is ::", RegularNo)
    except Exception as e:
        SystemExit("View More Data is not available! ", e)
        # print("View More Data is not available! ", e)
except Exception as e:
    SystemExit("TIN Provided does not exist! ", e)

# Close the browser
driver.quit()