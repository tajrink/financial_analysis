from config import key
import requests
import time
import csv

stocks=["GOOGL", "AMZN", "COUR", "NFLX", "AAPL"]

for stock in stocks:
    #construst a query URL for each stock and requesting data
    url= f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-03-25?adjusted=true&sort=asc&limit=300&apiKey={key}"
    data=requests.get(url)
    json_data=data.json()
    results=json_data['results']
    
    stock_data=[]
    #looping throught each day and saving into a dictionary
    for day in results:
        closing_price=day["c"]        
        time_price= day["t"]
        
        #human readable format 
        real_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time_price/1000))
        
        #
        stock_dict={
            'Date':real_time,                
            'Closing_Price':closing_price 
        }
        
        stock_data.append(stock_dict)

        with open(f"{stock}.csv","w",newline='') as outfile:
            writer=csv.DictWriter(outfile,fieldnames=["Date","Closing_Price"])
            writer.writeheader()
            writer.writerows(stock_data)
    
    