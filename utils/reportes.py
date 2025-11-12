from .textos_json import seleccionar_textos

def reporte_opcion_1(resultados_todos):
    print("\nREPORTE GENERAL DE TEXTOS")
    print("-" * 35)

    indices = seleccionar_textos(len(resultados_todos), minimo=1)
    if not indices:
        return

    print("Cantidad de Caracteres:")
    for idx in indices:
        resultado = resultados_todos[idx]
        print(f"  Texto {idx+1}: {resultado['caracteres']}")
    print()

    print("Cantidad de Palabras:")
    for idx in indices:
        resultado = resultados_todos[idx]
        print(f"  Texto {idx+1}: {resultado['palabras']}")
    print()

    print("Cantidad de Líneas:")
    for idx in indices:
        resultado = resultados_todos[idx]
        print(f"  Texto {idx+1}: {resultado['lineas']}")
    print()

    print("Promedio de Caracteres por Palabra:")
    for idx in indices:
        resultado = resultados_todos[idx]
        print(f"  Texto {idx+1}: {resultado['promedio_letras']}")
    print()

    print("Palabra/s Más Larga/s:")
    for idx in indices:
        resultado = resultados_todos[idx]
        if resultado['longitud_palabra_mas_larga'] == 0:
            print(f"  Texto {idx+1}: No hay")
        else:
            lista = resultado['palabras_mas_largas']
            largo = resultado['longitud_palabra_mas_larga']
            sufijo = 'carácter' if largo == 1 else 'caracteres'
            print(f"  Texto {idx+1}: {lista} ({largo} {sufijo})")
    print()

    print("Palabras Más Frecuentes:")
    for idx in indices:
        resultado = resultados_todos[idx]
        if resultado['maximo'] == 0 or not resultado['mas_frecuentes']:
            print(f"  Texto {idx+1}: No hay")
        else:
            aparicion = "aparición" if resultado['maximo'] == 1 else "apariciones"
            print(f"  Texto {idx+1}: {resultado['mas_frecuentes']} ({resultado['maximo']} {aparicion})")
    print()

    print("Palabras Únicas (Cantidad):")
    for idx in indices:
        resultado = resultados_todos[idx]
        print(f"  Texto {idx+1}: {len(resultado['unicas'])}")
    print()

    print("Densidad Léxica:")
    for idx in indices:
        resultado = resultados_todos[idx]
        print(f"  Texto {idx+1}: {resultado['densidad_lexica']:.2f}")
    print()

    print("Distribución de Longitudes de Palabras (proporción):")
    for idx in indices:
        resultado = resultados_todos[idx]
        if not resultado["longitudes_frecuencia"]:
            print(f"  Texto {idx+1}: No hay palabras.")
        else:
            pares = ", ".join(f"{k}:{v:.2f}" for k, v in sorted(resultado["longitudes_frecuencia"].items()))
            print(f"  Texto {idx+1}: {pares}")
    print("-" * 35)