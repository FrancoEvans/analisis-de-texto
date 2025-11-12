from .text_utils import crear_lista_palabras, sumar_largos, singular_plural
from .textos_json import seleccionar_textos
import re

def info_basica_texto(txt):
    lista_palabras = crear_lista_palabras(txt)
    caracteres = len(txt)
    palabras = len(lista_palabras)
    lineas = len(txt.splitlines())
    letras = sumar_largos(lista_palabras)
    letras_promedio = letras / palabras if palabras > 0 else 0
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
    try:
        maximo = max(frecuencia.values())
    except ValueError:
        maximo = 0
    mas_frecuentes = []
    for palabra, cantidad in frecuencia.items():
        if cantidad == maximo:
            mas_frecuentes.append(palabra)

    return frecuencia, mas_frecuentes, maximo, unicas


def ranking_palabras(frecuencia, n=5):
    ordenadas = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)
    top_n_frecuentes = ordenadas[:n]
    return top_n_frecuentes

def palabra_mas_larga(lista_palabras, i=0, mayores=None):
    if not lista_palabras:
        return []
    if mayores is None:
        mayores = [lista_palabras[0]]
    if i == len(lista_palabras):
        return mayores

    palabra = lista_palabras[i]
    if len(palabra) > len(mayores[0]):
        mayores = [palabra]
    elif len(palabra) == len(mayores[0]) and palabra not in mayores:
        mayores.append(palabra)

    return palabra_mas_larga(lista_palabras, i + 1, mayores)



def calcular_densidad_lexica(lista_palabras):
    return len(set(lista_palabras)) / len(lista_palabras) if lista_palabras else 0

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
            longitud_frecuencia[longitud] = (longitud_frecuencia[longitud] / total) * 100 if total > 0 else 0
        else:
            longitud_frecuencia[longitud] = longitud_frecuencia[longitud] / total if total > 0 else 0
    return longitud_frecuencia


def top_palabras(textos):
    print("\nTOP DE PALABRAS MÁS FRECUENTES")
    print("-" * 35)

    indices = seleccionar_textos(len(textos), minimo=1)
    if not indices:
        return

    try:
        cant_palabras = int(input("¿Cuántas palabras mostrar?: "))
        if cant_palabras <= 0:
            print("Ingrese un número mayor que 0.")
            return
    except ValueError:
        print("Ingrese un número válido.")
        return

    for idx in indices:
        txt = textos[idx]
        lista_palabras = crear_lista_palabras(txt)
        frecuencia, _, _, _ = frecuencia_palabras(lista_palabras)
        top_n = ranking_palabras(frecuencia, cant_palabras)

        print(f"Texto {idx+1}:")
        if not top_n:
            print("  No hay palabras.")
        else:
            for j, (palabra, veces) in enumerate(top_n, start=1):
                print(f"  {j}) {palabra}: {veces} {singular_plural(veces, 'vez', 'veces')}")
        print("-" * 35)

def palabras_unicas_textos(textos):
    print("\nPALABRAS ÚNICAS EN LOS TEXTOS")
    print("-" * 35)

    indices = seleccionar_textos(len(textos), minimo=1)
    if not indices:
        return

    for idx in indices:
        txt = textos[idx]
        lista_palabras = crear_lista_palabras(txt)
        _, _, _, unicas = frecuencia_palabras(lista_palabras)
        print(f"Texto {idx+1}:")
        if len(unicas) == 0:
            print("  Palabras Únicas: No hay")
        elif len(unicas) == 1:
            print(f"  Palabra Única (1): {unicas}")
        else:
            print(f"  Palabras Únicas ({len(unicas)}): {unicas}")
        print("-" * 35)


