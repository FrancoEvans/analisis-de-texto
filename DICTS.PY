frase = input('ingrese una frase:\n')

lista_palabras = frase.split()

dic = {}
for palabra in lista_palabras:
    dic[palabra] = dic.get(palabra, 0) + 1

listado = []
for p in dic:
    listado.append(f'{p}: {str(dic[p])}')

for linea in listado:
    print(linea)