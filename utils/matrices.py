# RESULTADOS EN MATRICES

# donde:
# cada fila => un texto
# cada columna => una métrica

from .text_utils import formatear_valor
from .analisis import analizar_texto
from .textos_json import seleccionar_textos


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


def imprimir_matriz_metricas(metricas, matriz):
    encabezados = ["Texto"] + [m.replace("_", " ").capitalize() for m in metricas]
    filas = []
    for i, fila in enumerate(matriz):
        filas.append([str(i+1)] + [formatear_valor(x) for x in fila])
    anchos = [len(e) for e in encabezados]
    for fila in filas:
        for idx, celda in enumerate(fila):
            if len(celda) > anchos[idx]:
                anchos[idx] = len(celda)
    separador = "-".join("-" * (a + 2) for a in anchos)

    print("\nMATRIZ DE MÉTRICAS DE LOS TEXTOS")
    print(separador)
    print(" | ".join(encabezados[i].ljust(anchos[i]) for i in range(len(encabezados))))
    print(separador)
    for fila in filas:
        print(" | ".join(fila[i].ljust(anchos[i]) for i in range(len(fila))))
    print(separador)


def cargar_matriz_metricas(textos):
    if not textos:
        print("No hay textos cargados para generar la matriz.")
        return
    matriz, metricas = crear_matriz_metricas(textos)
    imprimir_matriz_metricas(metricas, matriz)

def promedio_metricas(matriz, claves):
    metricas_dict = {k: [] for k in claves}
    for fila in matriz:
        for j, val in enumerate(fila):
            metricas_dict[claves[j]].append(val)
    promedios = {}
    for k, valores in metricas_dict.items():
        promedios[k] = sum(valores) / len(valores) if len(valores) > 0 else 0
    return promedios

def promedios(textos):
    print("\nPROMEDIO DE MÉTRICAS ENTRE LOS TEXTOS")
    print("-" * 45)

    if not textos:
        print("No hay textos cargados.")
        print("-" * 45)
        return

    indices = seleccionar_textos(len(textos), minimo=1)
    if not indices:
        print("-" * 45)
        return

    textos_seleccionados = [textos[i] for i in indices]
    matriz, metricas = crear_matriz_metricas(textos_seleccionados)
    promedios = promedio_metricas(matriz, metricas)

    etiquetas = ", ".join(f"Texto {i+1}" for i in indices)
    print(f"Textos considerados: {etiquetas}")

    for metrica, valor in promedios.items():
        etiqueta = metrica.replace("_", " ").capitalize()
        if isinstance(valor, float):
            print(f"- {etiqueta}: {valor:.2f}")
        else:
            print(f"- {etiqueta}: {valor}")
    print("-" * 45)
