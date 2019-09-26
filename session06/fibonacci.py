def fibonacci(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))
for i in range(1,20,1):
    print(fibonacci(i))




