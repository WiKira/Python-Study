from InstagramBot import InstagramBot

SIMILAR_ACCOUNT = "SOME_ACCOUNT"
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

instaBot = InstagramBot()

instaBot.login(USERNAME, PASSWORD)

instaBot.find_followers(SIMILAR_ACCOUNT)

instaBot.follow()

instaBot.close_nav()
