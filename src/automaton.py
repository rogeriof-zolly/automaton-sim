from typing import List
from node import Node

class Automaton:

  def __init__(self, firstNodeLabel):
    self.nodes:List[Node] = [Node(firstNodeLabel, None, None)]
    self.workingNode = self.nodes[0]

  def addNode(self, newNodeLabel):
    newNode = Node(newNodeLabel, self.workingNode, None)
    self.nodes.append(newNode)
    self.workingNode.next.append(newNode)
    self.workingNode = self.nodes[-1]

  def removeNode(self):
    if(self.workingNode.parentNodes[0] is None):
      raise(ValueError("Cannot remove the first node"))

    for index, node in enumerate(self.nodes):
      if node.id == self.workingNode.id:
        for childNode in node.next:
          childNode.parentNodes = node.parentNodes
        self.workingNode = node.parentNodes[0]
        self.workingNode.next = node.next
        self.nodes.pop(index)

  def getNodes(self):
    for node in self.nodes:
      print(node.getNode())
  
  def simulate(self, input: str) -> bool:
    node = self.nodes[0]

    if len(input) == 1:
      if node.label == input:
        return True
      return False

    while len(node.next) > 0:
      for idx, char in enumerate(input):
        valid = False
        if idx == 0:
          if node.label == char:
            valid = True
            continue
          return False

        for nd in node.next:
          if nd.label == char:
            valid = True
            node = nd
            break
        if valid == False: return False
    return True
        
        



