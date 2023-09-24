import unittest
from src.automaton import Automaton

class TestAutomatonMethods(unittest.TestCase):

  def test_create_automaton(self):
    automaton = Automaton("a")
    self.assertEqual(len(automaton.nodes), 1)

  def test_add_node(self):
    automaton = Automaton("a")
    automaton.addNode("b")
    self.assertEqual(len(automaton.nodes), 2)
    self.assertEqual(len(automaton.nodes[0].next), 1)
    self.assertEqual(len(automaton.nodes[1].parentNodes), 1)
    self.assertEqual(automaton.nodes[0].id, automaton.nodes[1].parentNodes[0].id)
    self.assertEqual(automaton.nodes[0].next[0].id, automaton.nodes[1].id)

  def test_add_more_than_one_node(self):
    automaton = Automaton("a")
    automaton.addNode("b")
    automaton.addNode("c")
    self.assertEqual(len(automaton.nodes), 3)
    self.assertEqual(automaton.workingNode.label, "c")

  def test_remove_node(self):
    automaton = Automaton("a")
    automaton.addNode("a")
    automaton.addNode("b")
    automaton.removeNode()
    self.assertEqual(len(automaton.nodes), 2)
    self.assertEqual(len(automaton.nodes[0].next), 1)
    self.assertEqual(len(automaton.nodes[1].parentNodes), 1)
    self.assertEqual(automaton.nodes[0].id, automaton.nodes[1].parentNodes[0].id)
    self.assertEqual(automaton.nodes[0].next[0].id, automaton.nodes[1].id)

  def test_remove_node_from_empty_automaton(self):
    automaton = Automaton("a")
    with self.assertRaises(ValueError):
      automaton.removeNode()

class TestSimulationMethods(unittest.TestCase):
  
  def test_valid_no_pile_simulation(self):
    automaton = Automaton("a")
    automaton.addNode("b")
    automaton.addNode("c")
    self.assertTrue(automaton.simulate("abc"))

  def test_invalid_no_pile_simulation(self):
    automaton = Automaton("a")
    automaton.addNode("b")
    automaton.addNode("c")
    self.assertFalse(automaton.simulate("cbc"))

  def test_invalid_greater_no_pile_simulation(self):
    automaton = Automaton("a")
    automaton.addNode("b")
    automaton.addNode("c")
    self.assertFalse(automaton.simulate("abcc"))

  def test_invalid_lesser_no_pile_simulation(self):
    automaton = Automaton("a")
    automaton.addNode("b")
    automaton.addNode("c")
    self.assertFalse(automaton.simulate("ab"))
    

