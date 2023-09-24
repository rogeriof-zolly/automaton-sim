import unittest
from src.one_pile_automaton import OnePileAutomaton

class TestValidationOnePileAutomaton(unittest.TestCase):

  def test_valid_no_pile_simulation(self):
    automaton = OnePileAutomaton("a")
    automaton.addNode("b")
    automaton.addNode("c")
    #self.assertTrue(automaton.simulate("abc"))
    self.assertEqual(automaton.simulate("abc"), "abc")

  def test_invalid_no_pile_simulation(self):
    automaton = OnePileAutomaton("a")
    automaton.addNode("b")
    automaton.addNode("c")
    self.assertFalse(automaton.simulate("cbc"))

  def test_invalid_greater_no_pile_simulation(self):
    automaton = OnePileAutomaton("a")
    automaton.addNode("b")
    automaton.addNode("c")
    self.assertFalse(automaton.simulate("abcc"))

  def test_invalid_lesser_no_pile_simulation(self):
    automaton = OnePileAutomaton("a")
    automaton.addNode("b")
    automaton.addNode("c")
    self.assertFalse(automaton.simulate("ab"))