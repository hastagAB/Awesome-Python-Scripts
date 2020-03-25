"""Calculadora utilizando ArgumentParser."""

from argparse import ArgumentParser

from calc import soma, sub, mult, div


parser = ArgumentParser(description='Calculadora')

parser.add_argument('--sum', help='Operação de soma', action='store_true')
parser.add_argument('--sub', help='Operação de subtração', action='store_true')
parser.add_argument('--mult', help='Operação de multiplicação', action='store_true')
parser.add_argument('--div', help='Operação de divisão', action='store_true')
parser.add_argument('x', type=int, help='Primeiro valor')
parser.add_argument('y', type=int, help='Segundo valor')

args = parser.parse_args()

if args.sum:
    print(f'{soma(args.x, args.y)}')

if args.sub:
    print(f'{sub(args.x, args.y)}')

if args.mult:
    print(f'{mult(args.x, args.y)}')

if args.div:
    print(f'{div(args.x, args.y)}')
