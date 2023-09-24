from .automaton import Automaton

class OnePileAutomaton(Automaton): 

  def __init__(self, label) -> None:
    super().__init__(label)
    self.outputPile = []

  def addToOutputPile(self, item):
    self.outputPile.append(item)

  def simulate(self, input: str) -> bool:
    self.outputPile = []
    node = self.nodes[0]

    while len(node.next) > 0:
      for idx, char in enumerate(input):

        if idx == 0:
          if node.label == char:
            self.addToOutputPile(char)
            continue
          return False

        for nd in node.next:
          if nd.label == char:
            self.addToOutputPile(char)
            node = nd
            break
    output = ""
    output = output.join(self.outputPile)

    if input == output:
      return True
    return False