from random import randint
A = []
Cont = 0
N = int(input("Digite um valor entre 0 e 50:"))
while N < 0 or N > 50:
    print("Entrada Inválida")
    N = int(input("Digite um valor entre 0 e 50:"))
while Cont < N:
    if N > 0 or N < 50: 
        X = randint(0,1000)
        Cont = Cont +1
        A.append(X)
print(A)
