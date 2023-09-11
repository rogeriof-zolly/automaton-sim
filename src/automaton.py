from typing import List
from .node import Node

class Automaton:

  def __init__(self, firstNodeLabel):
    self.nodes:List[Node] = [Node(firstNodeLabel, None)]
    self.workingNode = self.nodes[0]

  def addNode(self, newNodeLabel):
    newNode = Node(newNodeLabel, self.workingNode)
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
  


