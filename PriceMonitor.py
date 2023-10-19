# Import necessary libraries
from autoscraper import AutoScraper
import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Input the URL of the product you want to track
url1 = input("Enter your product's URL:")

# Set user-agent headers to mimic a web browser
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

# Send an HTTP GET request to the URL and parse the page content
page = requests.get(url1, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Input your desired price and email address
x = float(input("Enter your desired price:"))
y = input("Enter your email address:")

# Function to send an email notification
def send_mail():
    # Set up an SMTP server for sending email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Log in to your email account (You should use a secure method to store credentials)
    server.login("minorproject1sem5@gmail.com", "zanujsksnuqgnkou")

    # Compose email subject and body
    subject = "Hey! The current price is below your desired price"
    body = "Check the link given below:"
    msg = f"subject:{subject}\n\n{body}\n{url1}"

    # Send the email
    server.sendmail("minorproject1sem5@gmail.com", y, msg)

    print("Email sent")

    # Close the SMTP server connection
    server.quit()

# Function to check the product price
def check_price():
    # Find and print the product title
    title = soup.find(id="productTitle").getText()
    print("Your product's title is:", title.strip())

    # Find and extract the product price from the page
    price = soup.find('span', {'class': 'a-price-whole'}).getText()
    price1 = price.replace(",", "")  # Remove commas from the price string
    newprice = float(price1)  # Convert the cleaned price to a float
    print("Your product's price is:", newprice)

    # Check if the current price is below the desired price, and send an email if it is
    if newprice <= x:
        send_mail()
    else:
        # If the price is not below the desired price, wait and check again
        while True:
            time.sleep(10)
            check_price()

# Start the price tracking process
check_price()
