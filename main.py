from instagrapi import Client

with open("credentials.txt", "r") as f:
    username, password = f.read().splitlines()

cl = Client()
cl.login(username, password)

user_me = cl.user_id_from_username("its_me_alen_roy")
user_them1 = cl.user_id_from_username("followback.army")

following_whitelist = ['ryan._.cmk', 'albz_.zz', '__owl_girl', '___.han.nah.___', '_jorge.cornejo_', '_sarangi.saru_', 'followback.army']

following = cl.user_following(user_me)
followers = cl.user_followers(user_me)
followers_list = []
#following_them1 = cl.user_followers(user_them1)

common=[]

print(cl.user_follow(cl.user_id_from_username("__owl_girl")))