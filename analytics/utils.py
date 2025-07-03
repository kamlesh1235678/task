import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests

# there we use open api  not Scraping  use api integration
def fetch_flight_data():
    url = "https://api.example.com/flights"
    response = requests.get(url, params={"origin": "SYD", "destination": "MEL"})
    data = response.json()
    return data




def analyze(data):
    df = pd.DataFrame(data)
    route_count = df.groupby(['source', 'destination']).size().sort_values(ascending=False)
    price_trend = df.groupby('date')['price'].mean()
    return route_count, price_trend