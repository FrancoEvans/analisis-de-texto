def normalizar(palabra: str):
    try:
        for char in palabra:
            if not char.isalpha():
                palabra = palabra.replace(char, '')
        return palabra.lower()
    
    except AttributeError:
        print("Error. no se ingreso string. se devolvera un string vacio")
        return ""


def crear_lista_palabras(txt):
    try:
        lista_palabras = [p for p in [normalizar(p) for p in txt.split()] if p]
        return lista_palabras
    
    except AttributeError:
        print("Error. el texto no es una cadena válida. se devolvera una lista vacio")
        return []
    

def singular_plural(n, singular, plural):
    return singular if n == 1 else plural


def sumar_largos(lista, i=0):
    if i == len(lista):
        return 0
    return len(lista[i]) + sumar_largos(lista, i + 1)


def formatear_valor(v):
    return f"{v:.2f}" if isinstance(v, float) else str(v)