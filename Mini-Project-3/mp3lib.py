import numpy as np
from scipy import stats, special

# print(np.random.default_rng().integers(0, 2**31))

def sample_mean_cov(X) -> tuple[np.ndarray, np.ndarray]: # (mean_vector, cov_matrix): # X is (N, d)
    return np.mean(X, axis=0), np.cov(X, rowvar=False)

def is_valid_covariance(S, tol=1e-10) -> bool: # symmetric and positive semidefinite
    return (
            S.ndim == 2
        and S.shape[0] == S.shape[1]
        and np.all(np.isfinite(S))
        and np.allclose(S, S.T, atol=tol)
        and np.all(np.linalg.eigvalsh(S) >= -tol)
    )

def gaussian_pdf(x, mu, Sigma) -> np.ndarray: # multivariate normal density, your own
    
    return

def whitening_matrix(Sigma) -> np.ndarray: # W with W Sigma W^T = I
    return ((eig:=np.linalg.eigh(Sigma))[1] / np.sqrt(eig[0])) @ eig[1].T

def lmmse_weights(Sigma_xx, Sigma_sx) -> np.ndarray: # the linear MMSE weight vector
    return np.linalg.solve(Sigma_xx, Sigma_sx)