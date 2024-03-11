from instagrapi import Client
import credentials
from time import sleep

username = credentials.username
password = credentials.password

cl = Client()
cl.login(username, password)

user = ["followback.army"]
user_me = cl.user_id_from_username(username)

def follow_user ():
    user_id = []
    for i in user:
        user_id.append(cl.user_id_from_username(i))

    following = list(cl.user_following(user_me).keys())

    t = 0
    for i in user_id:
        if i not in following:
            try:
                cl.user_follow(i)
                print("Follow Number: " + str(t))
                t+=1
                sleep(20)
            except:
                print("Unable to follow")
                continue

def follow_user_following():
    user_id = []
    user_followers = []
    a = 0

    for i in user:
        user_id.append(cl.user_id_from_username(i))
        for j in list(cl.user_followers(user_id[a], amount=100).keys()):
            user_followers.append(j)
        a += 1

    following = list(cl.user_following(user_me).keys())

    t = 0
    for i in user_followers:
        if i not in following:
            try:
                cl.user_follow(i)
                print("Follow Number: " + str(t))
                t += 1
                sleep(20)
            except:
                print("Unable to follow")
                continue

def unfollow_nonfollowers():
    followers = list(cl.user_followers(user_me).keys())
    following = list(cl.user_following(user_me).keys())

    following_whitelist = ['ryan._.cmk', 'albz_.zz', '__owl_girl', '___.han.nah.___', '_jorge.cornejo_',
                           '_sarangi.saru_', 'followback.army']
    following_whitelist_id = ['40690646758', '48209689286', '50036115339', '50046907140', '58857647854', '60107881564']
    """for i in following_whitelist:
        try:
            following_whitelist_id.append(cl.user_id_from_username(i))
            sleep(1)
        except:
            continue"""

    t = 0
    for i in following:
        if i not in followers and i not in following_whitelist_id:
            try:
                cl.user_unfollow(i)
                print("Follow Number: " + str(t))
                t += 1
                sleep(20)
            except:
                print("Unable to follow")
                continue

follow_user_following()