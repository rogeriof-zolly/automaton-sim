from one_pile_automaton import OnePileAutomaton
from two_pile_automaton import TwoPileAutomaton


rule_a = OnePileAutomaton.createTransationRule("a", "e", "B")
rule_b = OnePileAutomaton.createTransationRule("b", "B", "e")
automaton = OnePileAutomaton("a", rule_a)
automaton.addNode("b", rule_b)
print(automaton.simulate("aabb"))

rule_a = TwoPileAutomaton.createTransationRule("a", "e", "B", "e", "e")
rule_b = TwoPileAutomaton.createTransationRule("b", "B", "e", "e", "C")
rule_c = TwoPileAutomaton.createTransationRule("c", "e", "e", "C", "e")
automaton = TwoPileAutomaton("a", rule_a)
automaton.addNode("b", rule_b)
automaton.addNode("c", rule_c)
print(automaton.simulate("aabbcc"))