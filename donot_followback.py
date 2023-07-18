from instagrapi import Client

with open("credentials.txt", "r") as f:
    username, password = f.read().splitlines()

cl = Client()
cl.login(username, password)

user_me = cl.user_id_from_username("its_me_alen_roy")

following_whitelist = ['ryan._.cmk', 'albz_.zz', '__owl_girl', '___.han.nah.___', '_jorge.cornejo_', '_sarangi.saru_', 'followback.army']

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
