"""TODO:
* Support nested for loops
	* go all in on NodeTransformer?
* Create a test suite with unittest
* Semantically process FFmpeg's expression language
* Create a filter complex AST using the supplied grammar
* Create typings for every filter and sink
* Consider making sinks act like variables
"""
from .exception import ParserException
from .compile import compile
