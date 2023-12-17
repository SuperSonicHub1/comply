from argparse import ArgumentParser, FileType
import ast
from sys import stdin, stdout
from .compile import compile

parser = ArgumentParser(prog="comply", description="A Python-to-FFmpeg-filter-complex compiler.")

parser.add_argument('-i', '--input', type=FileType('r'), default=stdin)
parser.add_argument('-o', '--output', type=FileType('w'), default=stdout)
parser.add_argument('--preprocess', action='store_true')

args = parser.parse_args()

with args.input as f:
	source = f.read()

tree = ast.parse(source)

with args.output as f:
	f.write(compile(tree, args.preprocess))
