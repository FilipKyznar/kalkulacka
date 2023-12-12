x = input("zadejte promenu x:  ")
y = input("zadejte promenu y:  ")

x = int(x)
y = int(y)

print("pro sčítání zadejte +")
print("pro odčítání zadejte -")
print("pro dělení zadejte /")
print("pro násobení zadejte *")
print("pro mocnění zadejte **")
print("pro odmocnění zadejte /*")

znamenko = input("zvolte si operátor")

if znamenko == "+":
    vysledek = x + y
    vysledek = str(vysledek)
    print("Výsledek je: " + vysledek)
elif znamenko == "-":
    vysledek = x - y
    vysledek = str(vysledek)
    print("Výsledek je: " + vysledek)
elif znamenko == "*":
    vysledek = x * y
    vysledek = str(vysledek)
    print("Výsledek je: " + vysledek)
elif znamenko == "/":
    if y != 0:
        vysledek = x / y
        vysledek = str(vysledek)
        print("Výsledek je: " + vysledek)
    else:
        print("Nemůžeš dělit nulou")
elif znamenko == "**":
    vysledek = x ** y
    vysledek = str(vysledek)
    print("Výsledek je: " + vysledek)
elif znamenko == "/*":
    vysledek = x /* y
    vysledek = str(vysledek)
    print("Výsledek je: " + vysledek)
    if 
           