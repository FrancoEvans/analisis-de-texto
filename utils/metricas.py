from .text_utils import crear_lista_palabras

def info_basica_texto(txt):
    lista_palabras = crear_lista_palabras(txt)

    caracteres = len(txt)
    palabras = len(txt.split(' '))
    lineas = len(txt.splitlines())

    letras = 0
    for p in lista_palabras:
        letras += len(p)

    letras_promedio = letras / palabras

    return caracteres, palabras, lineas, letras_promedio, lista_palabras


def frecuencia_palabras(lista_palabras):
    frecuencia = {}
    for palabra in lista_palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    unicas = []
    for palabra, cantidad in frecuencia.items():
        if cantidad == 1:
            unicas.append(palabra)
            
    maximo = max(frecuencia.values())

    mas_frecuentes = []
    for palabra, cantidad in frecuencia.items():
        if cantidad == maximo:
            mas_frecuentes.append(palabra)


    return frecuencia, mas_frecuentes, maximo, unicas


def ranking_palabras(frecuencia, n=5):
    ordenadas = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)
    top_n_frecuentes = ordenadas[:n]
    return top_n_frecuentes


def palabra_mas_larga(lista_palabras):
    if not lista_palabras:
        return []
    mayores = [lista_palabras[0]]
    for palabra in lista_palabras:
        if len(palabra) > len(mayores[0]):
            mayores.clear()
            mayores.append(palabra)
        elif len(palabra) == len(mayores[0]):
            if palabra not in mayores:
                mayores.append(palabra)
    return mayores


def calcular_densidad_lexica(lista_palabras):
    return len(set(lista_palabras)) / len(lista_palabras)


def distribucion_longitudes(lista_palabras, porcentaje=False):
    longitud_frecuencia = {}
    total = len(lista_palabras)

    for palabra in lista_palabras:
        longitud = len(palabra)
        if longitud in longitud_frecuencia:
            longitud_frecuencia[longitud] += 1
        else:
            longitud_frecuencia[longitud] = 1

    for longitud in longitud_frecuencia:
        if porcentaje:
            longitud_frecuencia[longitud] = (longitud_frecuencia[longitud] / total) * 100
        else:
            longitud_frecuencia[longitud] = longitud_frecuencia[longitud] / total

    return longitud_frecuencia