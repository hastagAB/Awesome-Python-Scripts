#!/usr/bin/python3

import string
import argparse


def encrypt(word, key_a, key_b):
    alfa_lowercase, alfa_uppercase = string.ascii_lowercase, string.ascii_uppercase

    for j in range(0, len(word)):
        for i in range(0, 26):
            if word[j] == alfa_lowercase[i] or word[j] == alfa_uppercase[i]:
                c = (key_a * i + key_b) % 26
                for x in range(0, 26):
                    if c == x:
                        if word[j] == alfa_lowercase[i]:
                            print(alfa_lowercase[x], end="")
                            break
                        else:
                            print(alfa_uppercase[x], end="")
                            break
                break
        else:
            print(" ", end="")


def decrypt(word, key_a, key_b):
    cont2, inv = 0, ''

    alfa_lowercase = string.ascii_lowercase
    alfa_uppercase = string.ascii_uppercase

    for j in range(0, len(word)):
        for i in range(0, 26):
            if word[j] == alfa_lowercase[i] or word[j] == alfa_uppercase[i]:
                for k in range(0, len(word)):
                    if cont2 == 0:
                        inv = (float((k * 26) + 1)) / key_a
                    if inv == int(inv):
                        c = inv * (i - key_b) % 26
                        cont2 = 1
                        if c < 0:
                            c += 26
                        for x in range(0, 26):
                            if c == x:
                                if word[j] == alfa_lowercase[i]:
                                    print(alfa_lowercase[x], end="")
                                    break
                                else:
                                    print(alfa_uppercase[x], end="")
                                    break
                        break
                break
        else:
            print(" ", end="")


if __name__ == "__main__":

    args = argparse.ArgumentParser(description='Main')

    group = args.add_mutually_exclusive_group(required=True)
    group.add_argument('--encrypt', nargs=3, help='Encrypt a text')
    group.add_argument('--decrypt', nargs=3, help='Decrypt a text')

    if args.parse_args().encrypt:
        text = args.parse_args().encrypt[0]
        key_a = int(args.parse_args().encrypt[1])
        key_b = int(args.parse_args().encrypt[2])
        encrypt(text, key_a, key_b)

    elif args.parse_args().decrypt:
        text = args.parse_args().decrypt[0]
        key_a = int(args.parse_args().decrypt[1])
        key_b = int(args.parse_args().decrypt[2])
        decrypt(text, key_a, key_b)
