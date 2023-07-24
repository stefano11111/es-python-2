def fib(n):
    if n<=3:
        f=1
    else:
        f=fib(n-1)+fib(n-2)
    return f
print(fib(5))



