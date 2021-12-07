import json
import os
import time

import requests


def send_req():
    url = 'https://www.binance.com/bapi/nft/v1/public/nft/market-mystery/mystery-list'

    req_data = {"page": 1,
                "size": 100,
                "params":
                    {
                        "keyword": "",
                        "nftType": "2",
                        "orderBy": "amount_sort",
                        "orderType": "1",
                        "serialNo": ["163231291595698176"],
                        "tradeType": "0"
                    }
                }

    headers = {
    'Content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/94.0.4606.85 YaBrowser/21.11.1.932 Yowser/2.5 Safari/537.36'
    }
    r = requests.post(url, data=json.dumps(req_data), headers=headers)
    return r.json()


def main():
    while True:
        r = send_req()
        data = r['data']['data']
        total_amount = 0
        same_price_count = 1
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(len(data)):
            price = data[i]['amount']
            if len(data) - 1 > i:
                next_price = data[i + 1]['amount']
                if next_price != price:
                    total_amount += same_price_count
                    print(price, f'x{same_price_count}', sep='\t\t')
                if next_price != price and same_price_count != 1:
                    same_price_count = 1
                if next_price == price:
                    same_price_count += 1
            else:
                print(price, f'x{100 - total_amount}', sep='\t\t')
        time.sleep(3)


if __name__ == '__main__':
    main()
