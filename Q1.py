#!/usr/bin/python

x = 2           #Atribui a x o valor 2
y = 5           #Atribui a y o valor 5
if y > 8:       #Compara y com 8. Nesse caso, y nao eh maior que 8, entao ele pula pro laco do else, que multiplica x com dois que da 4
    y *= 2
else:
    x *= 2
print(x+y)      #imprime o valor da soma de 4 com 5, que eh 9.