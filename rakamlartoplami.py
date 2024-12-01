sayi=int(input("Bir sayı giriniz:"))
str_sayi= str(sayi)
toplam=0
for i in str_sayi:
    toplam += int(i)
print(toplam)