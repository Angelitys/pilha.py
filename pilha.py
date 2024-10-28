def menu():
    print("\nEscolha uma opção:")
    print("a) Empilhar")
    print("b) Desempilhar")
    print("c) Sair")
    return input("Opção: ").lower()

def main():
    pilha = []
    while True:
        opcao = menu()
        if opcao == 'a':
            item = input("Digite o valor para empilhar: ")
            pilha.append(item)
            print(f"{item} empilhado.")
        elif opcao == 'b':
            if pilha:
                item = pilha.pop()
                print(f"{item} desempilhado.")
            else:
                print("Pilha vazia.")
        elif opcao == 'c':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
