# Ejercicio 1: Búsqueda no informada 
## Joel C. Flores Escalante

***jcflores@uacam.mx***

***a26216692@alumnos.uady.mx***

### Mapa de búsqueda
![Texto alternativo](./imagenes/mapa.png)

## Configurar Parejas

***--from Timisoara*** 

***--to Pitesti*** 

Ejecución de mapa y existencia de la ciudad:

python 01_romania_map.py

python 01_romania_map.py --from-city Timisoara

![Texto alternativo](./imagenes/c1.png)

## Tabla de resultados de cada uno de los algoritmos

| Algoritmo | Status | Depth (roads) | Cost (km) | Expanded (nodes) | Generated (nodes) | Frontier (max) | Path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BFS | success | 4 | 435 | 9 | 22 | 5 | Timisoara → Arad → Sibiu → Rimnicu Vilcea → Pitesti
| UCS | success | 4 | 435 | 11 | 28 | 4 |  Timisoara → Arad → Sibiu → Rimnicu Vilcea → Pitesti |
| DFS | sucess | 5 | 669 | 6 | 17 | 7 |  Timisoara → Arad → Sibiu → Fagaras → Bucharest → Pitesti |
| DLS | cutoff |  |  | 3 | 8 | 5 |  |

### Ejecución de 02_breadth_first_search.py --from-city Timisoara --to Pitesti

![Texto alternativo](./imagenes/bfs.png)

### Ejecución de 03_uniform_cost_search.py --from-city Timisoara --to Pitesti

![Texto alternativo](./imagenes/ucs.png)

### Ejecución de 04_depth_first_search.py --from-city Timisoara --to Pitesti

![Texto alternativo](./imagenes/dfs.png)

### Ejecución de 05_depth_limited_search.py --from-city Timisoara --to Pitesti --limit 2

![Texto alternativo](./imagenes/dls.png)


