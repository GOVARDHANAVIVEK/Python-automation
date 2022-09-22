from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "C:/Users/vivek/Documents/dev/chromedriver"

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.glassdoor.co.in/Salaries/index.htm")

#input for user
jobtitle = input("enter a job title?")

#optional
# joblocation = input("enter job location?")

selectjob = driver.find_element(By.ID,"KeywordSearch")
selectjob.send_keys(jobtitle)

searchjob = driver.find_element(By.ID,"HeroSearchButton")
searchjob.click()


from bs4 import BeautifulSoup
import requests

jobtitle = jobtitle.split(" ")
jobname = "-".join(jobtitle)
# print(jobname)

page =requests.get(f"https://www.glassdoor.co.in/Salaries/hyderabad-{jobname}-salary-SRCH_IL.0,9_IM1076_KO10,22.htm?clickSource=searchBtn")

soup = BeautifulSoup(page.content,"html.parser")
# print(soup.prettify())

jobpage = soup.find(class_="d-flex flex-column flex-lg-row")
# print(jobpage)


# comapany names
comapnynames = jobpage.find_all(name="a",class_="css-f3vw95 e1aj7ssy3")
companies = [company.text for company in comapnynames]
print(companies)


#jobrole
jobrole = jobpage.find_all(class_="col-12 col-lg px-xsm")
role =[role.getText() for role in jobrole]
# print(role)


#slaries
salarylist = jobpage.find_all(class_="d-flex align-items-baseline")
salaries=[]
for salary in salarylist:
    package= salary.text.split()
    salarypackage = " ".join(package)
    salaries.append(salarypackage)
print(salaries)


bot = webdriver.Chrome(executable_path=driver_path)
bot.get("https://forms.gle/ZNufptbc2hMbpqzc9")

for i in range(len(companies)):

    #comapny name in google sheet
    input1= bot.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input1.send_keys(companies[i])

    #role name in google sheet
    input2 = bot.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input2.send_keys(role[i])

    #salary in google sheet
    input3 = bot.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input3.send_keys(salaries[i])

    #submit button
    button = bot.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    button.click()

    #to submit another response
    respondagain = bot.find_element(By.CSS_SELECTOR,".c2gzEf a")
    respondagain.click()


#-----------------------------------------------------------------resources of this project----------------------------------------------------------#

# to view the webiste copy this link on new tab
# https://www.glassdoor.co.in/Salaries/index.htm and enter the job role you want to verify the responses.


#to view the google form copy this link in a new tab
#    https://forms.gle/ZNufptbc2hMbpqzc9


#to check the spreadsheet responses we made using automation
#copy this link in a new browser tab
#   https://docs.google.com/spreadsheets/d/1sGJEUsAxoOeJM2BildOB425O6glIZVtG21xcB2T4DfY/edit?usp=sharing


















