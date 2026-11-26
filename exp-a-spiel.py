#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from sys import stdin, stdout

from jsonlines import Writer
from tqdm import trange
import eas
import numpy as np

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

    with open(args.efg_path) as efg, open(args.interp_path) as interp:
        A_js = load_A_js(efg, interp)

    xs = load_solution(stdin)
    rng = np.random.default_rng(args.seed)
    writer = Writer(stdout)

    for _ in trange(args.count):
        h = getattr(eas, args.name + 'State')()
        actions = []

        while not h.is_terminal():
            i = h.player()
            A = np.flatnonzero(h.action_mask()).tolist()
            p = xs[i][A_js[i, h.infoset_desc()]]
            a = A[rng.choice(len(A), p=p / p.sum())]

            actions.append(a)
            h.next(a)

        writer.write(actions)


if __name__ == '__main__':
    main()
