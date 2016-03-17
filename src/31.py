from recommendations import critics
from math import sqrt

print critics['Lisa Rose']['Lady in the Water']
print critics['Mick LaSalle']

a = sqrt(pow(critics['Toby']['Snakes on a Plane'] - critics['Mick LaSalle']['Snakes on a Plane'], 2) + pow(
    critics['Toby']['You, Me and Dupree'] - critics['Mick LaSalle']['You, Me and Dupree'], 2))

print 1/(1+a)
