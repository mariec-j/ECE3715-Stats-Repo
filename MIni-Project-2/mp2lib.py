import numpy as np
from scipy import stats, special

# print(np.random.default_rng().integers(0, 2**31))

def inv_cdf_exponential(u, lam) -> np.ndarray: # inverse CDF, exponential
    return stats.expon.ppf(u, scale = 1 / lam)

def inv_cdf_rayleigh(u, sigma) -> np.ndarray: # inverse CDF, Rayleigh
    return stats.rayleigh.ppf(u, scale = sigma)

def sample_by_inversion(inv_cdf, n, rng, **kw) -> np.ndarray: # uniform in, samples out
    return inv_cdf(rng.uniform(0.0, 1.0, size = n), **kw)

def ks_statistic(samples, cdf) -> float: # sup |empirical CDF - analytic CDF|
    return stats.ks_1samp(samples, cdf).statistic

def q_function(x) -> np.ndarray: # the Gaussian tail probability
    return 0.5 * special.erfc(x / 2 ** 0.5)