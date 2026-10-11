birthday = 0

print("Set 1:")
print(" 1  3  5  7")
print(" 9 11 13 15")
print("17 19 21 23")
print("25 27 29 31")
if int(input("Doğum gününüz bu setdə varmı? (1/0): ")) == 1:
    birthday += 1

print("\nSet 2:")
print(" 2  3  6  7")
print("10 11 14 15")
print("18 19 22 23")
print("26 27 30 31")
if int(input("Doğum gününüz bu setdə varmı? (1/0): ")) == 1:
    birthday += 2

print("\nSet 3:")
print(" 4  5  6  7")
print("12 13 14 15")
print("20 21 22 23")
print("28 29 30 31")
if int(input("Doğum gününüz bu setdə varmı? (1/0): ")) == 1:
    birthday += 4

print("\nSet 4:")
print(" 8  9 10 11")
print("12 13 14 15")
print("24 25 26 27")
print("28 29 30 31")
if int(input("Doğum gününüz bu setdə varmı? (1/0): ")) == 1:
    birthday += 8

print("\nSet 5:")
print("16 17 18 19")
print("20 21 22 23")
print("24 25 26 27")
print("28 29 30 31")
if int(input("Doğum gününüz bu setdə varmı? (1/0): ")) == 1:
    birthday += 16

print(f"\nSizin doğum gününüz:",birthday)