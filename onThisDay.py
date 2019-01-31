#onThisDay

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request

my_url="https://www.onthisday.com/birthdays/"

months=["January","February","March","June","July","August","September","October","November", "December"]

print("Enter month")
m= input()
print("Enter date")
d= input()

my_url+=m+"/"+d

hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(my_url,headers=hdr)
page = urlopen(req)
page_soup = soup(page, "html.parser")

print(page_soup.title)

containers = page_soup.findAll("div", {"class": "section section--highlight section--person-of-interest"})
print(len(containers))

for container in containers:
    data=container.findAll("div", {"class":"grid__item one-half--768 five-twelfths--1024"})
    data= data[0].text
    #print(data)
    name= data.split('\n')
    #print(name)
    data= name[2]
    name= name[1]
    print(name)
    print(data[0:4])

