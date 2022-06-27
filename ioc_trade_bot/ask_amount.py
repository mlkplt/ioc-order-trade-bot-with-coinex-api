from set_parity import parity
from connect import Connect
coinex = Connect()

def find_buy_amount():
    miktar= coinex.market_ticker(parity())["ticker"]["sell_amount"]
    return float(miktar)