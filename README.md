# Words Counter

Este software cuenta las palabras de uno o varios archivos de entrada, y permite escribir el resultado en diferentes formatos (csv, json o yaml).

Este software se ha desarrollado sobre Python 3.6.


# ¿Cómo funciona?

Existe una entidad llamada __loader__ que dado el nombre de un archivo devuelve de manera _lazy_ las palabras (o tokens) que contiene ese archivo.

Este flujo de palabras es inyectado en una función (simple_counter) que se encarga de filtrar y quitar elementos no deseados a todas las palabras.
Además, las añade a una estructura de datos (hashmap) para poder ir contando la cantidad de veces que ha aparecido esa palabra. Esta función devuelve un objeto
de tipo Count, que es un diccionario pero con algunos métodos que nos ayudan. 

Se ha elegido un diccionario (hashmap) como estructura de datos principal para llevar el conteo de palabras ya que el coste computacional de acceso a
un elemento es O(1). Este diccionario viene enmascarado dentro de un objeto propio llamado Count. Esto nos ayuda a abstraer la estructura de datos del proceso
de adaptar la salida del contador a un archivo.

Este objecto resultante es utilizado por los __adapters__ para formar el archivo resultante.


# ¿Cómo utilizarlo?

Se hace uso de **Docker** y **docker-compose** para la ejecución del software así como de la ejecución de los tests. Además, se hace uso de un **Makefile** para simplicar la ejecución.

En la primera ejecución del software deberemos realizar un *build* de la imagen Docker. Para ello, haremos servir el comando:

```sh
$ make build
```

y seguidamente ejecutamos el comando:

```sh
$ make run args="-f othello.txt kinglear.txt romeoandjuliet.txt"
```

Para ver todas las opciones permitidas, se puede utilizar:

```sh
$ make run args="--help"
```


# Tests

Existen los test mínimos para comprobar que la funcionalidad __core__ del problema (contar palabras).

Para ejecutarlos primero deberemos construir la imagen de Docker destinada a los tests:

```sh
$ make build-test
```

Y a continuación, podríamos ejecutar los test:

```sh
$ make test
```
