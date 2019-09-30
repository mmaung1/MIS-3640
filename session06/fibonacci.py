def fibonacci(n):
    if n == 0:
        return 1
    else:
        return fibonacci(n-1)*n

print(fibonacci(10))
for i in range(1,20,1):
    print(fibonacci(i))




