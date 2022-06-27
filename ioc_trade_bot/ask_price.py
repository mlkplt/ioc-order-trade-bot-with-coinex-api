from set_parity import parity
from connect import Connect
coinex = Connect()

def buy_price():
    fiyat= coinex.market_ticker(parity())["ticker"]["sell"]
    return fiyat