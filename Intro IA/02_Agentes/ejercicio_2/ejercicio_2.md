# Ejercicio 2
## Joel Cristoper Flores Escalante
***jcflores@uacam.mx***

***a26216692@alumnos.uady.mx***


## Aplicaciones a analizar

Describe PEAS para cada una de estas aplicaciones:

1. **Asistente virtual de voz** (p. ej. Siri, Alexa o Google Assistant en un altavoz inteligente).
2. **Robot aspirador doméstico** (p. ej. Roomba u otro robot que limpia pisos de un departamento).
3. **Sistema de recomendación de streaming** (p. ej. Netflix o Spotify que sugiere películas o canciones).
4. **Vehículo autónomo en ciudad** (conducción sin conductor en calles urbanas con tráfico y peatones).
5. **Agente de trading algorítmico en bolsa** (compra y venta automática de acciones en mercados financieros).
6. **Sistema de diagnóstico médico asistido por IA** (apoya a un médico a interpretar síntomas e imágenes clínicas).
7. **Dron de inspección de infraestructura** (revisa grietas, corrosión o fugas en puentes, tuberías o líneas eléctricas).
8. **Agente jugador de ajedrez** (programa que compite contra un humano u otro agente en partidas completas).

## Respuestas

**1. Aplicación:** Asistente virtual de voz

- **Performance:** la correcta interpretación de lo que se le pide (comandos de voz), realizar las tareas lo más rápido posible, satisfacción del cliente con la operación del agente.  
- **Environment:** El cliente o clientes, voz, acentos, tonos, sistema operativo, software y APIS. El ambiente sería parcialmente observable. Por el tema de la voz el ambiente es continuo, estocástico. 
- **Actuators:** La bocina, pantalla, software y APIS.
- **Sensors:** La tarjeta de red, teclas de volumen y encendido, microfono.

**2. Aplicación:** Robot aspirador doméstico

- **Performance:** La calidad de la limpieza, cubrir la totalidad o mayoría de la superficie a limpiar, el correcto mapeo del piso o área de limpieza, la habilidad para esquivar obstáculos, el regreso a su base para cargar energía. 
- **Environment:** El piso de la casa u oficina, los objetos, el ambiente. El ambiente es parcialmente observable hasta donde le permita el alcance de sus sensores. Seria continuo y estocástico. 
- **Actuators:** Las escobas/cepillos para barrer, la espiradora, los diversos motores usados para desplazarse.
- **Sensors:** Sensores de proximidad, movimiento, sensores de mapeo de area, sensores de choque, acelerómetro, cámaras.

**3. Aplicación:** Sistema de recomendación de streaming 

- **Performance:** Escala de calificación en base a estrellas o likes para medir la satisfacción del usuario en cuanto a la recomendación. Recomendaciones no tan conocidas pero del gusto del cliente, cantidad de clics o accesos del usuario a las recomendaciones. QUe el usuario termine completa una recomendación.   
- **Environment:**  Base de datos de las películas, catálogos, clasificaciones. El ambiente es estocastico y discreto (catalogo finito) 
- **Actuators:** El software, la interfaz gráfica del usuario (GUI), las APIS. 
- **Sensors:**  La red, los eventos del usuario (clics, reproducir, pausar, calificar, etc)

**4. Aplicación:** Vehículo autónomo en ciudad 

- **Performance:** Evitar choques, baches e irregularidades del camino. Cero atropellamiento de personas, comodidad del pasajero en la conducción es decir conducción fluida no brusca. Optimización de la ruta.
- **Environment:** Las calles, avenidas, puentes, carreteras, pasos peatonales. Parcialmente observable es estocástico y continuo. 
- **Actuators:** Volante, frenos, transmición, dirección, bolsas de aire, sistema de navegación autónomo, interfaz de comuniacción con el usuario, computadora del carro,  acelerador. Luces, claxon.  
- **Sensors:**  Cámaras, sensores de proximidad, sensores de navegación.

**5. Aplicación:** Agente de trading algorítmico en bolsa.

- **Performance :** Maximizar ganancias, reducir perdidas, mostrar con velocidad las ofertas, alarmas de ofertas importantes
- **Environment:** El mercado de inversión, bolsas de valores, inversiones bancarias, inversiones propias del sistema financiero del país (ejemplo CTEs), noticias e informes financieros.  Es parcialmente observable y estocástico. 
- **Actuators:** Ejecutar compras, ventas, cancelaciones. 
- **Sensors:** Datos de las bolsas, mercados, sistema financiero. Fuentes de información, reportes, noticias para análisis de probabilidades. API bancaria para saber con cuanto capital liquido cuenta el cliente.

**6. Aplicación:** Sistema de diagnóstico médico asistido por IA

- **Performance :** Precisión diagnóstica, maximizar la cantidad de aciertos y minimizar los falsos positivos, tiempo de interpretación. 
- **Environment:** Consultorios, hospitales, doctores, enfermeras, radiólogos, laboratorios de análisis. Parcialmente observable y estocástico. 
- **Actuators:** GUI para interactuar con los médicos, imágenes generadas, informes. 
- **Sensors:** La entrada de información por voz, imagen o teclado.

**7. Aplicación:** Dron de inspección de infraestructura

- **Performance :** Precisión en la inspección es decir maximizar la tasa de aciertos al identificar fallas. Totalidad de la infraestructura inspeccionada. Esquivar obstáculos, es decir no chocar. Detección de la estructura a estudiar.
- **Environment:** Estructuras, construcciones, puentes, edificios, instalaciones eléctricas de media y alta tensión. Es parcialmente observable y estocástico. 
- **Actuators:** Sistema de vuelo, las hélices, motores, luces
- **Sensors:** cámaras, sensores de navegación, sensores del medio ambiente.

**8. Aplicación:** 

- **Performance :** Maximizar las victorias, tiempo al ganar.
- **Environment:** Observable y determinista. Tablero de ajedrez, piezas. Pueden ser físicas o virtuales
- **Actuators:** En el caso del ajedrez físico un brazo robotico. La GUI en el caso virtual- 
- **Sensors:** Para el caso fisico cámaras y sensores. Para el virtual APIS y eventos. 

