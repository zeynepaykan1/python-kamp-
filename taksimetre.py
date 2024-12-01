km_fyt = 17
acilis= 30
min_ucret= 150
mesafeler = {
    "havaalanı": 15.0,
    "lens": 8.0,
    "okan": 12.5,
    "metro": 5.0,
    "viaport": 10.0
}

print("Hoşgeldiniz, nereye gitmek istersiniz?")
for key in mesafeler:
    print(key)
key = input("Gidilecek yeri girin: ").strip().lower()


if key in mesafeler:
    mesafe = mesafeler[key]
    ücret = mesafe * km_fyt + acilis
    print(f"Gidilen mesafe: {mesafe:.2f} km")
    print(f"Toplam ücret: {ücret:.2f} TL")
else:
    print("Oraya gidemem.")
if min_ucret <= 150:
    print("İndi-Bindi ücreti alıyorum, toplam ödeme",min_ucret,"TL.")
else:
    print(f"Gidilecek mesafe: {mesafe:.2f} km")
    print(f"Ücret: {ücret:.2f} TL")