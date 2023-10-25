#!/usr/bin/python

import sys
import copy
import argparse
import itertools


def parse_arguments():
    parser = argparse.ArgumentParser(description = 'Countdown - Numbers Game',
                                     add_help = False)

    parser._optionals.title = 'Target and List Numbers'

    parser.add_argument('-h', '--help', action = 'help', 
            default = argparse.SUPPRESS, 
            help = 'Countdown Numbers Game. Inform a list of six numbers (-l) and a target (-t).')

    parser.add_argument('-t', '--target', type = int, action = 'store', 
            dest = 'target', default = 100, help = 'The target of the game.')

    parser.add_argument('-l', '--list', type = int, nargs = '+', 
            default = [1, 2, 4, 8, 10, 25], help = 'List with six integers.')

    arguments = parser.parse_args()

    return arguments


pd = {}
def nubmers_game(L, t, s, ol):
    global pd
    ops = ['+', '-', '*', '/']
    ss = copy.deepcopy(s)
    key = str((ss, L))
    if key in pd:
        return pd[key]

    if len(L) == 1:
        if L[0] == t:
            print(f'Target: {t}\nNumbers: {ol}\nSolution: {ss}')
            return True
        else:
            pd[key] = False
            return False
    else:
        for c in itertools.combinations(L, 2):
            if not c[0] or not c[1]:
                continue
            tmp = L[:]
            tmp.remove(c[0])
            tmp.remove(c[1])
            exp1 = f'{c[0]} %s {c[1]}'
            exp2 = f'{c[1]} %s {c[0]}'
            if   nubmers_game(tmp + [c[0] + c[1]], t, ss + [exp1 % ('+')], ol):
                return True
            elif nubmers_game(tmp + [c[0] - c[1]], t, ss + [exp1 % ('-')], ol):
                return True
            elif nubmers_game(tmp + [c[1] - c[0]], t, ss + [exp2 % ('-')], ol):
                return True
            elif nubmers_game(tmp + [c[0] * c[1]], t, ss + [exp1 % ('*')], ol):
                return True
            elif c[0] % c[1] == 0 and nubmers_game(tmp + [c[0] // c[1]], t, ss + [exp1 % ('/')], ol):
                return True
            elif c[1] % c[0] == 0 and nubmers_game(tmp + [c[1] // c[0]], t, ss + [exp2 % ('/')], ol):
                return True
            elif nubmers_game(tmp + [c[0]], t, ss, ol):
                return True
            elif nubmers_game(tmp + [c[1]], t, ss, ol):
                return True
    pd[key] = False
    return False


if __name__ == '__main__':

    args = parse_arguments()

    if len(args.list) != 6:
        print(f'The set of numbers in Countdown is 6.')
        sys.exit(-1)

    if args.target < 0 or args.target > 999:
        print(f'The target number in Countdown is between 0 and 999.')
        sys.exit(-1)

    if not nubmers_game(args.list, args.target, [], args.list):
        print(f'Target: {args.target}')
        print(f'Numbers: {args.list}')
        print(f'Solution: Not found.')


