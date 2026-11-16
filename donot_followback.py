from instagrapi import Client
import credentials

username = credentials.username
password = credentials.password
sessionid = credentials.sessionid

cl = Client()
if sessionid:
    cl.login_by_sessionid(sessionid)
else:
    cl.login(username, password)

user_me = cl.user_id_from_username(username)

following = cl.user_following(user_me)
followers = cl.user_followers(user_me)
followers_list = []

common=[]

for j in followers:
    me1 = str(followers[j])
    followers_list.append(me1.split("'")[3])

for i in following:
    me = str(following[i])
    if followers_list.count(me.split("'")[3]) == 0:
        common.append(me.split("'")[3])

print(common)
