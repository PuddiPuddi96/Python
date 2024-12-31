from internet_speed_twitter_bot import InternetSpeedTwitterBot

PROMISED_DOWN = 100000000
PROMISED_UP = 100000000

twitter_bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
twitter_bot.get_internet_speed()

if twitter_bot.promise_up > twitter_bot.up or twitter_bot.promise_down > twitter_bot.down:
    twitter_bot.tweet_as_provider()
