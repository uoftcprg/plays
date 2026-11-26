#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from sys import stdin, stdout

from jsonlines import Writer
from pyspiel import load_game
from tqdm import trange
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
    gamma = load_game(args.name)

    with open(args.efg_path) as efg, open(args.interp_path) as interp:
        A_js = load_A_js(efg, interp)

    xs = load_solution(stdin)
    rng = np.random.default_rng(args.seed)
    writer = Writer(stdout)

    for _ in trange(args.count):
        h = gamma.new_initial_state()
        actions = []

        while not h.is_terminal():
            if (i := h.current_player()) < 0:
                A, p = zip(*h.chance_outcomes())
                a = rng.choice(A, p=p)
            else:
                A = h.legal_actions()
                p = xs[i][A_js[i, h.information_state_string()]]
                a = A[rng.choice(len(A), p=p / p.sum())]

            actions.append(h.action_to_string(a))
            h.apply_action(a)

        writer.write(actions)


if __name__ == '__main__':
    main()
