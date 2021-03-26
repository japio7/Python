def fib(num):
    fibs = []
    a = 0
    b = 1
    for i in range(num):
        new = a + b
        a = b
        b = new
        fibs.append(new)
    return fibs

print(fib(10))
