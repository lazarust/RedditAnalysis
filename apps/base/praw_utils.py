from config.settings.base import REDDIT_CLIENT, REDDIT_SECRET
import praw

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT,
    client_secret=REDDIT_SECRET,
)

for submission in reddit.subreddit("news").hot(limit=10):
    print(submission.title)
