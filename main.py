# PROGRAMA DE ANALISIS DE TEXTO


# CON MANEJO DE ARCHIVOS:

# with open('texto_prueba1.txt', 'r', encoding='utf-8') as file:
#     txt = file.read()

# with open('texto_prueba2.txt', 'r', encoding='utf-8') as file:
#     txt2 = file.read()

# with open('texto_prueba3.txt', 'r', encoding='utf-8') as file:
#     txt3 = file.read()


from utils.text_utils import crear_lista_palabras
from utils.metricas import frecuencia_palabras, ranking_palabras, distribucion_longitudes
from utils.reportes import (
    analizar_texto,
    reporte,
    comparar_textos,
    crear_matriz_metricas,
    promedio_metricas
)



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

