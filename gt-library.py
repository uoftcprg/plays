#!/usr/bin/env python3

from argparse import ArgumentParser
from json import loads
from sys import stdin, stdout

from jpype import JClass, startJVM
from jsonlines import Writer
from tqdm import trange
import numpy as np

from utilities import load_solution

DOMAIN = 'cz.agents.gtlibrary.domain.'
CONFIG = 'cz.agents.gtlibrary.nfg.simalphabeta.SimABConfig'


def parse_args():
    parser = ArgumentParser()

    parser.add_argument('count', type=int)
    parser.add_argument('name')
    parser.add_argument('--seed', type=int)

    return parser.parse_args()


def main():
    args = parse_args()
    info, state, expander, *params = args.name.split()

    startJVM()

    info = JClass(DOMAIN + info)

    for param in params:
        name, value = param.split('=')

        try:
            value = loads(value)
        except ValueError:
            pass

        setattr(info, name, value)

    info()

    state = JClass(DOMAIN + state)
    expander = JClass(DOMAIN + expander)(JClass(CONFIG)())
    n = 2
    Sigmas = [{} for _ in range(n)]
    labels = [{} for _ in range(n)]
    hs = [(state(), [0] * n)]

    while hs:
        h, sigmas = hs.pop()

        if h.isGameEnd():
            continue

        A = list(expander.getActions(h))

        if h.isPlayerToMoveNature():
            for a in A:
                hs.append((h.performAction(a), sigmas))
        else:
            i = h.getPlayerToMove().getId()
            j = sigmas[i], h.getISKeyForPlayerToMove().getHash()
            A_j = [
                Sigmas[i].setdefault((j, a.hashCode()), len(Sigmas[i]) + 1)
                for a in A
            ]

            for a, a_j in zip(A, A_j):
                sigma_primes = sigmas.copy()
                sigma_primes[i] = a_j

                labels[i].setdefault(a_j, str(a))
                hs.append((h.performAction(a), sigma_primes))

    xs = load_solution(stdin)
    rng = np.random.default_rng(args.seed)
    writer = Writer(stdout)

    for _ in trange(args.count):
        h = state()
        sigmas = [0] * n
        actions = []

        while not h.isGameEnd():
            A = list(expander.getActions(h))

            if h.isPlayerToMoveNature():
                p = np.array([h.getProbabilityOfNatureFor(a) for a in A])
                a = A[rng.choice(len(A), p=p / p.sum())]

                actions.append(str(a))
            else:
                i = h.getPlayerToMove().getId()
                j = sigmas[i], h.getISKeyForPlayerToMove().getHash()
                A_j = [Sigmas[i][j, a.hashCode()] for a in A]
                p = xs[i][A_j]
                k = rng.choice(len(A), p=p / p.sum())
                a = A[k]
                sigmas[i] = A_j[k]

                actions.append(labels[i][sigmas[i]])

            h = h.performAction(a)

        writer.write(actions)


if __name__ == '__main__':
    main()
