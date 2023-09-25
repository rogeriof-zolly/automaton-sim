from one_pile_automaton import OnePileAutomaton

class TwoPileAutomaton(OnePileAutomaton):

  def __init__(self, firstNodeLabel, firstNodeExecutionRule):
    super().__init__(firstNodeLabel, firstNodeExecutionRule)
    self.pileTwo = []

  def handleTransation(self, executionRule):
    pileOneActions = super().handleTransation(executionRule)

    if(pileOneActions == False):
      return False

    if executionRule["readPileTwo"] != "e":
      try:
        if self.pileTwo[-1] == executionRule["readPileTwo"]:
          print("leu da pilha 2:", executionRule["readPileTwo"])
          self.pileTwo.pop()
        else:
          raise ValueError("Erro de programação da pilha, valor inesperado")
      except:
        return False

    if executionRule["recordPileTwo"] != "e":
      self.pileTwo.append(executionRule["recordPileTwo"])

    print("Pilha 2:", self.pileTwo)
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
          break
        
        if found == True:
          break

      if found == False:
        return False

    if 0 == len(self.pileOne) == len(self.pileTwo):
      return True

    return False
    
  
  @staticmethod
  def createTransationRule(transationLabel, read1, record1, read2, record2) -> dict:
    return {
      "label": transationLabel,
      "readPileOne": read1,
      "recordPileOne": record1,
      "readPileTwo": read2,
      "recordPileTwo": record2
    }
    



      
