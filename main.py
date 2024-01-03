import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# Sender credentials
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")

# Recipient email
recipient_email = "Your email"

product_url = "pruduct_url"

header = {
    "User-Agent": "Your User Agent",
    "Accept-Language": "Your Accept Language",
}

response = requests.get(url=product_url)
soup = BeautifulSoup(response.content, "lxml")
current_price = float(soup.find(name="span", class_="a-offscreen").getText().split('$')[1])

with open("last_price.txt", mode="r") as file:
    last_price = float(file.readline())
    print(last_price, current_price)

if current_price < last_price:
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:

        # Message content
        subject = "Price Tracker"
        body = f"Good news!! The price of your tracked item has dropped\n\n" \
               f"Previous price: {last_price}\n" \
               f"Current  price: {current_price}\n\n" \
               f"Visit the product page on amazon = {product_url}"
        msg = f"Subject: {subject}\n\n{body}".encode("utf-8")

        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=recipient_email,
                            msg=msg)

        with open("last_price.txt", mode="w") as file:
            file.write(str(current_price))
