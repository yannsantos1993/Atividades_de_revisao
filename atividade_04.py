notas = []
contador = 0
ocorrencias = 4

while contador < ocorrencias:
    notas.append(int(input("Informe a nota por favor:")))
    contador+=1

media = sum(notas)/ocorrencias
print(f"as notas informadas foram: {notas} e a média dessas notas equivale a: {media}")