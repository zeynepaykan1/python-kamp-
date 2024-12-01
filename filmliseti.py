mod = int((input("Bugün kendini 10 üzerinden kaç hissediyorsun?: ")))
uzgunfilm='Issız Adam, Titanic, Recep İvedik'
normalfilm='Alacakaranlık, Spider-Man, Recep İvedik'
komikfilm='G.O.R.A., A.R.O.G., Recep İvedik '

if 0<= mod <=3:
    decision = str(input("Sana izlemen için birkaç film önerememi ister misin? (Y/N):  "))
    if decision =="Y" or decision =="y":
        print(uzgunfilm, "umarım önerilerimi beğenirsin ve daha iyi hissedersin.")
    else:
        print("Sen bilirsin, kendine dikkat et")
if 4<= mod <=7:
    decision=str(input("Sana izlemen için birkaç film önermemi ister misin? (Y/N):  "))
    if decision =="Y" or decision =="y":
        print(normalfilm, "umarım daha da iyi hissedersin.")
    else:
        print("Sen bilirsin, kendine dikkat et")
if 8<= mod <=10:
    decision=str(input("Modunun iyi olmasına çok sevindim, daha da iyi olman için sana birkça film önermemi ister misin? (Y/N):  "))
    if decision =="Y" or decision =="y":
        print(komikfilm, "umarım hep modun böyle iyi olur :) ")
for mod in range(mod,mod+1):
    print("Bu kadar iyi olmana çok sevindim, kendine iyi bak")
