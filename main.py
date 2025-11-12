# PROGRAMA DE ANALISIS DE TEXTO

from utils.analisis import (
    analizar_texto,
    comparar_textos,
    mostrar_textos,
)
from utils.reportes import reporte_opcion_1
from utils.metricas import (
    top_palabras,
    palabras_unicas_textos,

)
from utils.matrices import (
    cargar_matriz_metricas,
    promedios
)
from utils.textos_json import (
    cargar_mas_textos,
    guardar_resultados_json,
    guardar_textos_json,
    cargar_textos_json
)
from utils.rutas import (
    elegir_varias_rutas
)
from utils.regex import buscar_regex

def main():

    textos = []
    for ruta in elegir_varias_rutas():
        with open(ruta, "r", encoding="utf-8") as f:
            texto = f.read().strip()
            textos.append(texto)
    
    resultados_todos = [analizar_texto(t) for t in textos]

    while True:
        print('''
Menu

1. ver reporte general de un texto  
2. top de palabras más frecuentes  
3. buscar palabra o patron en un texto 
4. mostrar palabras únicas  
5. comparar textos (similitud y vocabulario)  
6. mostrar matriz de métricas  
7. ver promedios de métricas  
8. mostrar textos cargados  
9. cargar más textos  
10. guardar resultados en json  
11. guardar textos en json  
12. cargar textos desde json  
0. salir
''')


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
            if not textos:
                print("No hay textos cargados.")
            else:
                resultados_todos = [analizar_texto(t) for t in textos] 
                reporte_opcion_1(resultados_todos)

        elif opcion == 2:
            top_palabras(textos)

        elif opcion == 3:
            for i, txt in enumerate(textos, start=1):
                print(f"\n--- texto {i} ---")
                buscar_regex(txt)

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
