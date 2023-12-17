import ast
from .exception import ParserException
from .walk import walk_node
from .preprocess import preprocess

def compile(node: ast.Module, preprocess: bool) -> str:
	"""Convert comply's Python subset into a FFmpeg filter complex."""
	assert isinstance(node, ast.Module)

	if preprocess:
		node = preprocess(node)

	filter_source = []

	for item in node.body:
		# sws_flags
		if isinstance(item, ast.Assign):
			value = item
		# everything else
		elif isinstance(item, ast.Expr):
			value = item.value
		else:
			raise ParserException(f"Node is not types Assign, Expr: {ast.dump(item)}")

		partial_source = walk_node(value)
		filter_source.append(partial_source)

	return ";\n".join(filter_source) + "\n"
