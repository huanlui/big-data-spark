# Big Data con Spark

## Instalación

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
