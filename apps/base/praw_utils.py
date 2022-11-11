from config.settings.base import REDDIT_CLIENT, REDDIT_SECRET, REDDIT_USERNAME
import praw

def get_all_subs():
    reddit = praw.Reddit(client_id=REDDIT_CLIENT,client_secret=REDDIT_SECRET, user_agent=REDDIT_USERNAME)
    return_list = []
    for x in reddit.subreddits.default(limit=None):
        return_list.append(x)
    return return_list
