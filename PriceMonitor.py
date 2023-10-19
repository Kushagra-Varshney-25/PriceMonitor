from autoscraper import AutoScraper
import requests
from bs4 import BeautifulSoup
import smtplib
import time

url1 = input("enter your product's url:")

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'} 

page = requests.get(url1,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
x = float(input("Enter your desired price:"))
y = input("enter your email-id:")

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("minorproject1sem5@gmail.com","zanujsksnuqgnkou")
    subject = "Hey! The current price is below your desired price"
    body = "Check the link given below:"


    msg = f"subject:{subject}\n\n{body}\n{url1}"
    server.sendmail("minorproject1sem5@gmail.com",y,msg)

    print("email sent")

    server.quit()

def check_price():
    title = soup.find(id="productTitle").getText()
    print("Your product's title is:" ,title.strip())

    price = soup.find('span',{'class':'a-price-whole'}).getText()

    price1 = price.replace(",","")
   
    newprice =float(price1)
    print("Your product's price is:",newprice)
    if (newprice<=x):
        send_mail()
    else:
        while (True):
            time.sleep(10)
            check_price()


check_price()
