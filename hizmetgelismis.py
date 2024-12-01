isim = str(input("Öncelikle merhaba, ismini öğrenebilir miyim? : "))
while True:

    hizmetler = {"1": "Gelir Vergisi Hesaplama", "2": "ÖTV Hesaplama", "3": "Faiz Hesaplama"}
    print("Merhaba", isim, "hoşgeldin. Sana hangi hizmetimizle yardım etmemizi istersin ? ")
    print(hizmetler)
    talep = int(input("Lütfen istediğiniz hizmetin numarasını giriniz: "))
    if talep == 1:
        gelir = int(input(
            "Gelir Vergisi Hesaplama hizmetimizden yararlanmak için lütfen gelirini noktasız şekilde yazabilir misin?: "))
        print("Gelir Verginiz", gelir * 15 / 100, " TL olarak hesaplanmıştır.Hizmetimizi kullandığın için teşekkürler",
              isim, ".")
        devam = input("Devam etmek istiyor musunuz? (Evet/Hayır): ").strip().lower()
        if devam != "evet":
            print("Program sonlandırılıyor...")

    elif talep == 2:
        fiyat = int(input(
            "ÖTV hesaplama hizmetimizden yararlanmak için lütfen satın aldığın ürünün fiyatını noktasız şekilde yazabilir misin?: "))
        print("ÖTV'niz satın aldığınız", fiyat, "TL lik ürün için", fiyat * 20 / 100,
              "TL olarak hesaplanmıştır. Hizmetimizi kullandığın için teşekkürler.")
        devam = input("Devam etmek istiyor musunuz? (Evet/Hayır): ").strip().lower()
        if devam != "evet":
            print("Program sonlandırılıyor...")
    elif talep == 3:
        anapara = int(input(
            "Faiz Hesaplama hizmetimizden yararlanmak için lütfen faize koymak istediğiniz para miktarını noktasız şekilde yazınız: "))
        vade = int(input("Lütfen vade süresini sayı olarak yazınız (ay) :"))
        print("Hizmetimiz sonucu", anapara, "TL paranızın", vade, "ay boyunca faizde olması sonucunda toplam",
              anapara * 50 / 100 * vade, "TL kazanç sağlayacaksınız ve bankadaki toplam paranız",
              anapara + (anapara * 50 / 100 * vade), "Tl olacak. Hizmetimizi kullandığın için teşekkürler.")
        devam = input("Devam etmek istiyor musunuz? (Evet/Hayır): ").strip().lower()
        if devam != "evet":
            print("Program sonlandırılıyor...")
    else:
        talep = int(input("Lütfen geçerli bir hizmet numarası giriniz:"))


