import tweepy
from src import settings

def get_user_tweets(username):

    twitter_client = tweepy.Client(settings.BEAREAR_TWITTER_TOKEN)
    try:
        user = twitter_client.get_user(username = username)
        tweets_response = twitter_client.get_users_tweets(user.data.id)
    except:
        return []
    if tweets_response.data:
        tweets = [tweet.text for tweet in tweets_response.data][0:5]
        return tweets
    return []



