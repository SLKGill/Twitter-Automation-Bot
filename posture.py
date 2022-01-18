import tweepy

# authentication credentials
auth = tweepy.OAuthHandler("OCVNXxtnO9T5SLwJqUKaREnxg",
                           "Kf2R9wMNBDDUjs93LjhRSSMb9cjRjqpysz5r8Mc0T9gn4ppqCB")
auth.set_access_token("1072291513584025600-dLEjxse7yltT95CXInhBbYzVqCf8T4",
                      "Cyo6i8EiB0BeKXBjozCycAp8vqGhXvgzBO6LQF9p5uvGg")
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# api object, print a message and wait if the rate limit is exceeded
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# get the last 20 entries in your timeline
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}\n")


# set tweets, create a new tweet from a Python string.
api.update_status("Test tweet from Python")
