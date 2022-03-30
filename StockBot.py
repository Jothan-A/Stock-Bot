import discord
import json
from webbrowser import get
import requests
from datetime import date


def getData(ticker, data):
    try:
        response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + str(ticker) + '&apikey=L3C6ZKOS8SJ50625')

    #https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOOGL&apikey=L3C6ZKOS8SJ50625

        read = response.json()
        
        
        today = date.today()
        d3 = today.strftime("%Y-%m-%d")
        timeSeries = read['Time Series (Daily)']
        currentDate = timeSeries[d3]
        

        if(data.lower() == 'open'):
            info = currentDate['1. open']
            return("The Opening Price of " + ticker + ' is $' + str(round(float(info), 7))) 
        if(data.lower() == 'high'):
            info = currentDate['2. high']
            return("High Price of " + ticker + ' is $' + str(round(float(info), 7))) 
        if(data.lower() == 'low'):
            info = currentDate['3. low']
            return("Low Price of " + ticker + ' is $' + str(round(float(info), 7))) 
        if(data.lower() == 'close'):
            info = currentDate['4. close']
            return("The Closing Price of " + ticker + ' is $' + str(round(float(info), 7))) 
        if(data.lower() == 'volume'):
            info = currentDate['5. volume']
            return("The Volume of " + ticker + ' is ' + str(round(float(info), 7)))

            

        
    except:
        return("That is not valid")
client = discord.Client()

@client.event

async def on_message(message):

    
    print(message.content)
    if(message.content[0]=='$'):
        try:
            print(message.content.split()[1])
            print(message.content.split()[3])
            print(getData ((message.content.split()[1]), (message.content.split()[3])))
            await message.channel.send(getData ((message.content.split()[1]), (message.content.split()[3])))
        except:
            print("Invalid Input")
            await message.channel.send("Invalid Syntax!")
            


client.run('OTQ0MzczOTAyNDMwMzI2ODQ0.YhAquw.p7_gaeyN8OVmpnwTwrNBHGYfJR4')



