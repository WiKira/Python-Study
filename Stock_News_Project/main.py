from twilio.rest import Client
import datetime as dt
import json
import requests


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
FREE_STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
FREE_STOCK_API_KEY = "YOUR_FREE_API_KEY"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
TWILIO_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_API_KEY = "YOUR_TWILIO_API_KEY"


def get_stock_prices():
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "full",
        "apikey": FREE_STOCK_API_KEY
    }

    response = requests.get(url=FREE_STOCK_API_ENDPOINT, params=parameters)
    response.raise_for_status()
    #data = response.json()["Time Series (Daily)"]
    with open('dados.json') as file:
        data = json.load(file)["Time Series (Daily)"]

    values = list(data.keys())[1:3]
    day1 = float(data[values[0]]["4. close"])
    day2 = float(data[values[1]]["4. close"])

    return round(100 * (day1 - day2) / day1, 2)


def get_news():

    parameters = {
        "qInTitle": COMPANY_NAME,
        "apikey": NEWS_API_KEY,
        "pageSize": 3
    }

    response = requests.get(url=NEWS_API_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()["articles"]
    articles = []
    for article in data:
        article = {k: v for k, v in article.items() if k == "title" or k == "description"}
        articles.append(article)

    return articles


def format_message(variation: float, news: dict) -> str:
    msg = f"{STOCK}: {"🔺" if variation > 0 else "🔻"}{abs(variation)}%\n"
    for item in news:
        msg += (f"\n*Headline:* {item["title"]}\n\n"
                f"*Brief:* {item["description"]}\n\n")
    return msg


def send_message(variation: float, news: dict):
    format_message(variation, news)

    client = Client(TWILIO_SID, TWILIO_API_KEY)
    message = client.messages.create(
        from_='whatsapp:+YOUR_TWILIO_NUMBER',
        body=format_message(variation, news),
        to='whatsapp:+DESTINATION_NUMBER'
    )

    print(message.sid)


variation = get_stock_prices()

if variation >= 5 or variation <= -5:
    print("Get News")

news = get_news()

send_message(variation, news)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

