"""pesos = input("¿Cuantos pesos mexicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 20
dolares = pesos / valor_dolar                           
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + "dolares")
menu = 
Bienvenido al conversor de monedas 🐱‍👤
1 - pesos colombianos
2 - pesos argentinos
3 - pesos mexicanos
Elige una option: """

opcion = int(input(menu))
if opcion == 1:
    dolares = input("¿Cuantos dolares tienes?: ")
    dolares = float(dolares)
    valor_pesos = 0.050
    pesos = dolares/ valor_pesos
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print ("tienes $" + pesos + "pesos")
if opcion == 2:
    dolares = input("¿Cuantos dolares tienes?: ")
    dolares = float(dolares)
    valor_pesos = 0.050
    pesos = dolares/ valor_pesos
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print ("tienes $" + pesos + "pesos")
elif opcion == 3:
    dolares = input("¿Cuantos dolares tienes?: ")
    dolares = float(dolares)
    valor_pesos = 0.050
    pesos = dolares/ valor_pesos
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print ("tienes $" + pesos + "pesos")
else:
    print("Ingrese una opcion correcta")
