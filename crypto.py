import json
import pandas as pd
import requests
import matplotlib.pyplot as plt
import datetime

class cryptoplot:
    def getmarket_price(vs_currency='usd',days='1000',intervals='daily'):
        url = f'https://api.coingecko.com/api/v3/coins'
        resp = requests.get(url)
        dt = resp.json()
        crypto_name = []
        for asset in dt:
            crypto_name.append(asset['id'])
        crypto_ids = crypto_name
        print("The availiable crypto currency is: ", crypto_ids)
        coin=input("Enter the name of crypto you want to see the graph: ")
        currency1=input("Enter another coin in which you want to get the chart of above entered coin: ")
        days=input("Enter the number of days for which the graph should show the data : ")
        coin_id=coin

        if coin_id in crypto_ids:
            url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart'
            payload = {'vs_currency': vs_currency, 'days': days, 'interval': intervals}

            resp = requests.get(url, params=payload)
            data = resp.json()
            timestamp_list, price_list = [], []
            for price in data['prices']:
                timestamp_list.append(datetime.datetime.fromtimestamp(price[0] / 1000))
                price_list.append(price[1])
            raw_data = {
                'timestamp': timestamp_list,
                'price': price_list
            }
            df = pd.DataFrame(raw_data)
            pr = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=" + currency1 + "&vs_currencies=usd").text
            pr = json.loads(pr)
            price1 = float(pr[currency1]["usd"])
            df['price'] = df['price'] /price1
            df.plot(y='price',x='timestamp',color='#4284F4')
            plt.title('Price of '+coin_id+' in terms of '+currency1)
            plt.ylabel(currency1)
            plt.show()
            return 0
        else:
            print("The crypto is not availiabe")

obj=cryptoplot
print(obj.getmarket_price())