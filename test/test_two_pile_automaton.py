import unittest
from src.two_pile_automaton import TwoPileAutomaton

class TestCreationTwoPileAutomaton(unittest.TestCase):

  def test_create_automaton(self):
    rules = TwoPileAutomaton.createTransationRule("a", "e", "e", "e", "e")
    automaton = TwoPileAutomaton("a", rules)
    self.assertEqual(len(automaton.nodes), 1)

  def test_add_node(self):
    rules = TwoPileAutomaton.createTransationRule("a", "e", "e", "e", "e")
    automaton = TwoPileAutomaton("a", rules)
    automaton.addNode("b", rules)
    self.assertEqual(len(automaton.nodes), 2)
    self.assertEqual(len(automaton.nodes[0].next), 1)
    self.assertEqual(len(automaton.nodes[1].parentNodes), 1)
    self.assertEqual(automaton.nodes[0].id, automaton.nodes[1].parentNodes[0].id)
    self.assertEqual(automaton.nodes[0].next[0].id, automaton.nodes[1].id)

  def test_add_more_than_one_node(self):
    rules = TwoPileAutomaton.createTransationRule("a", "e", "e", "e", "e")
    automaton = TwoPileAutomaton("a", rules)
    automaton.addNode("b", rules)
    automaton.addNode("c", rules)
    self.assertEqual(len(automaton.nodes), 3)
    self.assertEqual(automaton.workingNode.label, "c")

  def test_remove_node(self):
    rules = TwoPileAutomaton.createTransationRule("a", "e", "e", "e", "e")
    automaton = TwoPileAutomaton("a", rules)
    automaton.addNode("a", rules)
    automaton.addNode("b", rules)
    automaton.removeNode()
    self.assertEqual(len(automaton.nodes), 2)
    self.assertEqual(len(automaton.nodes[0].next), 1)
    self.assertEqual(len(automaton.nodes[1].parentNodes), 1)
    self.assertEqual(automaton.nodes[0].id, automaton.nodes[1].parentNodes[0].id)
    self.assertEqual(automaton.nodes[0].next[0].id, automaton.nodes[1].id)

  def test_remove_node_from_empty_automaton(self):
    rules = TwoPileAutomaton.createTransationRule("a", "e", "e", "e", "e")
    automaton = TwoPileAutomaton("a", rules)
    with self.assertRaises(ValueError):
      automaton.removeNode()

class TestSimulationMethods(unittest.TestCase):

  def test_simulate_valid_input(self):
    rules_a = TwoPileAutomaton.createTransationRule("a", "e", "B", "e", "e")
    rules_b = TwoPileAutomaton.createTransationRule("b", "B", "e", "e", "e")
    automaton = TwoPileAutomaton("a", rules_a)
    automaton.addNode("b", rules_b)
    self.assertTrue(automaton.simulate("aaabbb"))
