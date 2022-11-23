from ninja import NinjaAPI
from apps.base.praw_utils import get_all_subs, search_subs

api = NinjaAPI()


@api.get("/search-subs")
def search_subreddits(request, q: str = ""):
    if q == "":
        subs = get_all_subs()
    else:
        subs = search_subs(q)
    to_rtn = [{"id": sub.display_name, "text": sub.display_name} for sub in subs]
    return {"results": to_rtn}
