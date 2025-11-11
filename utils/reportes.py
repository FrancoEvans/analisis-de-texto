from .metricas import (
    info_basica_texto,
    palabra_mas_larga,
    frecuencia_palabras,
    calcular_densidad_lexica,
    distribucion_longitudes
)
from .text_utils import crear_lista_palabras



def analizar_texto(txt):
    caracteres, palabras, lineas, oraciones, letras_promedio, lista_palabras = info_basica_texto(txt)

    palabras_mas_largas = palabra_mas_larga(lista_palabras)
    frecuencia, mas_frecuentes, maximo, unicas = frecuencia_palabras(lista_palabras)
    densidad_lexica = calcular_densidad_lexica(lista_palabras)
    frecuencia_longitudes = distribucion_longitudes(lista_palabras)

    resultados = {
        "caracteres": caracteres,
        "palabras": palabras,
        "lineas": lineas,
        "oraciones": len(oraciones),
        "promedio_letras": round(letras_promedio),
        "palabras_mas_largas": palabras_mas_largas,
        "longitud_palabra_mas_larga": len(palabras_mas_largas[0]) if palabras_mas_largas else 0,
        "frecuencia": frecuencia,
        "mas_frecuentes": mas_frecuentes,
        "maximo": maximo,
        "unicas": unicas,
        "densidad_lexica": densidad_lexica,
        "longitudes_frecuencia": frecuencia_longitudes
    }

    return resultados


def reporte(resultados):
    reporte = f'''REPORTE
    caracteres: {resultados["caracteres"]}
    palabras: {resultados["palabras"]}
    lineas: {resultados["lineas"]}
    oraciones: {resultados["oraciones"]}
    palabra/s más larga/s: {str(resultados["palabras_mas_largas"])} ({resultados["longitud_palabra_mas_larga"]} caracteres)
    promedio de caracteres por palabra: {resultados["promedio_letras"]}
    frecuencia: {resultados["frecuencia"]}
    más frecuentes: {resultados["mas_frecuentes"]}
    máximo: {resultados["maximo"]}
    únicas : {resultados["unicas"]}
    densidad léxica: {resultados["densidad_lexica"]}
    longitudes frecuencia: {resultados["longitudes_frecuencia"]}
    '''
    print(reporte)
    return reporte



def comparar_textos(textos):
    if len(textos) < 2:
        print("minimo 2 textos")
        return

    sets = [set(crear_lista_palabras(txt)) for txt in textos]
    interseccion = set.intersection(*sets)
    union = set.union(*sets)
    jaccard = len(interseccion) / len(union)

    print("palabras compartidas entre todos:", interseccion)
    print(f"similitud de jaccard: {jaccard:.2f}")


# FUNCION PARA EL FUTURO

# import re
# def buscar_palabra(palabra: str, texto: str):
#     resultado = re.findall(rf'\b{palabra.lower()}\b', texto.lower())
#     print(f'{palabra.upper()} aparece {len(resultado)} veces')




# RESULTADOS EN MATRICES

# donde:
# cada fila => un texto
# cada columna => una métrica


def crear_matriz_metricas(textos):
    metricas = [
        "caracteres",
        "palabras",
        "lineas",
        "promedio_letras",
        "longitud_palabra_mas_larga",
        "maximo",
        "densidad_lexica"
    ]

    matriz = []
    for txt in textos:
        resultados = analizar_texto(txt)
        fila = [resultados[k] for k in metricas]
        matriz.append(fila)

    return matriz, metricas


def promedio_metricas(matriz, claves):
    metricas_dict = {k: [] for k in claves}

    for fila in matriz:
        for j, val in enumerate(fila):
            metricas_dict[claves[j]].append(val)

    promedios = {}
    for k, valores in metricas_dict.items():
        promedios[k] = sum(valores) / len(valores)

    return promedios

    # [[metrica1, metrica1, metrica1],
    # [metrica2, metrica2, metrica2],
    # [metrica3, metrica3, metrica3]]

