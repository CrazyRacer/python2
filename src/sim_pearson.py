# coding=utf-8
from math import sqrt
import recommendations


def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    n = len(si)
    if len(si) == 0:
        return 1

    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0
    r = num / den
    return r

# data = [recommendations.Person1, recommendations.Person2, recommendations.Person3, recommendations.Person4,
#         recommendations.Person5, recommendations.Person6]
# for item in data:
#     for item2 in data:
#         if item != item2:
#             print item + "与" + item2 + "的相似度为" + str(sim_pearson(recommendations.critics, item, item2))
