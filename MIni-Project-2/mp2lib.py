import numpy as np
from scipy import stats

# print(np.random.default_rng().integers(0, 2**31))

def inv_cdf_exponential(u, lam): # -> ndarray # inverse CDF, exponential
    return stats.expon.ppf(u, scale = 1 / lam)

def inv_cdf_rayleigh(u, sigma): # -> ndarray # inverse CDF, Rayleigh
    return stats.rayleigh.ppf(u, scale = sigma)

def sample_by_inversion(inv_cdf, n, rng, **kw): # -> ndarray # uniform in, samples out
    return

def ks_statistic(samples, cdf): # -> float # sup |empirical CDF - analytic CDF|
    return

def q_function(x): # -> ndarray # the Gaussian tail probability
    return