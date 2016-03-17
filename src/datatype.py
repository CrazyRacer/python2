number_list = [1, 2, 3, 4]
string_list = ['a', 'b']
mixed_list = ['a', 3, 'b']

ages = {'John': 24, 'Sarah': 28}

print string_list[1]
print ages['Sarah']

x = 1
l = 1
if x == l:
    print 'x is l'
    print 'Still i n i f b1ock'
print ' outs ide if block '

l1 =[1,2,3,4,5,6,7,8,9]
print [v*10 for v in l1 if v>4]


timesten = dict([(v,v*10) for v in l1 ])
print timesten