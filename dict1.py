#users = [{"id":0,"name":"Hero"},{"id":1,"name":"Dunn"},{"id":2,"name":"Sue"},{"id":3,"name":"Chi"},{"id":4,"name":"Thor"}]
pairs = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4)]
d={}
for i,j in pairs:
    if i in d:
        d[i].append(j)
    else:
        d[i]=[j]

for i,j in pairs:
    if j in d:
        d[j].append(i)
    else:
        d[j]=[i]
print(d)
