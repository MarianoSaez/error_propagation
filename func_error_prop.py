from sympy import *

# Propagacion de errores en funciones - 
# Este programa calcula el error propagado a traves de funciones en las
# cuales se introducen variables que poseen un cierto error asociado.
# La base de este programa se justifica mediante las series de Taylor.

# TODO:
# -Calculo del valor de la funcion para el vector de valores
# -Formatear output
# -Solucionar input
# -Input de constantes como pi, e, phi, etc...
# -Latex???

### INPUT ###
formula = 'x/(y**2) + z*p'
vars_vector = ['x', 'y', 'z', 'p']
values_vector = [1, 2, 3, 3.1416]
error_vector = [0.01, 0.02, 0.03, 0.00005]

# params:
# @array1: Array de valores que seran el primer elemento del par (simbolos)
# @array2: Array de valores que seran el segundo elemento del par (valor)
def to_pair_list(array1:list, array2:list):
    if len(array1) != len(array2):
        raise Exception
    result = list()
    for i in range(len(array1)):
        aux = ( symbols(array1[i]), array2[i] )
        result.append(aux)
    return result
        

# params:
# @function: Funcion a evaluar
# @variables: Vector de variables que introducen error
# @values: Vector de valores medidos de las variables
# @errors: Vector de errores con los que se realizaron las mediciones
def func_error_prop(function:str, variables:list, values:list, errors:list):
    # TODO: Validacion de args pasados a la funcion
    
    partial_derivatives = list()
    pairs = to_pair_list(variables, values) # Lista de pares ordenados
    error_bnd = 0

    # Obtenemos una lista de derivada parciales
    # para cada variable implicada en la funcion
    for i in variables:
        partial_der = diff(function, i)
        partial_derivatives.append(partial_der)
    
    # Evaluamos cada derivada para el vector de valores 
    # y lo multiplicamos por su cota de error absoluto
    for i in range(len(partial_derivatives)):
        error_bnd += abs(partial_derivatives[i].subs(pairs))*errors[i]

    return error_bnd


### OUTPUT ###
print(func_error_prop(formula, vars_vector, values_vector, error_vector))
