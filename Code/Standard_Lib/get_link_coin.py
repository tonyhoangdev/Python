#!/usr/bin/python3
#
"""
    @author: MinhHT3
    @brief : urllib check coin
"""
from urllib.request import urlopen, Request
import json
import datetime, time
from ctypes import windll
from decimal import Decimal
import subprocess


WORLD_COIN_INDEX_DEFAULT_URL = "https://www.worldcoinindex.com/widget/renderWidget?size=small&from=BTC&to=usd&clearstyle=true"

WORLD_COIN_INDEX_URL = "https://www.worldcoinindex.com/widget/renderWidget?size={0}&from={1}&to={2}&clearstyle={3}"

COIN_MARKET_CAP_URL_REC = "https://api.coinmarketcap.com/v1/ticker/regalcoin"
COIN_MARKET_CAP_URL_BTC = "https://api.coinmarketcap.com/v1/ticker/bitcoin"
COIN_MARKET_CAP_URL_BCC = "https://api.coinmarketcap.com/v1/ticker/bitconnect"
COIN_MARKET_CAP_URL_ETH = "https://api.coinmarketcap.com/v1/ticker/ethereum"
COIN_MARKET_CAP_URL_BCH = "https://api.coinmarketcap.com/v1/ticker/bitcoin-cash"

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

    count = -1
    curr = 0
    target = 50.0
    set_time_duration = 60

    while 1:
        count += 1
        print("===== getting data.hehe ===== ", count)

        # get btc
        print("===== BTC =====")
        res = get(COIN_MARKET_CAP_URL_BTC)
        data = json.loads(res.read())
        printData(data[0]['name'], data[0]['price_usd'])

        # get bch
        print("===== BCH =====")
        res = get(COIN_MARKET_CAP_URL_BCH)
        data = json.loads(res.read())
        printData(data[0]['name'], data[0]['price_usd'])

        # get bcc
        print("===== BCC =====")
        res = get(COIN_MARKET_CAP_URL_BCC)
        data = json.loads(res.read())
        printData(data[0]['name'], data[0]['price_usd'])

        # get eth
        print("===== ETH =====")
        res = get(COIN_MARKET_CAP_URL_ETH)
        data = json.loads(res.read())
        printData(data[0]['name'], data[0]['price_usd'])

        # get rec
        print("===== REC =====")
        res = get(COIN_MARKET_CAP_URL_REC)
        data = json.loads(res.read())
        printData(data[0]['name'], data[0]['price_usd'])

        curr = Decimal(data[0]['price_usd'])
        if (curr < target):
            SetConsoleTextAttribute(stdout_handle, 0x0C)
            print("===========> Gia da giam, mua thoi..", curr)
            SetConsoleTextAttribute(stdout_handle, 0x07)

            subprocess.call('"C:\Windows\system32\mspaint.exe"')
        else:
            SetConsoleTextAttribute(stdout_handle, 0x0A)
            print("<<<< Gia chua giam, chua mua..", curr)
            SetConsoleTextAttribute(stdout_handle, 0x07)


        ## done
        # print("===== xong.hehe =====")
        # wait = input("PRESS 'E' TO EXIT.. ANY KEY TO CONTINUE..")

        # if wait == 'E':
        #     break
        print("===== Wait %s =====" % set_time_duration)
        time.sleep(set_time_duration)
