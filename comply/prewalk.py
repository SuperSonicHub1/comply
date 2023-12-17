import ast
from copy import deepcopy

from .unparse import unparse
from .exception import ParserException

def walk_for(value: ast.For):
	target = value.target.id
	iterator = eval(unparse(value.iter))
	body = value.body
	nodes = []

	for i in iterator:
		class VariableToConstant(ast.NodeTransformer):
			"""Replace instances of `target` with `i`."""
			def visit_Name(self, node: ast.Name):
				if not isinstance(node.ctx, ast.Load):
					raise ParserException(f"Modifying variables ({node.id}) not allowed.")
				if node.id != target:
					return node

				new_node = ast.Constant(i)
				return ast.copy_location(new_node, node)
		
		for expr in deepcopy(body):
			VariableToConstant().visit(expr)
			nodes.append(expr)
	
	return nodes

def walk_node(value: ast.AST) -> list:
	# Filter chains
	if isinstance(value, ast.For):
		nodes = walk_for(value)
	else:
		return [value]
		# raise ParserException(f"Incompatible node reached: {ast.dump(value)}")

	return nodes

