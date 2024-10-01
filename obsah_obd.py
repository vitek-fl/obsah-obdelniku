def obsah_obdelniku():
    a = int(input("Zadej stranu a: "))
    b = int(input("Zadej stranu b: "))
    if a > 0 and b > 0:
        obsah = a * b
        print(f"Obsah je {obsah}.")
    else:
        print("Chyba, opakuj zadání.")
        obsah_obdelniku()

obsah_obdelniku()
