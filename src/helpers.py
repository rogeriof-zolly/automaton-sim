import os

from one_pile_automaton import OnePileAutomaton
from two_pile_automaton import TwoPileAutomaton

def clear():
  if os.name == "nt":
    _ = os.system("cls")
  else:
    _ = os.system("clear")

def createOnePileTransaction():
  label:str = input("Digite o dado que será lido da fita: ")
  read1:str = input("Digite o dado que será lido da pilha 1 (insira 'e' para fazer nada): ")
  record1:str = input("Digite o dado que será escrito na pilha 1 (insira 'e' para fazer nada): ")

  return OnePileAutomaton.createTransationRule(label, read1, record1)

def createTwoPileTransaction():
  label:str = input("Digite o dado que será lido da fita: ")
  read1:str = input("Digite o dado que será lido da pilha 1 (insira 'e' para fazer nada): ")
  record1:str = input("Digite o dado que será escrito na pilha 1 (insira 'e' para fazer nada): ")
  read2:str = input("Digite o dado que será lido da pilha 2 (insira 'e' para fazer nada): ")
  record2:str = input("Digite o dado que será escrito na pilha 2 (insira 'e' para fazer nada): ")

  return TwoPileAutomaton.createTransationRule(label, read1, record1, read2, record2)