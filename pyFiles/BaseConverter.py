# Enter a number in base10 to convert to a different base
# Enter a base to convert the given base10 number to

def base_conv(num, base):
    array = []
    numbers = []
    x = num//base
    r = num % base
    array.append(str(r))
    while x >= 1:
        r = x % base
        x = x//base
        array.append(str(r))
    for i in range(len(array)):
        if array[i] == "10":
            array[i] = "a"
        elif array[i] == "11":
            array[i] = "b"
        elif array[i] == "12":
            array[i] = "c"
        elif array[i] == "13":
            array[i] = "d"
        elif array[i] == "14":
            array[i] = "e"
        elif array[i] == "15":
            array[i] = "f"
    array.reverse()
    cNum = ""
    for k in array:
        cNum+=str(k)
    return cNum

def main():
    a = int(input("Enter number to convert: "))

    while a < 0:
        print("Enter a positive number!")
        a = int(input("Enter number to convert: "))
            
    b = int(input("Enter base: "))
        
    while b <= 1 or b > 16:
        print("Invalid base!")
        b = int(input("Enter base: "))
    
    print(base_conv(a, b))

main()
