# coding=utf-8
a = 80000
b = 200000
ano = 0
while b > a:
    a += (a * 0.03)
    b += (b * 0.015)
    ano +=1
    print ("O total de anos necessários é: %d" %ano)
