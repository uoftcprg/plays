from jsonlines import Reader
from tqdm import trange
import numpy as np


def load_efg(file):
    header = file.readline().split()

    if header[:2] != ['p', 'efg']:
        raise ValueError('not UOFTCPRG EFG')

    for i in trange(int(header[2])):
        for _ in trange(int(header[3 + 2 * i]), leave=False):
            p_j, *A_j, eol = map(int, file.readline().split())

            if eol != 0:
                raise ValueError('no EOL')

            yield i, p_j, A_j


def load_A_js(efg_file, interp_file):
    A_js = {}

    for (i, _, A_j), line in zip(load_efg(efg_file), Reader(interp_file)):
        A_js[i, line['decision_point']] = A_j

    return A_js


def load_solution(file):
    xs = []

    for line in file:
        if line.startswith('s'):
            xs.append(np.array(line.split()[1:], float))

    return xs
