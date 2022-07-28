
valor = int(input())

nota_100 = valor/100
resto = valor % 100
nota_50 = resto/50
resto = resto % 50
nota_20 = resto/20
resto = resto%20
nota_10 = resto/10
resto = resto % 10
nota_5 = resto/5
resto = resto % 5
nota_2 = resto/2
resto = resto % 2
nota_1 = resto / 1

print(valor)
print("%i nota(s) de R$ 100,00" %(nota_100))
print("%i nota(s) de R$ 50,00" %(nota_50))
print("%i nota(s) de R$ 20,00" %(nota_20))
print("%i nota(s) de R$ 10,00" %(nota_10))
print("%i nota(s) de R$ 5,00" %(nota_5))
print("%i nota(s) de R$ 2,00" %(nota_2))
print("%i nota(s) de R$ 1,00" %(nota_1))
