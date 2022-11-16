# ParcialFinalOOP
En este repositorio será adjuntado el parcial final de oop

# Segundo Parcial

María Isabel Solá Valle 

# Preguntas:

## 1 . Select one exception type in Python and explain with an example its use

""" Ejemplo adjunto:
    https://ellibrodepython.com/excepciones-try-except-finally
"""
En primera instancia las excepciones nos indican cuando se produce un
error en la ejecución de nuestro codigo, un ejemplo de excepciones es
el try y except, esta excepción, captura los errores y las maneja sin
que el programa se detenga.
Ejemplo:
    "ZeroDivisionError"
        a = 5; b = 0
    try:
        c = a/b
    except ZeroDivisionError:
        print("No se ha podido realizar la división")

    -> En este ejemplo intentamos realizar una división y como 
    realmente no verificamos que b!=0 y la division por 0 no se 
    puede entonces, de inmediatamente captura el error lo que 
    evita que nuestro programa se detenga.

## 2. Select one python built-in method for classes and propose an overriding scenario
"""Referencia
    https://docs.python.org/es/3/library/functions.html#abs
"""
El built-in metodo que seleccione es el all(iterable, /), lo que se encarga de hacer es verificar el valor de verdad de los elementos,
si esto es correcto, retornara un True
    Propuesta
    def all(iterable):
    for elementos in iterable:
        if not element:
            return False
    return True

    si se valida cada elemento, entonces este es verdadero, pero si
    no se encuentra entonces retornara Falso, lo curioso del all(),
    es que puede recibir como parametro cualquier objeto que pueda ser iterable.



## 3. Why abstract base classes are useful?
La clase abstracta esta diseñada como una clase padre de la cual
pueden heredar clases hijas, es como un cascarón que da una 
estructura en donde se declara la existencia de los metodos, 
sin embargo, no se implementa funcionalidad y es util porque permite
proporcionar funcionalidad predeterminada de las clases bases y ayuda
a que codigos extensos sean mucho mas sencillos de entender 


## Explicacion de UML
primero creo una clase de parking lot con abstract method el cual le brundara a las clases hijas Car, Van, Sub, despues hereda de verificacion y por agregacion se agrega el Usuario al parking lot, ti