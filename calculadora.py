n1 = int(input("digite o primeiro número: "))
n2 = int(input("digite o segundo número: "))
calculo = input('''
Por favor digite a operação matemática que você gostaria:
+ para adição
- para subtração
* para multiplicação
/ para divisão
                
digite: ''')

if calculo == "*":
    print("seu resultado é igual a: ",n1 * n2)
elif calculo == "+":
    print("seu resultado é igual a: ",n1 + n2)
elif calculo == "/":
    print("seu resultado é igual a: ",n1 / n2)
elif calculo == "-":
    print("seu resultado é igual a: ",n1 - n2)
else:
    print("Por favor digite a operação")