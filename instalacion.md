
## Instalación que funcionó

* https://www.sicara.ai/blog/2017-05-02-get-started-pyspark-jupyter-notebook-3-minutes (usar opción 1).

Encontré problemas solucionados por:

https://stackoverflow.com/a/47731444
https://stackoverflow.com/a/47731444  (ojo, aquí estoy diciendo que voy a usar java 8 en todo mi ordenador, porque spark es no compatible con Java 11. 

**OJO: Para lanzar los  notebooks, hay que escribir `pyspark`, no `jupyter notebook`**

Para comprobar que funciona, abrir el notebook [pi.ipynb](./pi.ipynb)

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
