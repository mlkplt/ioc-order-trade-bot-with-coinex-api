from set_parity import parity
from connect import Connect
coinex = Connect()

def  check_price(): #it shows the current price
    klines = coinex.market_kline(parity(),"1hour")
    high = [float(entry[2]) for entry in klines]
    return high[-1]
