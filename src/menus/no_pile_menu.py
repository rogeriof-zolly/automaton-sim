from automaton import Automaton
from helpers import clear

@staticmethod
def no_pile_menu_options():
  print("Você escolheu criar um autômato sem pilhas")
  firstNodeLabel:str = input("Defina com uma letra o label do primeiro nó: ")
  automaton = Automaton(firstNodeLabel)
  print("Autômato criado!")
  while(True):
    print("---------------------------------------------------")
    print("Você está no nó: ", automaton.workingNode.label)
    print("O que deseja fazer agora?")
    print("[1] Adicionar novo nó")
    print("[2] Remover nó atual")
    print("[3] Detalhar nó atual")
    print("[4] Simular autômato")
    print("[5] Sair do programa")
    opc = int(input("Digite o número da opção desejada: "))
    match opc:
      case 1:
        newNodeLabel = input("Digite a label do novo nó: ")
        automaton.addNode(newNodeLabel)
      case 2:
        automaton.removeNode()
      case 3:
        print(automaton.workingNode.getNode())
      case 4:
        entrada = input("Digite a string de entrada para validação: ")
        resultado = automaton.simulate(entrada)
        if resultado == True:
          print("A entrada é válida")
        else:
          print("A entrada é inválida")
      case 5:
        quit()
      case _:
        print("Opção inválida!")