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
