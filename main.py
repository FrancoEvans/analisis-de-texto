# PROGRAMA DE ANALISIS DE TEXTO


from utils.text_utils import crear_lista_palabras
from utils.metricas import frecuencia_palabras, ranking_palabras, distribucion_longitudes
from utils.analisis import (
    analizar_texto,
    reporte,
    comparar_textos,
    crear_matriz_metricas,
    promedio_metricas
)
from utils.regex import buscar_palabra


def main():
    textos = []
    while True:
        try:
            txt = input("Ingrese un texto (o presione Enter para finalizar): ")
            if len(txt) > 10000:
                raise ValueError
            if txt.strip() == "":
                break
            textos.append(txt)
        except ValueError:
            print("El texto ingresado es demasiado largo. Intente con un texto más corto.")

    if not textos:
        print("No se ingresó ningún texto. Fin del programa.")
        return

    resultados_todos = [analizar_texto(t) for t in textos]

    while True:
        print('''
==============================
        MENÚ PRINCIPAL
==============================

1. Ver Reporte General de un Texto
2. Top de Palabras Más Frecuentes
3. Buscar Palabra en un Texto (Próximamente)
4. Mostrar Palabras Únicas
5. Comparar Textos (Similitud y Vocabulario)
6. Mostrar Matriz de Métricas
7. Ver Promedios de Métricas
8. Mostrar Textos Cargados
9. Cargar Más Textos
10. Guardar Resultados en JSON
11. Guardar Textos en JSON
12. Cargar Textos desde JSON
0. Salir
==============================''')


        while True:
            try:
                opcion = int(input('Ingrese una opción (0-12): '))
                if 0 <= opcion <= 12:
                    break
                else:
                    print("Ingrese un número válido.")
            except ValueError:
                print("Ingrese un número válido.")

        if opcion == 1:
            reporte_opcion_1(resultados_todos)

        elif opcion == 2:
            top_palabras(textos)

        elif opcion == 3:
            print("Próximamente... (búsqueda con expresiones regulares)")

        elif opcion == 4:
            palabras_unicas_textos(textos)

        elif opcion == 5:
            comparar_textos(textos)

        elif opcion == 6:
            cargar_matriz_metricas(textos)

        elif opcion == 7:
            promedios(textos)
        
        elif opcion == 8:
            mostrar_textos(textos)
        
        elif opcion == 9:
            textos = cargar_mas_textos(textos)
            resultados_todos = [analizar_texto(t) for t in textos]
        
        elif opcion == 10:
            guardar_resultados_json(resultados_todos)
        
        elif opcion == 11:
            guardar_textos_json(textos)

        elif opcion == 12:
            textos = cargar_textos_json()
            resultados_todos = [analizar_texto(t) for t in textos]


        elif opcion == 0:
            print("\nPrograma finalizado.")
            break

if __name__ == "__main__":
    main()
