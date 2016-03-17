import recommendations
import time;


def loadMovieLens(path='/Users/yupeng/Downloads/ml-100K'):
    movies = {}
    for line in open(path + '/u.item'):
        (id, title) = line.split('|')[0:2]
        movies[id] = title

    prefs = {}
    for line in open(path + '/u.data'):
        (user, movieid, rating, ts) = line.split("\t")
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)
    return prefs


prefs = loadMovieLens()
start = time.time()
result = recommendations.getRecommendations(prefs, '87')[0:30]
print result
print time.time() - start
start = time.time()
itemsim = recommendations.calculateSimilarItems(prefs, n=50)
print itemsim
print recommendations.getRecommendedItems(prefs, itemsim, '87')[0:30]
print time.time() - start
