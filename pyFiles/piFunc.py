def pi():
    sum = 0
    power = 2
    
    for i in range(1, 10001, 2):
        sum+=(-1)**power/i
        power+=1
    pi = sum*4

    return pi

print(pi())
