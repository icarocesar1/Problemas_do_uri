palavra_1 = input()
palavra_2 = input()
palavra_3 = input()

if palavra_1 == "vertebrado":
    if palavra_2 == "ave":
        if palavra_3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if palavra_3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if palavra_2 == "inseto":
        if palavra_3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if palavra_3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
