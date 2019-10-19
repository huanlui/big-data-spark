# Big Data con Spark

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





