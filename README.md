# Big Data con Spark

Ver [Instrucciones de instalación](/instalacion.md)

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

Además, en un Hadoop Clúster, tenemos un diagrama, un grafo, de lo que tenemos que hacer. En los tradicionales, donde no lo teníamos, si había un error, no éramos capaces de recuperarnos. Aquí sí. Así, tenemos un grafo representando cada mini tarea. Si falla una, soomos capaces de saber por dónde nos quedamos, rpetirla en otro nodo y seguir con las siguientes. 

MapReduce era como se llamaba antes Hadoop. 

## Hadoop vs Spark

Hadoop funciona con storage, spark hace lo mismo que Hadoop, pero lo hace en RAM. Por tanto, Spark vuela comparado con Hadoop (hasta 100 veces).

### Nos importan los datos, y no nos gusta perderos. Necesitamos duplicidad. 
En Storage tradicional, se usaban sistemas RAID más complejos.

Lo que hace hadoop es decir: ok, si el nodo tiene 1 tb de storage, en lugar de eso, le decimos que tiene 500 gb y los otros 500 los usamos para duplicar información (de otro nodo, claro, no vas a hacerte copia de los datos en el mismo nodo). 

Esto sería para `factor de duplicidad` = 2. Para 3, tendríamos sólo un tercio de nuestro disco duro para meter nuestros datos. El resto, para duplicar datos de otros nodos. 

Todo esto orquedtado por el máster. Veremos cuando hagamos cosas con hadoop que el fichero tiene dos tamaños: 100 y 300, por ejemplo. Ocupa 100 en un nodo pero 300 en total porque el factor de duplicidad es 3. 








