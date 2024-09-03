def inverterString(string):
    stringInvertida = ""

    for i in range(len(string) - 1, -1, -1): #loop para percorrer a string de trás pra frente
        stringInvertida += string[i]
    return stringInvertida

string = input("Digite uma string para inverter: ")
stringInvertida = inverterString(string)

print("String original:", string)
print("String invertida:", stringInvertida)
