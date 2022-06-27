from set_parity import parity
from connect import Connect
coinex = Connect()

def sell_price():
    fiyat= coinex.market_ticker(parity())["ticker"]["buy"]
    return fiyat