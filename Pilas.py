''' Se debe solicitar al usuario una expresion matematica con parentesis, y se validara
que tenga tantos parentesis de apertura, como de cierre. Asi determinaremos si esta
balanceada la expresión'''

def validar_expresion(expresion):
    pila=[]
    for simbolo in expresion:
        if simbolo=='(':
            pila.append('(')
        elif simbolo==')':
            if len(pila)>0:
                pila.pop()
            else:
                return False
    return len(pila)==0

def main():
    print('Escriba una expresión aritmética y validaremos si esta balanceada respecto a los parentesis.')
    e=input('Expresión : ')
    valida= validar_expresion(e)
    if valida:
        print('La expresión está BALANCEADA!!!')
    else:
        print('No esta balanceada.')
    print('Hasta luego!')

if __name__=="__main__":
    main()