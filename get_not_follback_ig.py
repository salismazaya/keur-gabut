from instagrapi import Client
from concurrent.futures import ThreadPoolExecutor

cl = Client()

cl.login_by_sessionid('SESSION_ID_COOKIE')

me = cl.user_info_by_username(cl.account_info().username)

def check(user):
    try:
        username = cl.username_from_user_id(user)
        if not cl.search_followers(me.pk, username):
            print(username)
    except Exception as e:
        print(e)

following_users = cl.user_following(me.pk, amount = me.following_count).keys()
with ThreadPoolExecutor(max_workers = 15) as t:
    t.map(check, following_users)
