from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
      

PATH = r"C:\Users\andre\Documents\Python_Scripts\Hackathon\chromedriver.exe"
print(PATH)
driver = webdriver.Chrome(PATH)

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

driver.get(r"https://www.glassdoor.com/Job/software-engineer-intern-jobs-SRCH_KO0,24.htm")
time.sleep(10)
driver.find_element_by_xpath("//*[@id=\"MainCol\"]/div[1]/ul/li[1]").click()
time.sleep(5)
companyNames = []
jobNames = []
locations = []
ratings = []
pays = []
for j in range(0,27):
    time.sleep(2)
    companyName = driver.find_element_by_xpath("//*[@id=\"MainCol\"]/div[1]/ul/li[1]/div[2]/div[1]").text
    jobName = driver.find_element_by_xpath("//*[@id=\"MainCol\"]/div[1]/ul/li[1]/div[2]/a").text
    location = driver.find_element_by_xpath("//*[@id=\"MainCol\"]/div[1]/ul/li[1]/div[2]/div[2]/span").text
    
    if check_exists_by_xpath("//*[@id=\"MainCol\"]/div[1]/ul/li[1]/div[1]/span"):
        rating = driver.find_element_by_xpath("//*[@id=\"MainCol\"]/div[1]/ul/li[1]/div[1]/span").text
    else:
        rating = "N/A"
        
    if check_exists_by_xpath(f"//*[@id=\"MainCol\"]/div[1]/ul/li[{1}]/div[2]/div[3]/div[1]/span"):
        pay = driver.find_element_by_xpath("//*[@id=\"MainCol\"]/div[1]/ul/li[1]/div[2]/div[3]/div[1]/span").text
    else:
        pay = "N/A"
        
    companyNames.append(companyName)
    jobNames.append(jobName)
    locations.append(location)
    ratings.append(rating)
    pays.append(pay)
    for i in range(2,31):
        #driver.find_element_by_xpath(f"//*[@id=\"MainCol\"]/div[1]/ul/li[{i}]").click()
        companyName = driver.find_element_by_xpath(f"//*[@id=\"MainCol\"]/div[1]/ul/li[{i}]/div[2]/div[1]").text
        jobName = driver.find_element_by_xpath(f"//*[@id=\"MainCol\"]/div[1]/ul/li[{i}]/div[2]/a").text
        location = driver.find_element_by_xpath(f"//*[@id=\"MainCol\"]/div[1]/ul/li[{i}]/div[2]/div[2]/span").text
        if check_exists_by_xpath(f"//*[@id=\"MainCol\"]/div[1]/ul/li[{i}]/div[1]/span"):
            rating = driver.find_element_by_xpath(f"//*[@id=\"MainCol\"]/div[1]/ul/li[{i}]/div[1]/span").text
        else:
            rating = "N/A"
        if check_exists_by_xpath(f"//*[@id=\"MainCol\"]/div[1]/ul/li[{i}]/div[2]/div[3]/div[1]/span"):
            pay = driver.find_element_by_xpath(f"//*[@id=\"MainCol\"]/div[1]/ul/li[{i}]/div[2]/div[3]/div[1]/span").text
        else:
            pay = "N/A"
        companyNames.append(companyName)
        jobNames.append(jobName)
        locations.append(location)
        ratings.append(rating)
        pays.append(pay)
    driver.find_element_by_xpath("//*[@id=\"FooterPageNav\"]/div/ul/li[7]/a").click()

df = pd.DataFrame({
    'Company Name': companyNames,
    'Job Name': jobNames,
    'Location': locations,
    'Rating': ratings,
    'Pay': pays
    })

df.to_csv("temp.csv")
print(df.head())
driver.quit()