'''
1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! 
A program tartalmazza a függvény hívását is!
'''
lista = []
print("Adj meg számokat ha végeztél nyomj entert!")
while True:
  bekeres = input("Kérek számokat!\t")
  if bekeres == "":
    break
  else:
    lista.append(int(bekeres))

def osszegzo(lista):
    x = 0
    for szam in lista:
        x += szam
        
    return x
fuggvenyhivas = osszegzo(lista)
print(fuggvenyhivas)