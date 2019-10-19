# Big Data con Spark

## Instalación que funcionó

* https://www.sicara.ai/blog/2017-05-02-get-started-pyspark-jupyter-notebook-3-minutes (usar opción 1).

Encontré problemas solucionados por:

https://stackoverflow.com/a/47731444
https://stackoverflow.com/a/47731444  (ojo, aquí estoy diciendo que voy a usar java 8 en todo mi ordenador, porque spark es no compatible con Java 11. 

**OJO: Para lanzar los  notebooks, hay que escribir `pyspark`, no `jupyter notebook`**

## Instalación que NO me funcionó

* Tener instalado `Anaconda`.
* Instalarlo mediante `pip`

```
pip install pyspark
```

* Escribir pyspark en la consola. Debería funcionar y sacar algo similar a esto 

```
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.4.4
      /_/

Using Python version 3.7.4 (default, Aug 13 2019 15:17:50)
SparkSession available as 'spark'.
```
## Uso en notebooks

Vamos a usar el paquete `findspark`:

```
pip install findspark
```

Ahora, para usarlo debemos poner al principio del notebook (o en cualquier otro proyecto de Python), lo siguiente:

```
import findspark
findspark.init()
import pyspark
```

Ver el notebook (py.ypnb)

Fuente: https://www.analyticslane.com/2019/01/25/instalacion-de-pyspark-en-anaconda-y-primeros-pasos/


# Explicaciónn previa

## Clústers:

- Si tenemos muchos esclavos y le llega todo de golpe al master, peude tener problemas de procesameinto. Normalemten además el master no suele ser un ordenador mejor que los esclavos. 
- La distribución de trabajo es una tarea completada.
- Si un nodo peta, en un cluster tradicional, la tarea peta en general. 
- Si la red es mala, también tenemos problemas. 

Por tanto, en los kernels tradicionales se gastan un pastón en redes y buenos nodos. 

Si dos personas están trabajando en el mismo clúster, podría haber dos programas ejectuándose a la vez. Para eso hace falta un `scheduler`, que permite orquestar eso, dando por ejemplo unos cuantos nodos para la tarea del primero programa y otros cuantos. 

## Hadoop Cluster

Lo inventó Google para sus búsquedas. 

En un clúster hadoop, las cosas son un poco distintas. Cada nodo es responsable de su storage (físicamente no tiene por qué estar en ese nodo, nosotros podemos abstraernos de eso). 

![](https://user-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_9000,w_1200,f_auto,q_auto/1483830/612864_940846.png)

Además, en un Hadoop Clúster, tenemos un diagrama, un grafo, de lo que tenemos que hacer. En los tradicionales, donde no lo teníamos, si había un error, no éramos capaces de recuperarnos. Aquí sí. 

MapReduce era como se llamaba antes Hadoop. 





