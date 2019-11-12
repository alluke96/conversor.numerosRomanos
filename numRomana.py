# [1] No sistema de numeração romana as cifras escrevem-se com as letras I, V, X, L, C, D e M. Exemplo: 125 é representado
# por CXXV. Implemente um programa que leia um número inteiro, caso ele esteja dentro do intervalo de 1 a 999, mostre o
# número romano equivalente, caso contrário mostre “valor fornecido fora dos limites operacionais”.
# DICA: Utilize um vetor de strings para representar as unidades em números romanos, outro para as dezenas e outro para as
# centenas. Separe, usando mod e div, o valor da unidade, da dezena e da centena do número fornecido e use estes valores
# como índices de consulta aos vetores em romanos.

# 1	I
# 2	II
# 3	III
# 4	IV
# 5	V
# 6	VI
# 7	VII
# 8	VIII
# 9	IX
# 10	X
# 11	XI
# 19	XIX
# 20	XX
# 30	XXX
# 40	XL
# 50	L
# 60	LX
# 70	LXX
# 80	LXXX
# 90	XC
# 100	C
# 200	CC
# 300	CCC
# 400	CD
# 500	D
# 600	DC
# 700	DCC
# 800	DCCC
# 900	CM
# 1000	M

unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
dezenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
milhares = ["", "M", "MM", "MMM"]

num = int(input("Digite um numero: "))

uni = num % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000


if num > 0 and num <= 3999:

        print("Termo em numeracao romana: ", end='')
        print(milhares[mil], end='')
        print(centenas[cen], end='')
        print(dezenas[dez], end='')
        print(unidades[uni], end='')



else:
    print("Valor fornecido fora dos limites operacionais")
