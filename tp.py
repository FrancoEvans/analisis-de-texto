
# PROGRAMA DE ANALISIS DE TEXTO



# MANEJO DE ARCHIVOS (PARA EL FUTURO):

# with open('texto_prueba1.txt', 'r', encoding='utf-8') as file:
#     txt = file.read()

# with open('texto_prueba2.txt', 'r', encoding='utf-8') as file:
#     txt2 = file.read()

# with open('texto_prueba3.txt', 'r', encoding='utf-8') as file:
#     txt3 = file.read()



# FUNCIONES UTILS

def normalizar(palabra: str):
    for char in palabra:
        if not char.isalpha():
            palabra = palabra.replace(char, '')
    return palabra.lower()

def crear_lista_palabras(txt):
    lista_palabras = [normalizar(p) for p in txt.split(' ')]
    return lista_palabras

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



# ANALISIS DE TEXTO Y REPORTE (CON LAS FUNCIONES UTILS)

def analizar_texto(txt):
    caracteres, palabras, lineas, letras_promedio, lista_palabras = info_basica_texto(txt)

    palabras_mas_largas = palabra_mas_larga(lista_palabras)
    frecuencia, mas_frecuentes, maximo, unicas = frecuencia_palabras(lista_palabras)
    densidad_lexica = calcular_densidad_lexica(lista_palabras)
    frecuencia_longitudes = distribucion_longitudes(lista_palabras)

    resultados = {
        "caracteres": caracteres,
        "palabras": palabras,
        "lineas": lineas,
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
    palabra/s más larga/s: {resultados["palabras_mas_largas"]} ({resultados["longitud_palabra_mas_larga"]} caracteres)
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


# INDICE DE JACCARD
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


# FLUJO MAIN

def main():
    textos = []

    while True:
        txt = input("ingrese texto (o 'enter' para terminar): ")
        if txt.strip() == "":
            break
        textos.append(txt)

    if not textos:
        print("No se ingreso ningun texto. fin")
        return

    while True:
        print('''
        \n        MENU
        1. ver reporte general de un texto
        2. top de palabras mas frecuentes
        3. buscar palabra en un texto (proximamente)
        4. mostrar palabras unicas
        5. comparar textos (similitud y vocabulario)
        6. ver distribucion de longitudes de palabras
        7. mostrar matriz de metricas
        8. ver promedios de metricas
        0. salir
        ''')

        while True:
            opcion = int(input('Ingrese una opcion (0-8): '))
            if 0 <= opcion <= 8:
                break

        if opcion == 1:
            # Reporte
            for i, txt in enumerate(textos):
                print(f"\nTEXTO {i+1}")
                resultados = analizar_texto(txt)
                reporte(resultados)

        elif opcion == 2:
           # TOP PALABRAS MAS FRECUENTES
           n = int(input("cuantas palabras mostrar?: "))
           
           for i, txt in enumerate(textos):
            lista_palabras = crear_lista_palabras(txt)
            frecuencia, _, _, _ = frecuencia_palabras(lista_palabras)
            top_n = ranking_palabras(frecuencia, n)

            print(f"\nTEXTO {i+1}")
            print(f"TOP {n}")
                
            for i, (palabra, veces) in enumerate(top_n):
                print(f"{i+1}) {palabra}: {veces} veces")

        elif opcion == 3:
            print('proximamente...(regex)')

        elif opcion == 4:
            # PALABRAS UNICAS
            for i, txt in enumerate(textos):
                lista_palabras = crear_lista_palabras(txt)
                _, _, _, unicas = frecuencia_palabras(lista_palabras)
                print(f"\nTEXTO {i+1}")
                print("palabras únicas:", unicas)

        elif opcion == 5:
            # COMPARAR TEXTOS
            comparar_textos(textos)

        elif opcion == 6:
            # DISTRIBUCION DE LONGITUDES
            dist = distribucion_longitudes(lista_palabras, porcentaje=True)
            for i, txt in enumerate(textos):
                lista_palabras = crear_lista_palabras(txt)
                print(f"\nTEXTO {i+1}")
                for longitud, porcentaje in dist.items():
                    print(f"- {longitud}: {porcentaje:.2f}%")

        elif opcion == 7:
            # MATRIZ 
            matriz, metricas = crear_matriz_metricas(textos)
            print("matriz de metricas:", metricas)
            for i, fila in enumerate(matriz):
                print(f"TEXTO {i+1} -> {fila}")

        elif opcion == 8:
            matriz, metricas = crear_matriz_metricas(textos)
            promedios = promedio_metricas(matriz, metricas)
            print("promedio de metricas:", promedios)

        elif opcion == 0:
            print("fin")
            break

main()

