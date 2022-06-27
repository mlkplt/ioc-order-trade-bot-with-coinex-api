from coinex.coinex import CoinEx
import config

def Connect():
    coinex = CoinEx(config.API_KEY, config.API_SECRET)
    return coinex