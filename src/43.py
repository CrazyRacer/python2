import pydelicious

p1 = pydelicious.get_popular(tag='programming')[0:1]
print p1[0]['href']
# print pydelicious.get_userposts('delicious')[0:3]

print pydelicious.get_urlposts('http://furnitureyoucanafford.com/')