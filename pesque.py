def contar_texto(texto):
    cantidad_caracteres = len(texto)
    cantidad_palabras = len(texto.split())
    return cantidad_caracteres, cantidad_palabras

def promediar_longitud(texto, cantidad_palabras):
    solo_letras = 0
    for letra in texto:
        if letra.isalpha():
            solo_letras += 1
    if cantidad_palabras == 0:
        longitud_promedio = 0.0
    else:
        longitud_promedio = round(solo_letras / cantidad_palabras, 3)
    return longitud_promedio

def palabra_larga(texto):
    lista_palabras = texto.split()
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

def contar_ocurrencias(texto):
    lista_palabras = texto.split()
    cantidad_ocurrencias = 0
    termino = input("Ingrese un término que le gustaría buscar en el texto: ")
    for palabra in lista_palabras:
        if termino == palabra:
            cantidad_ocurrencias += 1 
    return termino, cantidad_ocurrencias

def frecuencia_palabras(texto):
    lista_palabras = texto.split()
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


texto = input("Ingrese un texto para analizar: ")
cantidad_caracteres, cantidad_palabras = contar_texto(texto)
longitud_promedio = promediar_longitud(texto, cantidad_palabras)
mayores = palabra_larga(texto)
termino, cantidad_ocurrencias = contar_ocurrencias(texto)
frecuencia, mas_frecuentes, maximo, unicas = frecuencia_palabras(texto)

def mostrar_datos():
    print(f"\nEl texto tiene {cantidad_caracteres} caracteres y {cantidad_palabras} palabras.\n")
    print(f"La longitud promedio de las palabras es de {longitud_promedio}.\n")

    if len(mayores) == 1:
        print(f"La palabra mas larga es: {mayores[0]}\n")
    elif len(mayores) > 1:
        print("Las palabras mas largas son:")
        for palabra in mayores:
            print(" -", palabra)
        print()

    print(f"El termino '{termino}' aparece {cantidad_ocurrencias} veces en el texto.\n")

    print("Frecuencia de palabras:")
    for p in frecuencia:
        print(f" - {p}: {frecuencia[p]}")
    print()

    if len(mas_frecuentes) == 1:
        print(f"Palabra que más aparece ({maximo} veces): {mas_frecuentes[0]}\n")
    elif len(mas_frecuentes) > 1:
        print(f"Palabras que más aparecen ({maximo} veces):")
        for p in mas_frecuentes:
            print(" -", p)

    if len(unicas) == 0:
        print("No hay palabras que salgan exactamente 1 vez.\n")
    elif len(unicas) == 1:
        print("La unica palabra que sale solo 1 vez es: " + unicas[0] + "\n")
    else:
        print("Palabras que salen unicamente 1 vez:")
        for p in unicas:
            print(" -", p)
        print()

mostrar_datos()