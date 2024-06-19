from functools import reduce
from pathlib import PurePosixPath

n = int(input())
put = []
for i in range(n):
    put.append(input())

tree = {}
for path in map(PurePosixPath, put):
    reduce(lambda node, part: node.setdefault(part, {}), path.parts, tree)


def print_directory_structure(directory_structure, indent=0):
    for directory, subdirs in directory_structure.items():
        print(' ' * indent + directory)
        print_directory_structure(subdirs, indent + 2)


print_directory_structure(tree)
