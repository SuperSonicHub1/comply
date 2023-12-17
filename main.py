from parsimonious.grammar import Grammar

with open("grammar.txt") as f:
	grammar = Grammar(f.read())

with open("grammar_test.txt") as f:
	filtergraph = f.read().strip()
	tree = grammar.parse(filtergraph)

print(tree)
