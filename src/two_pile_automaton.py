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
      except IndexError:
        return False

    if executionRule["recordPileTwo"] != "e":
      print("gravou na pilha 2:", executionRule["recordPileTwo"])
      self.pileTwo.append(executionRule["recordPileTwo"])

    print("Pilha 2:", self.pileTwo)
    return True
  
  def validatePilesAreEmpty(self):
    return 0 == len(self.pileOne) == len(self.pileTwo)
  
  def simulate(self, input: str) -> bool:
    self.pileTwo = []
    return super().simulate(input)
  
  @staticmethod
  def createTransationRule(transationLabel, read1, record1, read2, record2) -> dict:
    return {
      "label": transationLabel,
      "readPileOne": read1,
      "recordPileOne": record1,
      "readPileTwo": read2,
      "recordPileTwo": record2
    }
    



      
