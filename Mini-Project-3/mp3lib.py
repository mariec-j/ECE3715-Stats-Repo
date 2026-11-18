import numpy as np
from scipy import stats, special

def sample_mean_cov(X) -> (mean_vector, cov_matrix): # X is (N, d)
    
    return

def is_valid_covariance(S, tol=1e-10) -> bool: # symmetric and positive semidefinite
    
    return

def gaussian_pdf(x, mu, Sigma) -> ndarray: # multivariate normal density, your own
    
    return

def whitening_matrix(Sigma) -> ndarray: # W with W Sigma W^T = I
    
    return

def lmmse_weights(Sigma_xx, Sigma_sx) -> ndarray: # the linear MMSE weight vector
    
    return