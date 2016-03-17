# coding=utf-8
from math import sqrt
import recommendations


# 最短距离 根号下(差的平方和)
def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if len(si) == 0: return 0
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])
    return 1 / (1 + sqrt(sum_of_squares))


# data = [recommendations.Person1, recommendations.Person2, recommendations.Person3, recommendations.Person4,
#         recommendations.Person5, recommendations.Person6]
# for item in data:
#     for item2 in data:
#         if item != item2:
#             print item + "与" + item2 + "的相似度为" + str(sim_distance(recommendations.critics, item, item2))
