def toh(n, first, spare, finish):
    if n == 0:
        return

    #Move n-1 disks from first to spare.
    toh(n-1, first, finish, spare)
    print(f"Move disk from {first} to {finish}")

    #Move n-1 disks from spare to finish using first as spare.
    toh(n-1, spare, first, finish)

toh(5, 1, 2, 3)
