langd = int(input("Hur lång är du i cm = "))

#Kontroll om anv. får åka
if langd >= 130:
    print("Du får åka")
else:
    print("Du får inte åka")

print("-------------------------------------------------------\n")
#Testar värdet 129 för extra kontroll av värdet precis under gränsen att det visar rätt resultat
#version som automatiskt skriver ut en lista
test_vard = [121, 129, 130, 155]

for langd in test_vard:
    print(f"Testar längd: {langd} cm")
    if langd >= 130:
        print(" Du får åka!")
    else:
        print(" Du får inte åka")
    print()

#Denna testversion fått hjälp av kunnig person python