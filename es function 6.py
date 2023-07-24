def fib(n):
    if n<=1:
        f=1
    else:
        f=fib(n-1)+fib(n-2)
    return f
for x in range(5):
    print(fib(x))








    


    
