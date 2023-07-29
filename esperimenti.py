lista =  [1, 2, 3, 3, 3, 4, 4, 5, 5]
a=0
b=0
for x,y in enumerate(lista):
    if lista.count(y)>a:
        a=lista.count(y)
        b=x
print(lista[b])



