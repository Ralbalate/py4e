# perimetro
print("programa para la resolucion de ecuacion primer grado")
inicial = float(input("valor de a: "))
cantidad = inicial // 500
resto = inicial % 500
print("billetes de 500: ", cantidad)
if resto != 0:
    cantidad = resto // 200
    resto = resto % 200
    print("billetes de 200: ", cantidad)
    if resto != 0:
        cantidad = resto // 100
        resto = resto % 100
        print("billetes de 100: ", cantidad)
        if resto != 0:
            cantidad = resto // 50
            resto = resto % 50
            print("billetes de 50: ", cantidad)
            if resto != 0:
                cantidad = resto // 20
                resto = resto % 20
                print("billetes de 20: ", cantidad)
                if resto != 0:
                    cantidad = resto // 10
                    resto = resto % 10
                    print("billetes de 10: ", cantidad)
                    if resto != 0:
                        cantidad = resto // 5
                        resto = resto % 5
                        print("billetes de 5: ", cantidad)
                        if resto != 0:
                            cantidad = resto // 2
                            resto = resto % 2
                            print("monedas de 2: ", cantidad)
                            if resto != 0:
                                cantidad = resto // 1
                                resto = resto % 1
                                print("monedas de 1: ", cantidad)

print("quedan este resto", resto)
seguir = str(input("quieres calculas la calderilla S/N: "))
if seguir != "S":
    print("gracias por participar")
if seguir == "S" or "s":
    resto = int(resto * 100)
    print(resto)
    cantidad = resto // 50
    resto = resto % 50
    print("monedas de 0.50: ", cantidad)
    if  != 0:
        cantidad = resto // 20
        resto = resto % 20
        print("monedas de 0.20: ", cantidad)
        if resto != 0:
            cantidad = resto // 10
            resto = resto % 10
            print("monedas de 0.10: ", cantidad)
            if resto != 0:
                cantidad = resto // 5
                resto = resto % 5
                print("monedas de 0.05: ", cantidad)
                if resto != 0:
                    cantidad = resto // 2
                    resto = resto % 2
                    print("monedas de 0.02: ", cantidad)
                    if resto != 0:
                        cantidad = resto // 1
                        resto = resto % 1
                        print("monedas de 0.01: ", cantidad)
