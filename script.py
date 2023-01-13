import tweepy
import csv
import argparse
from datetime import datetime, timedelta

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Set up command line flag arguments
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--schedule", help="Schedule a single tweet")
parser.add_argument("-f", "--file", help="Schedule tweets from a CSV file")
parser.add_argument("-t", "--time", required=True help="Scheduled time for tweets in 24-hour format (HH:MM)")
args = parser.parse_args()

# Schedule a single tweet
if args.schedule:
    scheduled_time = datetime.strptime(args.time, "%H:%M")
    current_time = datetime.now().time()
    if current_time >= scheduled_time:
        scheduled_time += timedelta(days=1)
    scheduled_datetime = datetime.combine(datetime.now(), scheduled_time)
    api.update_status(args.schedule, scheduled_datetime=scheduled_datetime)

# Schedule tweets from a CSV file
elif args.file:
    with open(args.file, 'r') as csvfile:
        tweetreader = csv.reader(csvfile)
        tweets = [row[0] for row in tweetreader]
    scheduled_time = datetime.strptime(args.time, "%H:%M")
    current_time = datetime.now().time()
    if current_time >= scheduled_time:
        scheduled_time += timedelta(days=1)
    scheduled_datetime = datetime.combine(datetime.now(), scheduled_time)
    for tweet in tweets:
        api.update_status(tweet, scheduled_datetime=scheduled_datetime)
        scheduled_datetime += timedelta(days=1)

else:
    print("Please provide a tweet or file to schedule")
