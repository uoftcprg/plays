#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from sys import stdin, stdout

from jsonlines import Writer
from tqdm import trange
import numpy as np

from utilities import load_A_js, load_solution


def parse_args():
    parser = ArgumentParser()

    parser.add_argument('count', type=int)
    parser.add_argument('name', type=Path)
    parser.add_argument('efg_path', type=Path)
    parser.add_argument('interp_path', type=Path)
    parser.add_argument('--seed', type=int)

    return parser.parse_args()


def main():
    args = parse_args()
    nodes = {}
    infosets = {}

    with open(args.name) as file:
        for line in file:
            match line.split():
                case ['node', h, *tokens]:
                    nodes[h] = tokens
                case ['infoset', j, 'nodes', *hs]:
                    for h in hs:
                        infosets[h] = j

    with open(args.efg_path) as efg, open(args.interp_path) as interp:
        A_js = load_A_js(efg, interp)

    xs = load_solution(stdin)
    rng = np.random.default_rng(args.seed)
    writer = Writer(stdout)

    for _ in trange(args.count):
        h = '/'
        actions = []

        while nodes[h][0] != 'leaf':
            match nodes[h]:
                case ['chance', 'actions', *A]:
                    h_prime = f'{h.rstrip("/")}/C:'
                    A, p = zip(*(a.rsplit('=', 1) for a in A))
                    p = np.array(p, float)
                case ['player', i, 'actions', *A]:
                    h_prime = f'{h.rstrip("/")}/P{i}:'
                    i = int(i) - 1
                    p = xs[i][A_js[i, infosets.get(h, h)]]

            a = A[rng.choice(len(A), p=p / p.sum())]

            actions.append(a)
            h = h_prime + a

        writer.write(actions)


if __name__ == '__main__':
    main()
