import requests
from bs4 import BeautifulSoup

class Scraper():

    def __init__(self):
        response = requests.get("https://appbrewery.github.io/Zillow-Clone")

        self.soup = BeautifulSoup(response.text, 'html.parser')
        self.links = []
        self.values = []
        self.addresses = []

    def get_data(self):
        plinks = self.soup.select(selector=".property-card-link")
        self.links = [link.get('href') for link in plinks]
        print(self.links)
        print(len(self.links))

        pvalues = self.soup.select(selector=".PropertyCardWrapper__StyledPriceLine")
        self.values = [value.text[0:6].replace('/', '').replace('+', '') for value in pvalues]
        print(self.values)
        print(len(self.values))

        paddresses = self.soup.select(selector="address")
        self.addresses = [address.text.replace('\n', '').replace('|', '').strip() for address in paddresses]
        print(self.addresses)
        print(len(self.addresses))