"""
mp1lib.py
- Let's write some general info about the file here if need be
"""
import numpy as np
import scipy as sp
import matplotlib as mp
import jupyter as jp

# flip each bit independently w.p. p
def bsc(bits, p, rng):
    return bits ^ rng.binomial(1, p, bits.size())

# number of errors in each packet
def packet_errors(n_pkt, n_bits, p, rng):
    return rng.binomial(n_bits, p, n_pkt)

# attempts until the first clean packet,
# q = per-attempt clean probability
def attempts_until_clean(n_trials, q, rng):
    return rng.geometric(q, n_trials)

# total variation distance,
# both arrays over the same support
def tv_distance(pmf1, pmf2):

    return