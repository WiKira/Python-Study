from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 600
PROMISED_UP = 300
# CHROME_DRIVER_PATH = "/Users/willi/Development/chromedriver"
TWITTER_EMAIL = "YOUR_TWITTER_EMAIL"
TWITTER_PASSWORD = "YOUR_TWITTER_PASSWORD"


internetTest = InternetSpeedTwitterBot(PROMISED_UP, PROMISED_DOWN)

internetTest.get_internet_speed()

if internetTest.up < PROMISED_UP or internetTest.down < PROMISED_DOWN:
    internetTest.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)

internetTest.close_nav()