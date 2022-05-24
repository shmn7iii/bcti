import requests
import datetime
import math


# 01

first_day = datetime.datetime.strptime("2009/01/04 03:15:05+0900",
                                       "%Y/%m/%d %H:%M:%S%z")
today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
reward = 50 * \
    (0.5 ** (math.floor((today - first_day).total_seconds() / (60 * 10 * 210000))))
print(reward)


# =============================================================================
# 02

response = requests.get('https://blockchain.info/tickers')
json = response.json()
btc_jpy = json["BTC"]["JPY"]["last"]
print(btc_jpy)

# =============================================================================
# 03

tmp = 5 / 6
kwh = (btc_jpy * reward / tmp) / 1000000
print(f'5円: {kwh}')

tmp = 10/6
kwh = (btc_jpy * reward / tmp) / 1000000
print(f'10円: {kwh}')

# =============================================================================
# 04

reward = 50 * \
    (0.5 ** (math.floor(((today - first_day) +
     datetime.timedelta(years=40)).total_seconds() / (60 * 10 * 210000))))

tmp = 5 / 6
kwh = (btc_jpy * reward / tmp) / 1000000
print(f'5円: {kwh}')

tmp = 10/6
kwh = (btc_jpy * reward / tmp) / 1000000
print(f'10円: {kwh}')
