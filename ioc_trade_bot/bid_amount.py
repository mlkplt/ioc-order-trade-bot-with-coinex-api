from set_parity import parity
from connect import Connect
coinex = Connect()

def find_sell_amount():
    miktar= coinex.market_ticker(parity())["ticker"]["buy_amount"]
    return float(miktar)