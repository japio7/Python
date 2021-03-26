def greatestCommonDivisor(m, n):
    if n == 0:
        return m
    return greatestCommonDivisor(n, m % n)

print(greatestCommonDivisor(4746, 7854))
