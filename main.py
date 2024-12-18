inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

soma_pares = 0

tem_pares = False

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pares += numero
        tem_pares = True

if tem_pares:
    print(f"A soma dos números pares no intervalo é: {soma_pares}")
else:
    print("Não há números pares no intervalo.")