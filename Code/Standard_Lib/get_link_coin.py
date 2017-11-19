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
from math import ceil


WORLD_COIN_INDEX_DEFAULT_URL = "https://www.worldcoinindex.com/widget/renderWidget?size=small&from=BTC&to=usd&clearstyle=true"

WORLD_COIN_INDEX_URL = "https://www.worldcoinindex.com/widget/renderWidget?size={0}&from={1}&to={2}&clearstyle={3}"

COIN_MARKET_CAP_URL_REC = "https://api.coinmarketcap.com/v1/ticker/regalcoin"
COIN_MARKET_CAP_URL_BTC = "https://api.coinmarketcap.com/v1/ticker/bitcoin"
COIN_MARKET_CAP_URL_BCC = "https://api.coinmarketcap.com/v1/ticker/bitconnect"
COIN_MARKET_CAP_URL_ETH = "https://api.coinmarketcap.com/v1/ticker/ethereum"
COIN_MARKET_CAP_URL_BCH = "https://api.coinmarketcap.com/v1/ticker/bitcoin-cash"
COIN_MARKET_CAP_URL_NEOG = "https://api.coinmarketcap.com/v1/ticker/neo-gold"

def get(uri):
    req = Request(uri)
    req.add_header('user-agent', 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36')
    return urlopen(req)

def printData(name, usd, btc_price = 1, eth_price = 0):
    print("Time = " + str(datetime.datetime.now()))
    print("Name = " + name)
    print("USD  = ", end=" ")
    SetConsoleTextAttribute(stdout_handle, 0x02)
    print(usd, end=" ")
    if (eth_price != 0):
        print(" <-> {0:.8f} BTC <=> {1:.8f} ETH".format(btc_price, eth_price))
    else:
        print(" <-> {0:.1f} BTC".format(btc_price))
    SetConsoleTextAttribute(stdout_handle, 0x07)

stdout_handle = windll.kernel32.GetStdHandle(-11)
SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute

if __name__ == '__main__':
    count = -1
    curr = 0
    target = 40.0
    set_time_duration = 60

    # orders
    rec_balance = 2.29408478
    rec_btc_price_buy = 0.005841

    neog_balance = 24920.94055394
    neog_btc_price_buy = 0.00000036

    btc_balance = 0.00100965
    btc_btc_price_buy = 1


    while 1:
        count += 1
        print("===== getting data.hehe ===== ", count)

        # get btc
        print("===== BTC =====")
        res = get(COIN_MARKET_CAP_URL_BTC)
        data = json.loads(res.read())
        btc_usd = Decimal(data[0]['price_usd'])
        printData(data[0]['name'], data[0]['price_usd'])

        # get eth
        print("===== ETH =====")
        res = get(COIN_MARKET_CAP_URL_ETH)
        data = json.loads(res.read())
        eth_usd = Decimal(data[0]['price_usd'])
        eth_btc_price = round(eth_usd/btc_usd, 8)
        printData(data[0]['name'], data[0]['price_usd'], eth_btc_price, 1)

        # get bch
        print("===== BCH =====")
        res = get(COIN_MARKET_CAP_URL_BCH)
        data = json.loads(res.read())
        bch_usd = Decimal(data[0]['price_usd'])
        bch_btc_price = round(bch_usd/btc_usd, 8)
        bch_eth_price = round(bch_usd/eth_usd, 8)
        printData(data[0]['name'], data[0]['price_usd'], bch_btc_price, bch_eth_price)

        # get bcc
        print("===== BCC =====")
        res = get(COIN_MARKET_CAP_URL_BCC)
        data = json.loads(res.read())
        bcc_usd = Decimal(data[0]['price_usd'])
        bcc_btc_price = round(bcc_usd/btc_usd, 8)
        bcc_eth_price = round(bcc_usd/eth_usd, 8)
        printData(data[0]['name'], data[0]['price_usd'], bcc_btc_price, bcc_eth_price)

        # get neog
        print("===== NEOG =====")
        res = get(COIN_MARKET_CAP_URL_NEOG)
        data = json.loads(res.read())
        neog_usd = Decimal(data[0]['price_usd'])
        neog_btc_price = round(neog_usd/btc_usd, 8)
        neog_eth_price = round(neog_usd/eth_usd, 8)
        printData(data[0]['name'], data[0]['price_usd'], neog_btc_price, neog_eth_price)

        # get rec
        print("===== REC =====")
        res = get(COIN_MARKET_CAP_URL_REC)
        data = json.loads(res.read())
        rec_usd = Decimal(data[0]['price_usd'])
        rec_btc_price = round(rec_usd/btc_usd, 8)
        rec_eth_price = round(rec_usd/eth_usd, 8)
        printData(data[0]['name'], data[0]['price_usd'], rec_btc_price, rec_eth_price)

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

        # Tinh lai
        sum_btc_buy = btc_balance * btc_btc_price_buy
        sum_rec_buy = rec_balance * rec_btc_price_buy
        sum_neog_buy = neog_balance * neog_btc_price_buy

        sum_rec = rec_balance * float(rec_btc_price)
        sum_neog = neog_balance * float(neog_btc_price)

        sum_all_buy = sum_btc_buy + sum_rec_buy + sum_neog_buy
        sum_all = sum_btc_buy + sum_rec + sum_neog
        print("{0}: {1:.8f} * {2:0.8f} = {3:0.8f} || new {4:.8f} => {5:.8f} BTC ".format("BTC", btc_balance, btc_btc_price_buy, sum_btc_buy, btc_btc_price_buy, btc_btc_price_buy - btc_btc_price_buy))
        print("{0}: {1:.8f} * {2:0.8f} = {3:0.8f} || new {4:.8f} => {5:.8f} BTC ({6:.2f}%)".format("REC", rec_balance, rec_btc_price_buy, sum_rec_buy, rec_btc_price, sum_rec - sum_rec_buy, sum_rec / sum_rec_buy * 100))
        print("{0}: {1:.8f} * {2:0.8f} = {3:0.8f} || new {4:.8f} => {5:.8f} BTC ({6:.2f}%)".format("NEOG", neog_balance, neog_btc_price_buy, sum_neog_buy, neog_btc_price, sum_neog - sum_neog_buy, sum_neog / sum_neog_buy * 100))
        print("sum buy: {0:.8f} => ${1:.8f}".format(sum_all_buy, sum_all_buy * float(btc_usd)))
        print("sum new: {0:.8f} => ${1:.8f} => {2:.2f}%".format(sum_all, sum_all * float(btc_usd), sum_all / sum_all_buy *100))

        ## done
        # print("===== xong.hehe =====")
        # wait = input("PRESS 'E' TO EXIT.. ANY KEY TO CONTINUE..")

        # if wait == 'E':
        #     break
        print("===== Wait %s =====" % set_time_duration)
        time.sleep(set_time_duration)
