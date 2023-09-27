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

  def handleTransaction(self, executionRule):
    print("---------------------------------")
    if executionRule["readPileOne"] != "e":
      print(f'{executionRule["readPileOne"]}')
      try:
        if self.pileOne[-1] == executionRule["readPileOne"]:
          print(f'{executionRule["readPileOne"]}')
          print("leu da pilha 1:", executionRule["readPileOne"])
          self.pileOne.pop()
      except IndexError:
        return False

    if executionRule["recordPileOne"] != "e":
      print("gravou na pilha 1:", executionRule["recordPileOne"])
      self.pileOne.append(executionRule["recordPileOne"])

    print("Pilha 1:", self.pileOne)
    return True

  def simulate(self, input: str) -> bool:
    print("----------INICIANDO SIMULAÇÃO----------")
    currentNode = self.nodes[0]

    i=0

    while(i < len(input)):
      if input[i] == currentNode.transactionRule["label"]:
        if self.handleTransaction(currentNode.transactionRule) == False:
          return False
        i += 1
        continue

      for node in currentNode.next:
        if input[i] == node.transactionRule["label"]:
          currentNode = node
          break
    
    return self.validatePilesAreEmpty()
  
  def validatePilesAreEmpty(self):
    return 0 == len(self.pileOne)
   
  @staticmethod
  def createTransationRule(transationLabel, read1, record1) -> dict:
    return {
      "label": transationLabel,
      "readPileOne": read1,
      "recordPileOne": record1
    }