import numpy as np
from scipy.sparse import coo_matrix, csc_matrix
from scipy.sparse.linalg import splu, spsolve
from math import sqrt

def norm(x):
    return sqrt(sum(v * v for v in x))

def compute_jacobian_sparse(f, x, epsilon=1e-8):
    """
    Compute sparse Jacobian using finite differences.
    Returns: (rows, cols, data) for COO format.
    """
    n = len(x)
    rows, cols, data = [], [], []
    fx = np.array(f(x))
    
    for j in range(n):  # column j
        x_pert = x.copy()
        x_pert[j] += epsilon
        f_pert = np.array(f(x_pert))
        col_deriv = (f_pert - fx) / epsilon
        
        # Store only non-zero (or significant) entries
        for i in range(n):
            if abs(col_deriv[i]) > 1e-12:  # sparsity threshold
                rows.append(i)
                cols.append(j)
                data.append(col_deriv[i])
    
    J_coo = coo_matrix((data, (rows, cols)), shape=(n, n))
    return J_coo.tocsc()  # CSC is efficient for LU

def newton_raphson_sparse(f, x0, max_iter=50, tol=1e-10, line_search=True):
    x = np.array(x0, dtype=float)
    n = len(x)
    
    for it in range(max_iter):
        F = np.array(f(x.tolist()))
        res_norm = norm(F)
        #print(f"Iter {it}: ||F|| = {res_norm:.2e}")
        
        if res_norm < tol:
            return x.tolist(), True
        
        # Build sparse Jacobian
        J = compute_jacobian_sparse(f, x.tolist())
        
        # Solve J dx = -F
        try:
            # Option 1: Direct sparse solve (simple)
            dx = spsolve(J, -F)
            
            # Option 2 (faster for multiple solves): LU factorization
            # lu = splu(J)
            # dx = lu.solve(-F)
        except Exception as e:
            print("Linear solve failed:", e)
            return x.tolist(), False
        
        # Optional: Armijo line search
        if line_search:
            alpha = 1.0
            c = 1e-4
            F_norm_sq = res_norm ** 2
            x_new = x + alpha * dx
            F_new = np.array(f(x_new.tolist()))
            while norm(F_new) > (1 - c * alpha) * res_norm:
                alpha *= 0.5
                if alpha < 1e-12:
                    break
                x_new = x + alpha * dx
                F_new = np.array(f(x_new.tolist()))
            x = x_new
        else:
            x = x + dx

    return x.tolist(), False


def solven(x, y,option):
    sol, success = newton_raphson_sparse(y, x, line_search=True)
    return   sol, False


