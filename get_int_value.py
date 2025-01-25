def get_int_value():
    while True:
        try:
            msg = int(input("Valeur ? "))
            return msg
        except ValueError:
            print("Indiquez bien une valeur numérique.")