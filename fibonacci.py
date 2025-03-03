def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        

fibo = fibonacci(10)
for num in fibo:
    print(num)  
