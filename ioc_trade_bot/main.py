import requests
import time
import connect
import kline
from min_amount import tutar, min_tutar
from ask_price import buy_price
from ask_amount import find_buy_amount
from set_parity import parity
from bid_price import sell_price
from bid_amount import find_sell_amount
from set_type import type

coinex=connect.Connect()

class IocTrade:
    def __init__(self):
        self.start_trade=type()
        if self.start_trade == "buy":
            self.side="buy"
            while 1:
                time.sleep(3)
                try:
                    r = requests.get("http://api.coinex.com?")
                except (requests.ConnectionError, requests.ReadTimeout, requests.HTTPError, requests.RequestException, KeyboardInterrupt) as hata:
                    print("OOPS!! Connection error!!!\n")
                    print(str(hata))            
                    continue 
                print(f'\n{parity()} Price\t:', kline.check_price())
                if find_buy_amount() < min_tutar(): 
                    order=coinex.order_ioc(parity(), type=self.side, amount= tutar(), price=buy_price())
                    print("\nThe buy has been made. Restart the program!")
                    print("."*30)
                    break
        elif self.start_trade == "sell":
            self.side1="sell"
            while 2:
                time.sleep(3)
                try:
                    r = requests.get("http://api.coinex.com?")
                except (requests.ConnectionError, requests.ReadTimeout, requests.HTTPError, requests.RequestException, KeyboardInterrupt) as hata:
                    print("OOPS!! Connection error!!!\n")
                    print(str(hata))            
                    continue 
                print(f'\n{parity()} Price\t:', kline.check_price())
                if  find_sell_amount() < min_tutar():
                    order1=coinex.order_ioc(parity(), type=self.side1, amount=tutar(), price=sell_price())
                    print("\nThe sell has been made. Restart the program!")  
                    print("."*30)
                    break

if __name__ == "__main__":
    IocTrade()