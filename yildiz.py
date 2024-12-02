satir = int(input("Kaç satır olsun? "))

for i in range(1, satir + 1): #artan
    print("*" * i)

for i in range(satir - 1, 0, -1): #azalan
    print("*" * i)

