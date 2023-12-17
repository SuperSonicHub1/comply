import ast
from itertools import chain
from typing import Callable, Iterable

from .exception import ParserException
from .prewalk import walk_node

def replace_item(iterable: Iterable, replacement: object, test: Callable) -> Iterable:
	iterable_type = type(iterable)
	return iterable_type(chain.from_iterable(replacement if test(item) else [item] for item in iterable))

def preprocess(node: ast.Module) -> ast.Module:
	"""Preprocessing step: convert for loops to expressions."""
	assert isinstance(node, ast.Module)

	for item in node.body:
		nodes = walk_node(item)
		node.body = replace_item(node.body, nodes, lambda x: item is x)

	return node
