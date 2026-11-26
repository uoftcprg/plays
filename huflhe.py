#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from sys import stdin, stdout

from jsonlines import Writer
from pokerkit import (
    Automation,
    BoardDealing,
    CheckingOrCalling,
    CompletionBettingOrRaisingTo,
    Folding,
)
from tqdm import trange
import numpy as np
import pokerkit as pk

from utilities import load_A_js, load_solution

AUTOMATIONS = (
    Automation.ANTE_POSTING,
    Automation.BET_COLLECTION,
    Automation.BLIND_OR_STRADDLE_POSTING,
    Automation.RUNOUT_COUNT_SELECTION,
    Automation.HAND_KILLING,
    Automation.CHIPS_PUSHING,
    Automation.CHIPS_PULLING,
)
ACTIONS = {'f': 'fold', 'c': 'check_or_call', 'r': 'complete_bet_or_raise_to'}


def parse_args():
    parser = ArgumentParser()

    parser.add_argument('count', type=int)
    parser.add_argument('name')
    parser.add_argument('efg_path', type=Path)
    parser.add_argument('interp_path', type=Path)
    parser.add_argument('--seed', type=int)

    return parser.parse_args()


def infoset(h):
    tokens = ['{}']
    actions = []

    for op in h.operations:
        if isinstance(op, BoardDealing):
            tokens.append('{}')
        elif isinstance(op, Folding):
            actions.append('f')
        elif isinstance(op, CheckingOrCalling):
            actions.append('c')
        elif isinstance(op, CompletionBettingOrRaisingTo):
            actions.append('r')

    tokens.append(''.join(actions))

    return ':'.join(tokens)


def main():
    args = parse_args()
    game = getattr(pk, args.name)(AUTOMATIONS)
    deck = list(map(repr, game.deck))

    with open(args.efg_path) as efg, open(args.interp_path) as interp:
        A_js = load_A_js(efg, interp)

    xs = load_solution(stdin)
    rng = np.random.default_rng(args.seed)
    writer = Writer(stdout)

    for _ in trange(args.count):
        h = game()
        cards = rng.permutation(len(deck))
        deal = []
        actions = []

        while h.status and not h.can_show_or_muck_hole_cards(False):
            if (i := h.actor_index) is None:
                if h.can_burn_card():
                    h.burn_card('??')

                if h.can_deal_hole():
                    dealing = len(h.street.hole_dealing_statuses)

                    h.deal_hole('??' * dealing)
                else:
                    dealing = h.street.board_dealing_count

                    h.deal_board('??' * dealing)

                a = ''.join(deck[c] for c in sorted(cards[:dealing]))
                cards = cards[dealing:]

                deal.append(a)
            else:
                j = infoset(h).format(deal[i], *deal[2:])
                A = [a for a, f in ACTIONS.items() if getattr(h, 'can_' + f)()]
                p = xs[i][A_js[i, j]]
                a = A[rng.choice(len(A), p=p / p.sum())]

                getattr(h, ACTIONS[a])()

            actions.append(a)

        writer.write(actions)


if __name__ == '__main__':
    main()
