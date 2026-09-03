# Ejercicio 2
## Joel Cristoper Flores Escalante

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

**Aplicación:** Asistente virtual de voz

- **Performance:** la correcta interpretación de lo que se le pide (comandos de voz), realizar las tareas lo más rápido posible, satisfacción del cliente con la operación del agente.  
- **Environment:** El cliente o clientes, voz, acentos, tonos, sistema operativo, software y APIS. El ambiente sería parcialmente observable. Por el tema de la voz el ambiente es continuo, estocástico. 
- **Actuators:** La bocina, pantalla, software y APIS.
- **Sensors:** La tarjeta de red, teclas de volumen y encendido, microfono.

**Aplicación:** Robot aspirador doméstico

- **Performance:** La calidad de la limpieza, cubrir la totalidad o mayoría de la superficie a limpiar, el correcto mapeo del piso o área de limpieza, la habilidad para esquivar obstáculos, el regreso a su base para cargar energía. 
- **Environment:** El piso de la casa u oficina, los objetos, el ambiente. El ambiente es parcialmente observable hasta donde le permita el alcance de sus sensores. Seria continuo y estocástico. 
- **Actuators:** Las escobas/cepillos para barrer, la espiradora, los diversos motores usados para desplazarse.
- **Sensors:** Sensores de proximidad, movimiento, sensores de mapeo de area, sensores de choque, acelerómetro, cámaras.

**Aplicación:** Sistema de recomendación de streaming 

- **Performance:** Escala de calificación en base a estrellas o likes para medir la satisfacción del usuario en cuanto a la recomendación. Recomendaciones no tan conocidas pero del gusto del cliente, cantidad de clics o accesos del usuario a las recomendaciones. QUe el usuario termine completa una recomendación.   
- **Environment:**  Base de datos de las películas, catálogos, clasificaciones. El ambiente es estocastico y discreto (catalogo finito) 
- **Actuators:** El software, la interfaz gráfica del usuario (GUI), las APIS. 
- **Sensors:**  La red, los eventos del usuario (clics, reproducir, pausar, calificar, etc)  

**Aplicación:** termostato inteligente de una casa.

- **Performance:** mantener la temperatura deseada con mínimo consumo de energía y máxima comodidad del habitante.
- **Environment:** interior de una vivienda; cambia con clima exterior, ventanas abiertas y presencia de personas.
- **Actuators:** encender/apagar calefacción o aire acondicionado; ajustar temperatura objetivo; enviar alertas al usuario.
- **Sensors:** termómetro interior, horario, presencia (movimiento), lectura de clima exterior vía internet.
