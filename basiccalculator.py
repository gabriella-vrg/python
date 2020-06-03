def calculadora(entrada, a, b):
    if entrada == '*':
        res = int(a * b)
        return res
    elif entrada == '/':
        res = int(a / b)
        return res
    elif entrada == '+':
        res = int(a + b)
        return res
    elif entrada == '-':
        res = int(a - b)
        return res
    else:
        print('Invalid entry! Use symbols like * / + -')


entrada = input('Type math symbol, eg. * + - /: ')
a = int(input('Type first number: '))
b = int(input('Type second number: '))
resultado = calculadora(entrada, a, b)
print(int(resultado))
