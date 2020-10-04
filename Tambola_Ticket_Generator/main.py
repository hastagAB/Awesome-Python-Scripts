"""
Tambola Ticket generator
ask (c) 2020. All rights reserved.
"""

import argparse

import numpy as np
from tabulate import tabulate


def shuffle_array(a):
    while (~a.any(axis=1)).any():
        [np.random.shuffle(a[:, i]) for i in range(3)]
    return a


def generate_ticket():
    ticket = np.full(27, 1).reshape(9, 3)
    ticket[:4, :] *= 0
    ticket = shuffle_array(ticket)

    for i in range(9):
        num = np.arange(1, 10) if i < 8 else np.arange(1, 11)
        np.random.shuffle(num)
        num = np.sort(num[:3])
        ticket[i, :] *= (num + i * 10)
    return ticket.T


def get_tickets(args):
    tickets = []
    for _ in range(args.count):
        tickets.append(generate_ticket())
    return tickets


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', help="Generates and returns tambola tickets given by count", type=int,
                        default=1)
    args = parser.parse_args()
    return get_tickets(args)


if __name__ == "__main__":
    generated_tickets = main()
    print("Generated {0} tickets".format(len(generated_tickets)))

    for t in generated_tickets:
        print(tabulate(t, tablefmt='fancy_grid'))
