str = 'fraanevanss@gmail.com'

for index, char in enumerate(str):
    if not char.isalpha():
        str = str.replace(char, ' ')
lista = str.split(' ')
direccion = lista[0]
dominio = '.'.join([lista[1], lista[2]])
print(direccion)
print(dominio)

# eliminar un caracter

# str = "HOLA"
# for i,c in enumerate(str):
#     nuevo_str = str[:i] + str[i+1:]
#     print(f'{c}: {nuevo_str}')

