# coding=utf-8
import random
from persondata import m
import recommendations

# 随机找出一个人
# user = m.keys()[random.randint(0, len(m) - 1)]
# print user

# 按照人来进行推荐相似的排名
# print recommendations.topMatches(m, user)
# 按照人来推荐
# print recommendations.getRecommendations(m, user)[0:1]
# url = recommendations.getRecommendations(m, user)[0][1]

# print recommendations.topMatches(recommendations.transformPrefs(m), url)
# print recommendations.getRecommendations(recommendations.transformPrefs(m), url)

itemsim = recommendations.calculateSimilarItems(recommendations.critics)

print itemsim
# print itemsim
#
# url = recommendations.topMatches(recommendations.transformPrefs(recommendations.critics), 'Superman Returns',
#                                  similarity=recommendations.sim_distance)

def getRecommendedItems(prefs, itemMatch, user):
    userRatings = prefs[user]
    scores = {}
    totalSum = {}
    for item, rating in userRatings.items():
        for similarity, item2 in itemMatch[item]:
            if item2 in userRatings: continue

            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating

            totalSum.setdefault(item2, 0)
            totalSum[item2] += similarity
    rankings = [(score / totalSum[item], item) for item, score in scores.items()]
    rankings.sort()
    rankings.reverse()
    return rankings


print getRecommendedItems(recommendations.critics, itemsim, 'Toby')
print recommendations.getRecommendations(recommendations.critics, 'Toby')
