# 1)
# A = {1,2,3,4,5,}
# print(A)

# 2)
# lista = ["bananas", "peras", "laranjas", "abacates"]
# B = set(lista)
# print(B) 


# 3)
# lista = ["bananas", "peras", "laranjas", "limões", "bananas", "bananas", "abacates", "laranjas"]
# B = set(lista)
# print(B)

# 4)
# lista = ["bananas", "peras", "laranjas", "limões", "bananas", "bananas", "abacates", "laranjas"]
# B = set(lista)
# tamanho = len(B)
# print(f"A cardinalidade do conjunto B = {B} é {tamanho}")
# lista = {1,2}
# teste = set(lista)
# ListaB = {2,3,4,5}
# ListaC = {2,3,4}
# B = set(ListaB)
# C = set(ListaC)

# ListaA = {1,2,3}
# A = set(ListaA)
# ListaC = {1,2,3,4,5}
# C = set(ListaC)
# ListaD = {5,3,4,2,1}
# D = set(ListaD)

# if D.issubset(C) and D != C:
#     print("É Subconjunto próprio")
# else:
#     print("Não é Subconjunto Próprio")

# ListaA = {1,2,3,4,5} 
# A = set(ListaA)
# ListaB = {4,5,6,7,8,9,10}
# B = set(ListaB)
# print(B.difference(A))

# 10) Faça um menu que só encerre quando o usuário solicitar (opção de sair) que seja interativo e com as devidas validações de possíveis erros de entrada do usuário. O objetivo é fazer a operação entre 2 conjuntos, ou seja, crie uma forma de pedir dois conjuntos para o usuário (conjuntos A e B – posteriormente esses conjuntos podem ser alterados pelo usuário). As opções de operações são:
# a) União
# b) Intersecção
# c) Diferença
# d) Produto cartesiano
# e) Verificação se A é subconjunto de B (submenu: subconjunto ou subconjunto próprio)
# f) Mesma verificação do item e, mas de B com A.



def Menu_Operacao():
    print("Qual operação deseja realizar?")    
    print("1- União")
    print("2- Intersecção")
    print("3- Diferenca")
    print("4- Produto cartesiano")
    print("5- Verificação se A é subconjunto de B")
    print("6- Verificação se B é subconjunto de A")
    print("7- Voltar")


def uniao(A, B):
    print("A união dos conjuntos é: ")
    print(A.union(B))

def Interseccao(A, B):
    print("A Intersecção dos conjuntos é: ")
    print(A.intersection(B))

def Diferenca(A, B):
    print("A Diferença dos conjuntos é: ")
    print(A.difference(B))    

def Cartesiano(A, B):
    print("O Produto cartesino dos conjuntos é: ")
    from itertools import product
    print(set(product(A, B)))      
    
def SubConjunto(A, B):
    print("A união dos conjuntos é: ")
    print(A.union(B))    
       
def subconjunto(A, B):
    if(A.issubset(B) and A != B):
        print("A é subconjunto de B, e subconjunto próprio")
    elif(A.issubset(B) and A == B):
        print("A é subconjunto de B, mas não é subconjunto próprio")    
    else:
        print("Não é subconjunto")

def subconjunto2(A, B):
    if(B.issubset(A) and B != A):
        print("B é subconjunto de A, e subconjunto próprio")
    elif(B.issubset(A) and B == A):
        print("B é subconjunto de A, mas não é subconjunto próprio")
    else:
        print("Não é subconjunto.")
    

def Conjunto():
    erro = 0
    while erro == 0:
        qntA = int(input("Quantos valores terá o conjunto A?: "))
        if qntA <= erro:
            print("Entre com uma quantidade valida")
        else:
            break
    while erro == 0:
        qntB = int(input("Quantos valores terá o conjunto B?: "))
        if qntB <= erro:
            print("Entre com uma quantidade valida")
        else:
            break   

    print("Insira os valores do conjunto A")
    conjuntoA = {input().strip() for _ in range(qntA)}

    print("Insira os valores do conjunto B")
    conjuntoB = {input().strip() for _ in range(qntB)}

    return conjuntoA, conjuntoB

def Menu():
    print("1- Definir valor dos conjuntos")
    print("2- Escolher a opreção")
    print("3- Alterar Valores")
    print("4- Sair")

def Inicio():
    sair = True
    A, B = set(), set()

    while sair:
        Menu()
        opcao = int(input())
        if opcao == 1:
            A, B = Conjunto()
        elif opcao == 2:
            Menu_Operacao()
            opcao2 = int(input())
            if opcao2 == 1:
                uniao(A, B)
            elif opcao2 == 2:
                Interseccao(A, B)
            elif opcao2 == 3:
                Diferenca(A, B)
            elif opcao2 == 4:
                Cartesiano(A, B)
            elif opcao2 == 5:
                subconjunto(A, B)
            elif opcao2 == 6:
                subconjunto2(A, B)
            elif opcao2 == 7:
                break       
            else: 
                print("Opção invalida, tente novamente.")  
        elif opcao == 3:
            print("Altera os valores dos conjuntos.")
            A, B = Conjunto()
        elif opcao == 4:
            print("Até mais!")
            break
        else:           
            print("Opção Invalida, tente novamente.")

Inicio()

