from typing import List
import uuid

class Node:

  def __init__(self, label, parentNode):
    self.id = uuid.uuid4()
    self.label = label
    self.parentNodes: List[Node] = [parentNode]
    self.next: List[Node] = []

  def getNode(self):
    return {
      "id": self.id,
      "label": self.label,
      "parentNodes": self.parentNodes,
      "next": self.next
    }