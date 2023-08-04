def prodDigits(n):
    product = 1
    while n > 0:
        digit = n % 10
        product *= digit
        n //= 10
    return product
def MDR(n):
    while n >= 10:
        n = prodDigits(n)
    return n
def MPersistence(n):
    persistence = 0
    while n >= 10:
        n = prodDigits(n)
        persistence += 1
    return persistence
num = 86
mdr = MDR(num)
mpersistence = MPersistence(num)

print("Number:", num)
print("Multiplicative Digital Root (MDR):", mdr)
print("Multiplicative Persistence (MPersistence):", mpersistence)
