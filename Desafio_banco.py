import sys

def exibir_menu():
    print("Menu: Lista de serviços")
    print("#########################")
    print("Escolha uma opção do menu:")
    print("1. Efetuar um deposito")
    print("2. Efetuar um saque")
    print("3. Consultar extrato")
    print("4. Sair")


def efetuar_deposito():
    # Lógica para adicionar uma nova tarefa
    print("Digite o valor do depósito:")
    valor = float(input())
    if valor > 0:
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        global saldo
        saldo += valor
        # Adiciona o valor ao extrato
        global extrato
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor inválido. O depósito deve ser maior que zero.")

def efetuar_saque():
    # Lógica para remover uma tarefa
    print("Digite o valor do saque:")
    valor = float(input())
    global saldo, extrato, numero_saques, LIMITE_SAQUES
    # Verifica se o valor do saque é maior que o saldo ou o limite
    if valor > 0 and valor <= saldo:
        if valor > 500:
            print("Valor excede limite para saque.")
        else:
            saldo -= valor
                  
            
            global numero_saques, LIMITE_SAQUES
            numero_saques += 1
            if numero_saques > LIMITE_SAQUES:
                print("Número máximo de saques excedido.")
                numero_saques -= 1
                
            else:
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                 # Adiciona o valor ao extrato  
                extrato += f"Saque: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido ou excede o saldo.")

def consultar_extrato():
    # movimentações
    print("\n================ EXTRATO ================")
    if not extrato:
        print("*******Não foram realizadas movimentações.*******")
    else:
        print(extrato)

def sair():
    print("Saindo do sistema...")
    sys.exit()

def main():
    global saldo, limite, extrato, numero_saques, LIMITE_SAQUES
    saldo = float(0)
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    while True:
        exibir_menu()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            efetuar_deposito()
        elif opcao == "2":
            efetuar_saque()
        elif opcao == "3":
            consultar_extrato()
        elif opcao == "4":
            sair()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()