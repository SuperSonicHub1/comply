import ast

from .const import COLON, PIPE, COMMA, SPACE, SWS_FLAGS
from .exception import ParserException
from .process import full_process

def walk_call(value: ast.Call) -> str:
	"""Handle functions and their arguments"""
	strings = []

	# Function names to filter names
	strings.append(value.func.id)
	
	# Positonal function arguments to positonal filter arguments 
	# Assuming all args are Constants
	args = [full_process(arg) for arg in value.args]

	# Keyword function arguments to keyword filter arguments (key=value)
	keywords = [(keyword.arg, full_process(keyword.value)) for keyword in value.keywords]

	# Only have the beginning equals if there are arguments
	if args or keywords:
		strings.append("=")
	
	# Arguments are seperated with ":"
	strings.append(COLON.join(args))

	# Need an extra colon separator
	if keywords and value.args:
		strings.append(COLON)

	strings.append(
		# Arguments are seperated with ":"
		# Assuming all args are Constants
		COLON.join([f"{arg}={value}" for arg, value in keywords])
	)

	return "".join(strings)

def walk_binop(value: ast.BinOp) -> str:
	"""Handle links and filter chains."""
	strings = []

	left = walk_node(value.left)
	op = walk_node(value.op)
	right = walk_node(value.right)

	strings.extend((left, op, right))

	return "".join(strings)

def walk_set(value: ast.Set) -> str:
	"""Handle links."""
	strings = []
	for elt in value.elts:
		name = full_process(elt, string=True)
		strings.append(f"[{name}]")
	return "".join(strings)

def walk_assign(value: ast.Assign):
	"""Should only be used for handling sws_flags."""
	assert len(value.targets) == 1
	target = value.targets[0]
	assert target.id == SWS_FLAGS
	assert isinstance(value.value, ast.Constant)
	assert isinstance(value.value.value, str)
	return f"sws_flags={full_process(value.value)}"

def walk_node(value: ast.AST) -> str:
	# Filter chains
	if isinstance(value, ast.BitOr):
		partial_source = COMMA
	# Pipe to and from links
	elif isinstance(value, ast.RShift):
		partial_source = SPACE
	# Handle the operations above
	elif isinstance(value, ast.BinOp):
		partial_source = walk_binop(value)
	# Filters
	elif isinstance(value, ast.Call):
		partial_source = walk_call(value)
	# Links
	elif isinstance(value, ast.Set):
		partial_source = walk_set(value)
	# sws_flags
	elif isinstance(value, ast.Assign):
		partial_source = walk_assign(value)
	else:
		raise ParserException(f"Incompatible node reached: {ast.dump(value)}")

	return partial_source

