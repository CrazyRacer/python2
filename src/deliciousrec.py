import time

from pydelicious import get_popular, get_userposts, get_urlposts


def initializeUserDict(tag, count=5):
    user_dict = {}
    for p1 in get_popular(tag=tag)[0:count]:
        for p2 in get_urlposts(p1['href']):
            user = p2['user']
            user_dict[user] = {}

    return user_dict


# print initializeUserDict(tag='programming', count=1)
k = {u'nashamanda6': {}, u'charlottediaz': {}, u'delicious': {}, u'makeuptemple': {}, u'wilkersonangel': {},
     u'everythingim': {}, u'chattysuny': {}, u'late': {}, u'ocsld': {}, u'ricadogoodwin': {}, u'ediablo77': {},
     u'drsteroids': {}, u'mayweather88': {}, u'estheryilmaz': {}, u'summersalice15': {}, u'robinsonashly': {},
     u'andersonbeatriz': {}, u'krista9graf': {}, u'mytamiltv1': {}, u'sunnychatty': {}, u'cupidbazaar': {},
     u'tattoobelen': {}, u'amelia_atkins': {}, u'damicomatt847': {}, u'naik13': {}, u'kofir': {}, u'parkerbenjamin': {},
     u'mcguireana': {}, u'fulapp': {}}


def fillItemes(user_dict):
    all_items = {}
    for user in user_dict:
        for i in range(3):
            try:
                posts = get_userposts(user)
                break
            except:
                print "Failed user " + user + ",retrying"
                time.sleep(4)
        for post in posts:
            url = post['href']
            user_dict[user][url] = 1.0
            all_items[url] = 1

    for ratings in user_dict.values():
        for item in all_items:
            if item not in ratings:
                ratings[item] = 0.0


fillItemes(k)
# print k

