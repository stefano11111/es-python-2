
l=[{"a":2},{"b":1}] 
l.sort(key=lambda x: [x[y] for y in x] )
print(l)

