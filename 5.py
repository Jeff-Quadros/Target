def inverter_string(string):
    return string[::-1]

string = input("Digite uma string para inverter seus caracteres: ")
string_invertida = inverter_string(string)
print("String original:", string)
print("String invertida:", string_invertida)
