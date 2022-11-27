from config.settings.base import REDDIT_CLIENT, REDDIT_SECRET, REDDIT_USERNAME
import praw
import pandas as pd


def iterator_to_dataframe(iterator) -> pd.DataFrame:
    data = []
    for submission in iterator:
        submission_dict = submission.__dict__
        data.append(
            {
                "id": submission_dict["id"],
                "score": submission_dict["score"],
                "ups": submission_dict["ups"],
                "downs": submission_dict["downs"],
                "upvote_ratio": submission_dict["upvote_ratio"],
                "edited": submission_dict["edited"],
                "num_comments": submission_dict["num_comments"],
                "created_utc": submission_dict["created_utc"],
                "num_crossposts": submission_dict["num_crossposts"],
                "is_video": submission_dict["is_video"],
            }
        )

    return pd.DataFrame(data=data)


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
    return iterator_to_dataframe(reddit.subreddit(subreddit).hot(limit=1000))
