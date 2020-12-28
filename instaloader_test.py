import csv

from instaloader import Instaloader
from instaloader import Profile
from collections import Counter

L = Instaloader()
username = input("Instagram Username: ")
password = input("Instagram Pasword: ")
try:
    L.login(username, password)
except:
    print("Bad Crendentials Error")
    print("Username or Password are wrong")


profile = input("Which profile do you want to analyze? ")
try:
    profile = Profile.from_username(L.context, profile)
except:
    print('Profile not found')

all_likes = []

counter = 1
posts = profile.get_posts()
for post in posts:
    print("accesing post ", counter)
    for likes in post.get_likes():

        print(likes.username, "Likes your post")
        all_likes.append(likes.username)

    counter += 1

my_count = Counter(all_likes)
elements = dict(my_count.items())
sortDict = sorted(elements.items(), key=lambda x: x[1], reverse=True)

print(type(elements))
a_file = open("result.csv", "w")
writer = csv.writer(a_file)
for key, value in sortDict:
    writer.writerow([key, value])

a_file.close()

