# Mini Project 2

## Functions:

### > `inv_cdf_exponential(u, lam) -> np.ndarray`
- Finds the exponential inverse cdf of an ndarray represented by u, of rate lambda ($\lambda$)
________

### > `inv_cdf_rayleigh(u, sigma) -> np.ndarray`
- Finds the rayleigh inverse cdf of an ndarray represented by u, of scale sigma ($\sigma$)
________

### > `sample_by_inversion(inv_cdf, n, rng, **kw) -> np.ndarray`
- Generates new samples by sampling by inversion
- Takes the inverse cdf and utilizes a function and a set of uniform random numbers 
- Outputs samples based on inverse cdf
________

### > `ks_statistic(samples, cdf) -> float`
- Finds the KS statistic of a sample set with a cdf
________

### > `q_function(x) -> np.ndarray`
- Returns the Gaussian tail probability
________

## What each member did:
Alejandra A.
- Step 5
- Step 6

Helena M.
- Step 7
- Step 8

Marie J.
- Step 1
- Step 4

Nathan Z.
- Functions
- Step 2
- Step 3