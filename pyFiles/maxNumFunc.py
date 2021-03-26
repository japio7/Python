def max(lst):
    y = True
    k = 1
    while k < len(lst)-1 and y:
        y = False
        for i in range(len(lst) - k):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                y = True
                max = lst[-1]
    return max
    
numbers = [8, 19, 3, 26, 28, 49, 109, 78, 21, 10]
print(max(numbers))
