def normalizar(palabra: str):
    for char in palabra:
        if not char.isalpha():
            palabra = palabra.replace(char, '')
    return palabra.lower()

def crear_lista_palabras(txt):
    lista_palabras = [normalizar(p) for p in txt.split(' ')]
    return lista_palabras