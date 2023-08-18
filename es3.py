# Implement Fibonacci sequence as recursive function and print first 5 elements

def func(n):
    for x in range(n):
        if x<=1:
            x=1
        else:
            fib=func(x-1)+func(x-2)
            print(fib)
print(func(5))


 

