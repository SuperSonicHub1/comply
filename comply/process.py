import ast
from .const import PIPE
from .exception import ParserException

def full_process(node: ast.AST, string: bool = False):
	"""Turn an AST node into a FFmpeg-compatible value."""
	return process_value(process_node(node), string=string)

def process_node(node: ast.AST) -> str:
	"""Turn an AST node into a Python value. TODO: Add support for unary operators."""
	# Constants (e.g. strings) and variable names are interchangeable
	if isinstance(node, ast.Name):
		return node.id
	elif isinstance(node, ast.Constant):
		return node.value
	
	# Convert List nodes to normal lists
	elif isinstance(node, ast.List):
		return [process_node(elt) for elt in node.elts]
	
	# Joined strings (e.g. f"{i}")
	elif isinstance(node, ast.JoinedStr):
		return "".join([full_process(value, string=True) for value in node.values])
	elif isinstance(node, ast.FormattedValue):
		return process_node(node.value)
	else:
		raise ParserException(f"Incompatible node reached: {ast.dump(node)}")

def process_value(value: object, string: bool = False) -> str:
	"""Turn a Python value into a FFmpeg-compatible value with `repr`."""
	# Convert lists into |-separated values
	if isinstance(value, list):
		return process_value(PIPE.join([process_value(x, True) for x in value]))
	# Convert booleans to a 1 or 0
	elif isinstance(value, bool):
		value = int(value)
	# Return string representation of value else the value literal
	return str(value) if string else repr(value)
