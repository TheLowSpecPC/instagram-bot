import time
from instagrapi import Client
import credentials

cl = Client()
if credentials.sessionid:
    cl.login_by_sessionid(credentials.sessionid)
else:
    cl.login(credentials.username, credentials.password)

user_me = cl.user_id

# 1. Fetch both lists (2 API calls total)
following = cl.user_following(user_me)
followers = cl.user_followers(user_me)

# 2. Filter non-followers FIRST using set difference (0 extra API calls)
not_following_back_ids = set(following.keys()) - set(followers.keys())

personal_non_followers = {}

# 3. Only check account_type for the remaining non-followers
for user_id in not_following_back_ids:
    try:
        info = cl.user_info_v1(user_id)
        if info.account_type != 3:  # 2 = Business, 3 = Creator
            personal_non_followers[user_id] = following[user_id]
            
    except Exception as e:
        print(f"Error fetching info for {following[user_id].username}: {e}")

for user_id in personal_non_followers:
    print(f"{personal_non_followers[user_id].username}, ")