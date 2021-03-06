#!/usr/bin/python3
#
"""
    @author: MinhHT3
    @brief : urllib check coin
"""
from urllib.request import urlopen, Request
import json
import datetime, time
import re
from ctypes import windll


WORLD_COIN_INDEX_DEFAULT_URL = "https://www.worldcoinindex.com/widget/renderWidget?size=small&from=BTC&to=usd&clearstyle=true"

WORLD_COIN_INDEX_URL = "https://www.worldcoinindex.com/widget/renderWidget?size={0}&from={1}&to={2}&clearstyle={3}"

COIN_MARKET_CAP_URL_REC = "https://api.coinmarketcap.com/v1/ticker/regalcoin"
COIN_MARKET_CAP_URL_BTC = "https://api.coinmarketcap.com/v1/ticker/bitcoin"
COIN_MARKET_CAP_URL_BCC = "https://api.coinmarketcap.com/v1/ticker/bitconnect"

def get(uri):
    req = Request(uri)
    req.add_header('user-agent', 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36')
    return urlopen(req)

def printData(name, usd):
    print("Time = " + str(datetime.datetime.now()))
    print("Name = " + name)
    print("USD  = ", end=" ")
    SetConsoleTextAttribute(stdout_handle, 0x02)
    print(usd)
    SetConsoleTextAttribute(stdout_handle, 0x07)

stdout_handle = windll.kernel32.GetStdHandle(-11)
SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute

if __name__ == '__main__':
    print("===== getting data.hehe =====")

    # # get rec
    # print("===== REC =====")
    # res = get(COIN_MARKET_CAP_URL_REC)
    # data = json.loads(res.read())
    # printData(data[0]['name'], data[0]['price_usd'])

    # # get btc
    # print("===== BTC =====")
    # res = get(COIN_MARKET_CAP_URL_BTC)
    # data = json.loads(res.read())
    # printData(data[0]['name'], data[0]['price_usd'])

    # get bcc
    print("===== BCC =====")
    res = get('https://www.worldcoinindex.com/coin/bitcoin')
    # data = json.loads(res.read())
    # printData(data[0]['name'], data[0]['price_usd'])
    pattern = r'(btcusd)[\s\S]*btceur'
    data = res.read().decode('utf-8').encode('cp850','replace').decode('cp850')

    match = re.search(pattern, data)
    if match:
        print(match[0])

    ## done
    print("===== xong.hehe =====")
    wait = input("PRESS ENTER TO EXIT.")
