is_member = False
leve1 = 100
level2 = 300
discount = 0

price = input("Välkommen, köp något dyrt: ")
price = float(price)
if price > leve1:
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10
if price >= level2:
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

final_price = price * (100 - discount) / 100
print("Efter rabatter blir priset.... " + final_price)
# Strängen "Efter rabatten...... är en sträng och final_price är en float(tal)
# Konvertera final_price till en sträng.