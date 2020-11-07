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
X = str(input("quieres calculas la calderilla S/N: "))
if X != "S":
    print("gracias por participar")
if X == "S" or "s":
    P = int(resto * 100)
    t = P // 50
    u = P % 50
    print(P)
    print("monedas de 0.50: ", t)
    if u != 0:
        v = u // 20
        w = u % 20
        print("monedas de 0.20: ", v)
        if w != 0:
            y = w // 10
            z = w % 10
            print("monedas de 0.10: ", y)
            if z != 0:
                A = z // 5
                B = z % 5
                print("monedas de 0.05: ", A)
                if B != 0:
                    C = B // 2
                    D = B % 2
                    print("monedas de 0.02: ", C)
                    if D != 0:
                        E = D % 1
                        F = D // 1
                        print("monedas de 0.01: ", F)
