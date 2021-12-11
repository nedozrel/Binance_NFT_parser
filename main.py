import json
import os
import time

import requests
from colorama import Fore, Back, Style
from colorama import init

init()


def send_req():
    url = 'https://www.binance.com/bapi/nft/v1/public/nft/market-mystery/mystery-list'
    pre_result = []

    for i in range(1, 3):

        req_data = {"page": i,
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
        pre_result.append(r.json()['data']['data'])

    result = []
    for i in pre_result:
        for j in i:
            result.append(j)

    return result


def get_color(num):
    if num >= 15:
        color = Back.RED
    elif num >= 10:
        color = Back.MAGENTA
    elif num >= 5:
        color = Back.BLUE
    elif num >= 3:
        color = Back.CYAN
    else:
        color = Back.GREEN

    return color


def main():
    while True:
        items = send_req()
        total_amount = 0
        same_price_count = 1
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(len(items)):
            price = items[i]['amount']
            if len(items) - 1 > i:
                next_price = items[i + 1]['amount']
                if next_price != price:
                    total_amount += same_price_count
                    bg_color = get_color(same_price_count)
                    print(bg_color + price, f'x{same_price_count}' + ' ' * same_price_count, sep='\t\t')
                if next_price != price and same_price_count != 1:
                    same_price_count = 1
                if next_price == price:
                    same_price_count += 1
            else:
                bg_color = get_color(len(items) - total_amount)
                print(bg_color + price, f'x{len(items) - total_amount}', sep='\t\t')
        print(Back.RESET)
        time.sleep(1)


if __name__ == '__main__':
    main()
