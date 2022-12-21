from ninja import NinjaAPI
from .utils import praw_utils

api = NinjaAPI()


@api.get("/search-subs")
def search_subreddits(request, q: str = ""):
    if q == "":
        subs = praw_utils.get_all_subs()
    else:
        subs = praw_utils.search_subs(q)
    to_rtn = [{"id": sub.display_name, "text": sub.display_name} for sub in subs]
    return {"results": to_rtn}
