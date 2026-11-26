#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from sys import stdin, stdout

from jsonlines import Writer
from tqdm import trange
import numpy as np
import pygambit as gbt

from utilities import load_A_js, load_solution


def parse_args():
    parser = ArgumentParser()

    parser.add_argument('count', type=int)
    parser.add_argument('name')
    parser.add_argument('efg_path', type=Path)
    parser.add_argument('interp_path', type=Path)
    parser.add_argument('--seed', type=int)

    return parser.parse_args()


def main():
    args = parse_args()
    gamma = gbt.catalog.load(args.name)

    with open(args.efg_path) as efg, open(args.interp_path) as interp:
        A_js = load_A_js(efg, interp)

    xs = load_solution(stdin)
    rng = np.random.default_rng(args.seed)
    writer = Writer(stdout)

    for _ in trange(args.count):
        h = gamma.root
        actions = []

        while not h.is_terminal:
            A = list(h.infoset.actions)

            if h.player.is_chance:
                p = np.array([float(a.prob) for a in A])
            else:
                i = h.player.number
                p = xs[i][A_js[i, h.infoset.number]]

            a = A[rng.choice(len(A), p=p / p.sum())]

            actions.append(a.label)
            h = h.children[a]

        writer.write(actions)


if __name__ == '__main__':
    main()
