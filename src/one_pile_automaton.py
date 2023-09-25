from typing import List

from node import Node
from automaton import Automaton

class OnePileAutomaton(Automaton): 

  def __init__(self, label, firstNodeExecutionRule) -> None:
    self.nodes:List[Node] = [Node(label, None, firstNodeExecutionRule)]
    self.workingNode = self.nodes[0]
    self.pileOne = []

  def addNode(self, newNodeLabel, newNodeExecutionRule):
    newNode = Node(newNodeLabel, self.workingNode, newNodeExecutionRule)
    self.nodes.append(newNode)
    self.workingNode.next.append(newNode)
    self.workingNode = self.nodes[-1]

  def handleTransation(self, executionRule):
    print("---------------------------------")
    if executionRule["readPileOne"] != "e":
      try:
        if self.pileOne[-1] == executionRule["readPileOne"]:
          print("leu da pilha 1:", executionRule["readPileOne"])
          self.pileOne.pop()
        else:
          raise ValueError("Erro de programação da pilha, valor inesperado")
      except:
        return False

    if executionRule["recordPileOne"] != "e":
      print("gravou na pilha 1:", executionRule["recordPileOne"])
      self.pileOne.append(executionRule["recordPileOne"])

    print("Pilha 1:", self.pileOne)
    return True

  def simulate(self, input: str) -> bool:
    print("----------INICIANDO SIMULAÇÃO----------")
    currentNode = self.nodes[0]

    for char in input:
      found = False
      
      if char == currentNode.transationRule["label"]:
        found = True
        if(self.handleTransation(currentNode.transationRule) == False):
          return False
        continue
      
      while len(currentNode.next) > 0:
        for node in currentNode.next:
          if node.transationRule["label"] != char:
            continue
          
          found = True
          if(self.handleTransation(node.transationRule) == False):
            return False
          currentNode = node

      if found == False:
        return False

    if 0 == len(self.pileOne):
      return True

    return False
  
  @staticmethod
  def createTransationRule(transationLabel, read1, record1) -> dict:
    return {
      "label": transationLabel,
      "readPileOne": read1,
      "recordPileOne": record1
    }