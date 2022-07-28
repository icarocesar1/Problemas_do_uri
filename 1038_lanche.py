
codigo,quantidade_item = input().split(" ")

codigo = int(codigo)
quantidade_item = int(quantidade_item)

if codigo == 1:
    total = 4 * quantidade_item
elif codigo == 2:
    total = 4.5 * quantidade_item
elif codigo == 3:
    total = 5 * quantidade_item
elif codigo == 4:
    total = 2 * quantidade_item
elif codigo == 5:
    total = 1.5 * quantidade_item

print ("Total: R$ %.2f" %(total ))
