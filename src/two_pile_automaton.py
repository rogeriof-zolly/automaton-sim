from one_pile_automaton import OnePileAutomaton

class TwoPileAutomaton(OnePileAutomaton):

  def __init__(self, firstNodeLabel, firstNodeExecutionRule):
    super().__init__(firstNodeLabel, firstNodeExecutionRule)
    self.pileTwo = []

  def handleTransaction(self, executionRule):
    pileOneActions = super().handleTransaction(executionRule)

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
  
  def validatePilesAreEmpty(self):
    return 0 == len(self.pileOne) == len(self.pileTwo)
  
  @staticmethod
  def createTransationRule(transationLabel, read1, record1, read2, record2) -> dict:
    return {
      "label": transationLabel,
      "readPileOne": read1,
      "recordPileOne": record1,
      "readPileTwo": read2,
      "recordPileTwo": record2
    }
    



      
