import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# my_url = 'https://www.youtube.com/playlist?list=PLwRS4M4qFRzL9R6T8qrW1XWEUejTRcD1b'



driver = webdriver.PhantomJS()
# driver = webdriver.Chrome()

driver.get('http://megavn.com/')

input_txt_element = driver.find_element_by_css_selector('input#txtLink')
input_txt_element.send_keys("https://www.youtube.com/playlist?list=PLwRS4M4qFRzL9R6T8qrW1XWEUejTRcD1b")

page_html = driver.page_source
page_soup = soup(page_html, "lxml")


time.sleep(20)
links = []
links = driver.find_element_by_css_selector("table#ListVideo>tbody>tr>td")
# print(links[0])
# print(links.get_attribute("href"))
# for link in links: 
#url = links[0]

# print(links[0])
# print(link.get_attribute("href"))

# ListlinkerHref = driver.find_element_by_css_selector("table#ListVideo>tbody>tr>td>a")# print("URL: " + ListlinkerHref)

#for container in containers: 
#url_containers = soup.select("table#ListVideo>tbody>tr>td>a")
# print("URL: " + url_containers)


for row in driver.find_elements_by_css_selector("table#ListVideo>tbody>tr"):
	cell = row.find_elements_by_tag_name("td")[1]# 
	print(cell.text)
	link = cell.find_element_by_css_selector("a").get_attribute("href")
	print(link)
	driver.find_element_by_css_selector("span#next").click() 
	driver.find_elements_by_xpath("//*[@id='next']/a").click()
time.sleep(5)

#xpath : 