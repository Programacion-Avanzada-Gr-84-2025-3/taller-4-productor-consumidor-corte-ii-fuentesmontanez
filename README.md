Análisis: Taller 4.
Angie Xiomara Fuentes Montañez.

Solución:
Se planteó un programa que funciona como generador de pedidos, en donde el productor
genera pedidos y el consumidor va completandolos.

Como ejecutar:
Existen dos archivos, el de taller, sin threadpool y el que contiene threadpool, al ejecutar
ambos se notan algunas diferencias en los tiempos y el rendimiento de cada uno.

Respuesta a preguntas:
Trabajo concurrente:
Divide el trabajo en dos etapas, que evitan que existan bloqueos
además el uso de hilos permite que exista sincronizacion entre los diferentes procesos
manteniendo una estabilidad.

Rendimiento:
El número de consumidores y productores debe estar regulado para que no 
existan bloqueos entre procesos actuales, además la relacion entre estos dos
debe estar ligada al tiempo de ejecucion.

Eficiencia:
El sistema es eficiente gracias al uso de hilos que optimizan
una funcion de paralelismo.