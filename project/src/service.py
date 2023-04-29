import requests
from bs4 import BeautifulSoup

class Price():
    def fetch_price():
        url = "https://www.metal.com/Lithium-ion-Battery/202303240001"
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            price_ele = soup.find('span', {'class': 'strong___1JlBD priceDown___2TbRQ'})
            if price_ele:
                price = price_ele.text
                return price
            else:
                return None
        except:
            return None