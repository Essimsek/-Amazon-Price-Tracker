# Amazon-Price-Tracker
Amazon Price Tracker

## Requirements
- Python (3.x recommended)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/essimsek/amazon-price-tracker.git

2. Install dependencies:
   ```bash
    cd amazon-price-tracker
    pip install -r requirements.txt

4. Update your user agent and accept language:

   go to https://myhttpheader.com/
   header = {
    "User-Agent": "Your User Agent",
    "Accept-Language": "Your Accept Language",
   }

6. Create a .env file in the project root and add your sender email and password:

    SENDER_EMAIL=your_email@gmail.com
    SENDER_PASSWORD=your_email_password

   # To get the Sender email and sender password you need to
    Create a Gmail Account:
   
    If you don't have a Gmail account, you need to create one. Visit Gmail and sign up for a new account.

    Enable Less Secure Apps:
    To allow your script to access your Gmail account for sending emails, you need to enable "Less secure app access" in your Google Account settings. Follow these steps:

    Go to https://myaccount.google.com/.
    Click on "Security" in the left sidebar.
    Scroll down to the "Less secure app access" section.
    Turn on "Allow less secure apps."
    Generate an App Password (Optional but Recommended):
    Instead of using your main Gmail password directly in your script, it's recommended to generate an app password specifically for this script. Here's how:

    Go to https://myaccount.google.com/apppasswords.
    Select "Mail" and "Other (Custom Name)" in the dropdown menus.
    Enter a custom name for the app (e.g., "AmazonPriceTracker").
    Click "Generate."
    Copy the generated app password; you will use this as your SENDER_PASSWORD in the .env file.

8. Update the recipient_email, product_url and last price value(last_price.txt) variables in the script with your desired values.

9. run the script:
   ```bash
    python price_tracker.py


