# Backported from
# https://github.com/python/cpython/blob/0f42b726c87f72d522893f927b4cb592b8875641/Lib/ast.py#L1575

import ast 
import argparse

def main():
    parser = argparse.ArgumentParser(prog='python -m ast')
    parser.add_argument('infile', type=argparse.FileType(mode='rb'), nargs='?',
                        default='-',
                        help='the file to parse; defaults to stdin')
    parser.add_argument('-m', '--mode', default='exec',
                        choices=('exec', 'single', 'eval', 'func_type'),
                        help='specify what kind of code must be parsed')
    parser.add_argument('--no-type-comments', default=True, action='store_false',
                        help="don't add information about type comments")
    parser.add_argument('-a', '--include-attributes', action='store_true',
                        help='include attributes such as line numbers and '
                             'column offsets')
    args = parser.parse_args()

    with args.infile as infile:
        source = infile.read()
    tree = ast.parse(source, args.infile.name, args.mode, type_comments=args.no_type_comments)
    print(ast.dump(tree, include_attributes=args.include_attributes))

main()