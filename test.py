loop = 0
while loop <= 10:
    name = (input("seu nome: "))
    age = int(input("digite sua idade: "))
    arquivo = open("datab.txt", "w")
    arquivo.write(name)
    arquivo.close
