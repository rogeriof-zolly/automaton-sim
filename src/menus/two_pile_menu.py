from helpers import clear, createOnePileTransaction, createTwoPileTransaction
from two_pile_automaton import TwoPileAutomaton


@staticmethod
def two_pile_menu_options():
  print("Você escolheu criar um autômato sem pilhas")
  firstNodeLabel:str = input("Defina com uma letra o label do primeiro nó: ")
  transactionRules = createTwoPileTransaction()
  automaton = TwoPileAutomaton(firstNodeLabel, transactionRules)
  print("Autômato criado!")
  while(True):
    clear()
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
        newNodeTransactionRules = createTwoPileTransaction()
        automaton.addNode(newNodeLabel, newNodeTransactionRules)
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
        input("Pressione Enter para continuar...")
      case 5:
        quit()
      case _:
        print("Opção inválida!")