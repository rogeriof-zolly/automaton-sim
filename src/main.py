from menus import no_pile_menu
from helpers import clear

if __name__ == "__main__":
  while(True):
    print("Bem vindo ao criador de autômatos!")
    print("O que gostaria de fazer?")
    print("[1] Criar novo autômato sem pilhas")
    print("[2] Criar novo autômato sem pilhas")
    print("[3] Criar novo autômato sem pilhas")
    print("[4] Sair do programa")
    escolha = int(input("Digite o número da sua opção: "))
    print(escolha)

    match escolha:
      case 1:
        no_pile_menu.no_pile_menu_options()
      case _:
        print("Opção inválida!")
    