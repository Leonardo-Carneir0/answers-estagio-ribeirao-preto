s = input("Por favor, insira uma string: ")
s_invertida = ""
for i in range(len(s)-1, -1, -1):
    s_invertida += s[i]
print("A string invertida é:", s_invertida)
