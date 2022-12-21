from config.settings.base import REDDIT_CLIENT, REDDIT_SECRET, REDDIT_USERNAME
import pandas as pd
import praw
from datetime import datetime


def iterator_to_dataframe(iterator) -> pd.DataFrame:
    print("Converting iterator to dataframe")
    data = []
    for submission in iterator:
        data.append(
            {
                "id": submission.id,
                "score": submission.score,
                "ups": submission.ups,
                "downs": submission.downs,
                "upvote_ratio": submission.upvote_ratio,
                "edited": submission.edited,
                "num_comments": submission.num_comments,
                "date": datetime.fromtimestamp(submission.created_utc).date(),
                "num_crossposts": submission.num_crossposts,
                "is_video": submission.is_video,
                "text": submission.name,
                "author_karma": submission.author.total_karma
                if submission.author
                else 0,
            }
        )
    print("Done converting iterator to dataframe")
    return pd.DataFrame(data)


def get_all_subs():
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT, client_secret=REDDIT_SECRET, user_agent=REDDIT_USERNAME
    )
    return reddit.subreddits.default(limit=None)


def search_subs(query: str):
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT, client_secret=REDDIT_SECRET, user_agent=REDDIT_USERNAME
    )
    return reddit.subreddits.search(query)


def get_post_data(subreddit: str):
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT, client_secret=REDDIT_SECRET, user_agent=REDDIT_USERNAME
    )
    return iterator_to_dataframe(
        reddit.subreddit(subreddit).top(time_filter="year", limit=60)
    )
