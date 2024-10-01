a = int(input("Zadej stranu a: "))
b = int(input("Zadej stranu b: "))
if a > 0 and b > 0:
    obsah = a * b
    print(f"Obsah obdelníku o stranách o velikosti {a} cm a {b} cm je {obsah}.")
else:
    print("Error - špatně zadané hodnoty")