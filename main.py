# PROGRAMA DE ANALISIS DE TEXTO


from utils.text_utils import crear_lista_palabras
from utils.metricas import frecuencia_palabras, ranking_palabras, distribucion_longitudes
from utils.reportes import (
    analizar_texto,
    reporte,
    comparar_textos,
    crear_matriz_metricas,
    promedio_metricas
)
from utils.regex import buscar_palabra


def main(textos):
    
    if not textos:
        print("No hay ningun texto. fin")
        return

    while True:
        print('''
        \n        MENU
        1. ver reporte general de un texto
        2. top de palabras mas frecuentes
        3. buscar palabra en un texto
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
            palabra = input('ingrese palabra: ')
            i = 1
            for txt in textos:
                resultados = buscar_palabra(palabra, txt)
                cantidad = len(resultados)
                if cantidad == 0:
                    print(f'en el texto {i} no aparece la palabra "{palabra}"')
                else:
                    print(f'en el texto {i} la palabra "{palabra}" aparece {cantidad} veces')
                i+=1

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

