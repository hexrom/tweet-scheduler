import tweepy
import schedule
import time
import argparse

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Connect to the Twitter API using Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to schedule and send tweets
def tweet(message):
    api.update_status(message)
    print("Tweeted: " + message)

# Use argparse to accept the tweet message and scheduled time as command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--message", required=True, help="The message to tweet")
parser.add_argument("-s", "--schedule", required=True, help="The schedule time for the tweet in 24 hour format (HH:MM)")
args = parser.parse_args()
message = args.message
schedule_time = args.schedule

# Schedule the tweet to be sent at the input time
schedule.every().day.at(schedule_time).do(tweet, message)

while True:
    schedule.run_pending()
    time.sleep(1)
