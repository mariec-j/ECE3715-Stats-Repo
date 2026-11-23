import numpy as np
from scipy import stats, special

# print(np.random.default_rng().integers(0, 2**31))

def sample_mean_cov(X) -> tuple[np.ndarray, np.ndarray]: # (mean_vector, cov_matrix): # X is (N, d)
    
    return

def is_valid_covariance(S, tol=1e-10) -> bool: # symmetric and positive semidefinite
    
    return

def gaussian_pdf(x, mu, Sigma) -> np.ndarray: # multivariate normal density, your own
    
    return

def whitening_matrix(Sigma) -> np.ndarray: # W with W Sigma W^T = I
    
    return

def lmmse_weights(Sigma_xx, Sigma_sx) -> np.ndarray: # the linear MMSE weight vector
    
    return