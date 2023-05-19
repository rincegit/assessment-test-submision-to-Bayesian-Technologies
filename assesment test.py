#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
url = "https://www.hdfcbank.com/personal/pay/cards/credit-cards"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the credit card products on the page
card_products = soup.find_all("div", class_="product-block")

# Create a CSV file to store the scraped data
csv_file = open("cards.csv", "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Card Name", "Card Fee", "Reward Points", "Lounge Access", "Milestone Benefit", "Card Fee Reversal"])

# Extract details for each credit card product
for card_product in card_products:
    card_name = card_product.find("h2").text.strip()
    card_fee = card_product.find("span", class_="fee").text.strip()
    reward_points = card_product.find("span", class_="reward-point").text.strip()
    lounge_access = card_product.find("span", class_="lounge-access").text.strip()
    milestone_benefit = card_product.find("span", class_="milestone-benefit").text.strip()
    card_fee_reversal = card_product.find("span", class_="fee-reversal").text.strip()

    csv_writer.writerow([card_name, card_fee, reward_points, lounge_access, milestone_benefit, card_fee_reversal])

# Close the CSV file
 csv_file.close()

print("Scraping complete. Data saved to credit_cards.csv.")


# In[ ]:


.

