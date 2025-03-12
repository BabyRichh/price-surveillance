```python
import requests
from bs4 import BeautifulSoup
import smtplib
import time
from config import URL, TARGET_PRICE, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL


def check_price():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(URL, headers=headers)
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Exemple pour Amazon, récupère le prix
    price = soup.find("span", {"id": "priceblock_ourprice"}).get_text()
    price = float(price.replace('$', '').replace(',', '').strip())

    if price <= TARGET_PRICE:
        send_email(price)


def send_email(price):
    subject = 'Alerte : Le prix de votre produit a baissé !'
    body = f"Le prix du produit a baissé à ${price} !\n\nVisitez le lien : {URL}"
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg)
    server.quit()


def run():
    while True:
        check_price()
        time.sleep(3600)  # Vérifie toutes les heures (3600 secondes)

# Démarre la surveillance
run()