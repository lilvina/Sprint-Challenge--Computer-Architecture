#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

file_open = sys.argv[1]

print(f'Opening File: {file_open}')

file = open(file_open, 'r')
instructions = []

for line in file:
    if line[0] != '#':
        if line != '\n':
            instructions.append(int(line[:8], 2))

cpu = CPU()

cpu.load()
cpu.run()