from sympy import symbols, parse_expr, diff, sympify
import argparse as ap

# Propagacion de errores en funciones - 
# Este programa calcula el error propagado a traves de funciones en las
# cuales se introducen variables que poseen un cierto error asociado.
# La base de este programa se justifica mediante las series de Taylor.

# TODO:
# -Formatear output

# Castea a float los strings de un array dado (Usa pasaje por referencia)
#   @array: Array de strings a ser casteado a array de floats
def str_to_num(array: list):
    for i in range(len(array)):
        array[i] = float(array[i])


# Devuelve una lista de tuplas con pares variable:valor que puede ser
# utilizada en reemplazos de variables por valores
#   @array1: Array de valores que seran el primer elemento del par (simbolos)
#   @array2: Array de valores que seran el segundo elemento del par (valor)
def to_pair_list(array1: list, array2: list):
    if len(array1) != len(array2):
        raise Exception
    result = list()
    for i in range(len(array1)):
        aux = ( symbols(array1[i]), array2[i] )
        result.append(aux)
    return result


# Calcula el valor de la funcion para los valores de variable ingresados
#   @function: Funcion a evaluar
#   @variables: Vector de variables que introducen error
#   @values: Vector de valores medidos de las variables
def func_value(function: str, variables: list, values: list):
    var_value_dict = dict(to_pair_list(variables, values))
    function = parse_expr(function)
    func_value = function.subs(var_value_dict)

    return func_value


# Calcula la cota de error absoluto (error bound) de una variable
# dependiente dadas sus variables independientes con sus
# respectivos valores y errores
#   @function: Funcion a evaluar
#   @variables: Vector de variables que introducen error
#   @values: Vector de valores medidos de las variables
#   @errors: Vector de errores con los que se realizaron las mediciones
def func_error_prop(function: str, variables: list, values: list, errors: list):
    # TODO: Validacion de args pasados a la funcion
    str_to_num(values)
    str_to_num(errors)
    
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



if __name__ == '__main__':
    ### INPUT ###
    str_help = 'Modo de uso de archivo [FILE] para realizar input:\n\n'
    with open('example.txt', 'r') as f:
        str_help += f.read()
    parser = ap.ArgumentParser(formatter_class=ap.RawDescriptionHelpFormatter,
                               epilog=str_help)
    parser.add_argument('-f',
                        '--file',
                        required=True,
                        help='Archivo de donde leer valores iniciales',
                        default='example.txt')
    args = parser.parse_args()
    
    with open(f'{args.file}', 'r+') as f:
        lines = f.readlines()
        f.close()
    
    formula = lines.pop(0)
    vars_vector = lines.pop(0).split()
    values_vector = lines.pop(0).split()
    error_vector = lines.pop(0).split()

    ### OUTPUT ###
    err_bnd = func_error_prop(formula, vars_vector, values_vector, error_vector)
    estim_f = func_value(formula, vars_vector, values_vector)
    print('==================== ERROR PROPAGATION ====================\n')
    print(f'f{sympify(vars_vector)} = {sympify(formula)}\n')
    for i in range(len(vars_vector)):
        print(f'\t{sympify(vars_vector[i])} = {values_vector[i]} +\\- {error_vector[i]}')
    print('')
    print(f'=> f = {estim_f} +\\- {err_bnd}\n')
