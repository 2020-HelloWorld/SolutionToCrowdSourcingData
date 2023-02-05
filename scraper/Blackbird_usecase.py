import os
def scrapeBlackBird(username):
    try:
        os.system("python scraper/blackbird.py -u "+username)
        return 0
    except:
        return -1
