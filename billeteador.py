# perimetro
print("programa para la resolucion de ecuacion primer grado")
a = float(input("valor de a: "))
b = a // 500
c = a % 500
print("billetes de 500: ", b)
if c != 0:
    d = c // 200
    e = c % 200
    print("billetes de 200: ", d)
    if e != 0:
        f = e // 100
        g = e % 100
        print("billetes de 100: ", f)
        if g != 0:
            h = g // 50
            i = g % 50
            print("billetes de 50: ", h)
            if i != 0:
                j = i // 20
                k = i % 20
                print("billetes de 20: ", j)
                if k != 0:
                    l = k // 10
                    m = k % 10
                    print("billetes de 10: ", l)
                    if m != 0:
                        n = m // 5
                        o = m % 5
                        print("billetes de 5: ", n)
                        if o != 0:
                            p = o // 2
                            q = o % 2
                            print("monedas de 2: ", p)
                            if q != 0:
                                s = q % 1
                                r = q // 1
                                print("monedas de 1: ", r)

print("quedan este resto", s)
X = str(input("quieres calculas la calderilla S/N: "))
if X != "S":
    print("gracias por participar")
if X == "S" or "s":
    P = int(s * 100)
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
