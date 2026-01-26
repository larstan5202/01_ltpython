print("Matchen är slut, nu kan vi räkna ut resultatet!")

#Fråga antal mål
tottenham = int(input("Hur många mål gjorde Tottenham? "))
liverpool = int(input("Hur många mål gjorde Liverpool? "))

#Kontroll vem som segrade
if tottenham > liverpool:
    print("Tottenham segrade!")
elif liverpool > tottenham:
    print("Liverpool segrade!")
print("--------------------------------------------------------------\n")

# Om det blev oavgjort
print("Matchen är slut, nu ska vi räkna ut vem som vann eller om det blev oavgjort!")

#Fråga om antal mål

tottenham = int(input("Hur många mål gjorde Tottenham? "))
liverpool = int(input("Hu många mål gjorde Liverpool? "))

if tottenham > liverpool:
    print("Tottenham segrade!")
elif liverpool > tottenham:
    print("Liverpool segrade!")
else:
    print("Matchen slutade oavgjort!")
