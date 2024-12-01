sayi=int(input("Bir sayı giriniz:"))
bolen_sayisi =0
for i in range (1, sayi+1):
    if sayi %i == 0:
        bolen_sayisi +=1 #eğer sayının böleni varsa bolen sayisini 1 arttır.
print(f"{sayi} sayısının {bolen_sayisi} tane böleni vardır")