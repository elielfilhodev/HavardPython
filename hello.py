import os
def calculadora():
    print("\n--- Menu ---")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")
    
    escolha = input("Escolha a opção (1-5): ")
    
    if escolha == '5':
        return False
        
    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            a = num1 + num2
            s = num1 - num2
            m = num1 * num2
            d = num1 / num2

            if escolha == '1':
                print(f"{num1} + {num2} = {a}")
            elif escolha == '2':
                print(f"{num1} - {num2} {s}")
            elif escolha == '3':
                print(f"{num1} * {num2} {m}")
            elif escolha == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {d}")
                else:
                    print("Erro: Divisão por zero!")
        except ValueError:
            print("Erro: Entrada inválida. Digite números.")
    else:
        print("Opção inválida.")
    return True

# Loop para manter a calculadora funcionando
while True:
    if not calculadora():
        break
