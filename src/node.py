from typing import List
import uuid

class Node:

  def __init__(self, label, parentNode, executionRule):
    self.id = uuid.uuid4()
    self.label = label
    self.parentNodes: List[Node] = [parentNode]
    self.next: List[Node] = []
    self.transactionRule = executionRule

  def getNode(self):
    if isinstance(self.transactionRule, dict):
      transaction = "("
      for value in self.transactionRule.values():
        transaction += value + ','
      transaction = transaction.rstrip(transaction[-1])
      transaction += ")"
    else:
      transaction = None


    return {
      "id": self.id,
      "label": self.label,
      "transactionRule": transaction
    }