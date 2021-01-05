A = []
NEG = []
POS = []
Cont = 0
a = 0
b = 0
N = int(input("Digite um valor entre 0 e 50:"))
while N < 0 or N > 50:
    print("Entrada Inválida")
    N = int(input("Digite um valor entre 0 e 50:"))
while Cont < N:
    if N > 0 or N < 50:
        X = float(input("Insira um número real:"))
        A.append(X)
        Cont = Cont +1 
for i in A:
    if i < 0:
        NEG.append(i)
    if i > 0:
        POS.append(i)
for x in NEG:
    a = a + 1
for x in POS:
    b = b + 1
print("\nLista de Negativos",NEG, "\nQuantidade de valores contidos em NEG:", a)
print("\nLista de Positivos",POS, "\nQuantidade de valores contidos em POS:", b )
