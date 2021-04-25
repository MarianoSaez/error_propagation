# Propagacion de error en funciones
Proyecto informatico para la materia Analisis Numerico.
3ro Ing. Informatica.
Calculo de error propagado en funciones mediante series de Taylor.

## Modo de uso
A continuacion se encuentra la salida de la ayuda por consola
```
usage: func_error_prop.py [-h] -f FILE

optional arguments:
-h, --help            show this help message and exit
-f FILE, --file FILE  Archivo de donde leer valores iniciales
```

El programa utiliza un archivo de texto a modo de entrada, se puede
modificar el archivo de ejemplo o proveer otro por argumentos
```
$ func_error_prop.py -f example.txt
```
A continuacion se deja un instructivo sobre como debe ser el formato
con los que se ingresen o cambien valores en el archivo de entrada
```
x+y+z+p
x y z p
1 2 3 3.1415
0.01 0.02 0.03 0.00005

# =============== EJEMPLO ===============
# La primer fila corresponde a la funcion.
#   En este caso:
#               f = x + y + z + p
#
# La segunda fila corresponde al vector
# de variables
#   En este caso:
#               x, y, z, p
#
# La tercera fila corresponde al vector
# de valores respectivos a cada variable
#   En este caso:
#               x = 1
#               y = 2
#               z = 3
#               p = 3.1415
#
# La cuarta fila corresponde al vector
# de errores respectivos a cada variable
#   En este caso:
#               x = 1 +\- 0.01
#               y = 2 +\- 0.02
#               z = 3 +\- 0.03
#               p = 3.1415 +\- 0.00005
```
## Referencias
* [Serie de Taylor](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiI4ZOCrJjwAhV2qJUCHZaqCr8QFjAAegQIBBAD&url=https%3A%2F%2Fes.wikipedia.org%2Fwiki%2FSerie_de_Taylor&usg=AOvVaw0ah1zq-7QBvhtILYOqP0dg)
* [Fuentes de error](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjduMWHrZjwAhW3oJUCHdzsBOMQFjAMegQIIBAD&url=https%3A%2F%2Festadistica-dma.ulpgc.es%2FFCC%2F05-1-Generalidades-Metodos-Numericos.html&usg=AOvVaw2EbXXnetcxdrraatUCh8U4)

## Bibliografia
* Métodos numéricos para ingenieros. Quinta edición. Steven C. Chapra. Raymond P. Canale

### Autor
* **Mariano Saez**