# tweet-scheduler
Simple Python script to schedule tweets

This script authenticates with the Twitter API and sets up command line flag arguments to schedule a single tweet or schedule tweets from a CSV file one tweet per day. The -s or --schedule flag is used to schedule a single tweet, the -f or --file flag is used to schedule tweets from a CSV file, and the -t or --time flag is used to define the scheduled time for the tweets in 24-hour format (HH:MM). If the scheduled time has already passed for the day, it will schedule the tweet for the following day. The script iterates through the tweets in the CSV file, scheduling each one for the next day at the defined scheduled time.

```
usage: script.py [-h] [-s SCHEDULE] [-f FILE] -t TIME

options:
  -h, --help            show this help message and exit
  -s SCHEDULE, --schedule SCHEDULE
                        Schedule a single tweet
  -f FILE, --file FILE  Schedule tweets from a CSV file
  -t TIME, --time TIME  Scheduled time for tweets in 24-hour format (HH:MM)
```
