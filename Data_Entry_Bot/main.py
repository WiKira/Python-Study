from scraper import Scraper
from awnserBot import AwnserBot

scraperBot = Scraper()
scraperBot.get_data()

awnserBot_ = AwnserBot(scraperBot)
awnserBot_.send_data()