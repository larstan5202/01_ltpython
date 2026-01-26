# =====================================
# FELAKTIG VERSION
# =====================================
def felaktig_version():
    print("=== Felaktig version ===")
    is_member = False
    level1 = 100
    level2 = 300
    discount = 0

    try:
        price = float(input("Välkommen, köp något dyrt (felaktig version): "))

        if price > level1:
            print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
            discount = discount + 10
        if price > level2:
            print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt")
            discount = discount + 25

        final_price = price * (100 - discount) / 100
        # Detta är raden som normalt kraschar:
        print("Efter rabatter blir priser...." + final_price)

    except TypeError as e:
        print(f"Oops! Ett fel uppstod: {e}")
        print("Detta beror på att man inte kan addera en sträng och ett tal direkt.\n")


# =====================================
# RÄTTAD VERSION
# =====================================
def rattad_version():
    print("=== Rättad version ===")
    level1 = 100
    level2 = 300
    discount = 0

    price = float(input("Välkommen, köp något dyrt (rättad version): "))

    if price > level2:
        discount = 25
        print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    elif price > level1:
        discount = 10
        print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    else:
        print("Ingen rabatt denna gång.")

    final_price = price * (100 - discount) / 100
    print(f"Efter rabatter blir priset: {final_price:.2f} kr\n")


# =====================================
# KÖRNING
# =====================================
felaktig_version()
rattad_version()

