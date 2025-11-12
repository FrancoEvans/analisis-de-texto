from .metricas import (
    info_basica_texto,
    palabra_mas_larga,
    frecuencia_palabras,
    calcular_densidad_lexica,
    distribucion_longitudes
)
from .text_utils import crear_lista_palabras
from .textos_json import seleccionar_textos

def analizar_texto(txt):
    try:
        caracteres, palabras, lineas, letras_promedio, lista_palabras = info_basica_texto(txt)
        palabras_mas_largas = palabra_mas_larga(lista_palabras)
        frecuencia, mas_frecuentes, maximo, unicas = frecuencia_palabras(lista_palabras)
        densidad_lexica = calcular_densidad_lexica(lista_palabras)
        frecuencia_longitudes = distribucion_longitudes(lista_palabras)


        resultados = {
            "caracteres": caracteres,
            "palabras": palabras,
            "lineas": lineas,
            "promedio_letras": round(letras_promedio) if palabras > 0 else 0,
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

    except Exception:
        print("Ocurrió un error al analizar el texto. Se devolverán valores vacíos.")
        resultados = {
            "caracteres": 0,
            "palabras": 0,
            "lineas": 0,
            "promedio_letras": 0,
            "palabras_mas_largas": [],
            "longitud_palabra_mas_larga": 0,
            "frecuencia": {},
            "mas_frecuentes": [],
            "maximo": 0,
            "unicas": [],
            "densidad_lexica": 0,
            "longitudes_frecuencia": {}
        }
        return resultados


def mostrar_textos(textos, i=0):
    if i == 0:
        print("\n==============================")
        print("       TEXTOS CARGADOS")
        print("==============================")
        if not textos:
            print("No hay textos cargados.\n")
            return
    if i == len(textos):
        return

    print(f"\nTEXTO {i+1}")
    print(textos[i])
    mostrar_textos(textos, i + 1)


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
        print("Se necesitan al menos 2 textos para comparar.")
        return

    print("\nCOMPARACIÓN ENTRE TEXTOS")
    indices = seleccionar_textos(len(textos), minimo=2)
    if not indices:
        return

    textos_seleccionados = [textos[i] for i in indices]
    sets = [set(crear_lista_palabras(txt)) for txt in textos_seleccionados]

    interseccion = set.intersection(*sets)
    union = set.union(*sets)
    jaccard = len(interseccion) / len(union) if len(union) > 0 else 0

    textos_usados = ", ".join(f"Texto {i+1}" for i in indices)

    print(f"Textos considerados: {textos_usados}")
    if len(interseccion) == 0:
        print("Palabras compartidas entre todos los textos seleccionados: No hay")
    else:
        print(f"Palabras compartidas entre todos los textos seleccionados: {interseccion}")
    print(f"Índice de similitud de Jaccard: {jaccard:.2f}\n")


# FUNCION PARA EL FUTURO

# import re
# def buscar_palabra(palabra: str, texto: str):
#     resultado = re.findall(rf'\b{palabra.lower()}\b', texto.lower())
#     print(f'{palabra.upper()} aparece {len(resultado)} veces')



