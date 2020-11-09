#perimetro
print('programa para calcular billetes')
cantidad=float(input('valor de a: '))
decimales = cantidad *100 % 100
entero=int(cantidad)
a = entero // 500
resto = entero % 500
print('billetes de 500: ', a)
if resto==0 and decimales==0:
    exit()
else:
    a = resto // 200
    resto = resto % 200
    print('billetes de 200: ',a)
    if resto==0 and decimales==0:
        exit()
    else:
        a = resto // 100
        resto = resto % 100
        print('billetes de 100: ',a)
        if resto==0 and decimales==0 :
            exit()
        else:
            a = resto // 50
            resto = resto % 50
            print('billetes de 50: ',a)
            if resto==0 and decimales==0:
                exit()
            else:
                a = resto // 20
                resto = resto % 20
                print('billetes de 20: ',a)
                if resto==0 and decimales==0:
                    exit()
                else:
                    a = resto // 10
                    resto = resto % 10
                    print('billetes de 10: ',a)
                    if resto==0 and decimales==0:
                        exit()
                    else:
                        a = resto // 5
                        resto = resto % 5
                        print('billetes de 5: ',a)
                        if resto==0 and decimales==0:
                            exit()
                        else:
                            a = resto // 2
                            resto = resto % 2
                            print('monedas de 2: ',a)
                            if resto==0 and decimales==0:
                                exit()
                            else:
                                a = resto // 1
                                resto = resto % 1
                                print('monedas de 1: ',a)
                                if decimales==0:
                                    exit()
                                else:
                                    print('quedan estos centimos', int (decimales))
                                    x=str (input('quieres calcular la calderilla? S/N: '))
                                    if x!='S' and x!='s':
                                        print('gracias por participar')
                                        exit()
                                    else:
                                        b = decimales // 50
                                        resto = decimales % 50
                                        print('monedas de 0.50: ', b)
                                        if resto==0:
                                            exit()
                                        else:
                                            b = resto // 20
                                            resto = resto % 20
                                            print('monedas de 0.20: ',b)
                                            if resto==0:
                                                exit()
                                            else:
                                                b = resto // 10
                                                resto = resto % 10
                                                print('monedas de 0.10: ',b)
                                                if resto==0:
                                                    exit()
                                                else:
                                                    b = resto // 5
                                                    resto = resto % 5
                                                    print('monedas de 0.05: ',b)
                                                    if resto==0:
                                                        exit()
                                                    else:
                                                        b = resto // 2
                                                        resto = resto % 2
                                                        print('monedas de 0.02: ',b)
                                                        if resto==0:
                                                            exit()
                                                        else:
                                                            b = resto // 1
                                                            resto = resto % 1
                                                            print('monedas de 0.01: ',b)
                                                            if resto==0:
                                                                exit()








