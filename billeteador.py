#billeteador
print('programa para calcular billetes')
#variables
cantidad=float(input('valor de a: '))
decimales =int( cantidad *100 % 100)
resto = int(cantidad)
#condicion centimos
if decimales>0:
    print('tienes estos centimos', int (decimales))
    x=str (input('quieres calcular la calderilla? S/N: '))
    if x!='S' and x!='s':
        decimales=0

 #calculo de enteros

if resto>500:
    a = resto // 500
    resto = resto % 500
    print('billetes de 500: ', a)
if resto==0 and decimales==0:
    exit()

if resto>=200:
    a = resto // 200
    resto = resto % 200
    print('billetes de 200: ',a)
if resto==0 and decimales==0:
    exit()

if resto>=100:
    a = resto // 100
    resto = resto % 100
    print('billetes de 100: ',a)
if resto==0 and decimales==0 :
        exit()

if resto>=50:
    a = resto // 50
    resto = resto % 50
    print('billetes de 50: ',a)
if resto==0 and decimales==0:
    exit()
if resto>=20:
    a = resto // 20
    resto = resto % 20
    print('billetes de 20: ',a)
if resto==0 and decimales==0:
    exit()
if resto>=10:
    a = resto // 10
    resto = resto % 10
    print('billetes de 10: ',a)
if resto==0 and decimales==0:
    exit()
if resto>=5:
    a = resto // 5
    resto = resto % 5
    print('billetes de 5: ',a)
if resto==0 and decimales==0:
    exit()
if resto>=2:
    a = resto // 2
    resto = resto % 2
    print('monedas de 2: ',a)
if resto==0 and decimales==0:
    exit()
if resto>=1:
    a = resto // 1
    resto = resto % 1
    print('monedas de 1: ',a)
if decimales==0:
    exit()

 #calculo de decimales

if decimales>=50:
    b = decimales // 50
    decimales = decimales % 50
    print('monedas de 0.50: ', b)
if decimales==0:
    exit()
if decimales>=20:
    b = decimales // 20
    decimales = decimales % 20
    print('monedas de 0.20: ',b)
if decimales==0:
    exit()
if decimales>=10:
    b = decimales // 10
    decimales = decimales % 10
    print('monedas de 0.10: ',b)
if decimales==0:
    exit()
if decimales>=5:
    b = decimales // 5
    decimales = decimales % 5
    print('monedas de 0.05: ',b)
if decimales==0:
    exit()
if decimales>=2:
    b = decimales // 2
    decimales = decimales % 2
    print('monedas de 0.02: ',b)
if decimales==0:
    exit()
if decimales>=1: 
    b = decimales // 1
    decimales = decimales % 1
    print('monedas de 0.01: ',b)








