import recommendations
from sim_pearson import sim_pearson


def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

print topMatches(recommendations.critics,recommendations.Person6,n=5)
