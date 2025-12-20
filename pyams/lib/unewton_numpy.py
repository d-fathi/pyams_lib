#-------------------------------------------------------------------------------
# Name:        solver_numpy_newton
# Purpose:     Nonlinear system solver (Newton–Raphson + Armijo) using NumPy
# Author:      Dhiabi Fathi
#-------------------------------------------------------------------------------

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

#-------------------------------------------------------------------------------
# norm
#-------------------------------------------------------------------------------

def norm(x):
    return np.linalg.norm(x)


#-------------------------------------------------------------------------------
# parab3p: safeguarded parabolic step
#-------------------------------------------------------------------------------
def parab3p(lambdac, lambdam, ff0, ffc, ffm):
    sigma0 = 0.1;
    sigma1 = 0.9;
    c2= lambdam*(ffc-ff0)-lambdac*(ffm-ff0);
    if c2 >= 0:
        return sigma1*lambdac;
    c1 = (lambdac*lambdac*(ffm-ff0))-(lambdam*lambdam*(ffc-ff0));
    a= -c1*0.5/c2;
    if (a < sigma0*lambdac):
        a= sigma0*lambdac;
    if(a > sigma1*lambdac):
        a= sigma1*lambdac;
    return a
#-------------------------------------------------------------------------------
# Armijo line search (NumPy)
#-------------------------------------------------------------------------------


def armijo(direction, x, f0, maxarm, f):
    """
    Armijo line search (NumPy version)

    Args:
        direction (array_like): Descent direction
        x (array_like): Current point
        f0 (array_like): f(x)
        maxarm (int): Maximum number of Armijo iterations
        f (callable): Function f(x) -> vector

    Returns:
        np.ndarray: Updated x
    """

    sigma1 = 0.8
    alpha = 1.0e-12
    iarm = 0
    armflag = 0

    lamb = 1.0
    lamm = 0.1
    lamc = lamb

    xt = x - lamb * direction
    ft = f(xt)

    nft = np.linalg.norm(ft)
    nf0 = np.linalg.norm(f0)

    ff0 = nf0**2
    ffc = nft**2
    ffm = nft**2

    maxarm = 80

    while nft >= (1 - alpha * lamb) * nf0:
        xold = xt.copy()
        fp = ft.copy()

        lamb = 0.7 * lamb
        if iarm == 0:
            lamb = sigma1 * lamb
        else:
            lamb = parab3p(lamc, lamm, ff0, ffc, ffm)

        xt = x - lamb * direction

        lamm = lamc
        lamc = lamb

        ft = f(xt)
        nft = np.linalg.norm(ft)

        ffm = ffc
        ffc = nft**2

        iarm += 1
        if iarm > maxarm:
            armflag = 1
            return xold

    return xt


#-------------------------------------------------------------------------------
# Jacobian (central finite differences)
#-------------------------------------------------------------------------------

def jacobian(x, f, delta=1e-6):
    
    n = x.size
    J = np.zeros((n, n))
    
    for i in range(n):
        xp = x.copy(); xp[i] += delta
        xm = x.copy(); xm[i] -= delta
        J[:, i] = (f(xp) - f(xm)) / (2 * delta)
    return J


def jac(x, f):
    x = np.asarray(x, dtype=float)
    n = x.size
    fx = f(x)
    J = np.zeros((n, n))

    eps = np.sqrt(np.finfo(float).eps)

    for i in range(n):
        h = eps * max(1.0, abs(x[i]))
        x[i] += h
        fp = f(x)
        x[i] -= 2*h
        fm = f(x)
        x[i] += h   # إعادة x كما كان

        J[:, i] = (fp - fm) / (2*h)

    return J
    


#-------------------------------------------------------------------------------
# Newton–Raphson solver (NumPy)
#-------------------------------------------------------------------------------

def solveNewtonNumPy(x, f,option):
    max_iter, tol = option.itl, option.error
                     
    for _ in range(max_iter):
        F = f(x)
        if norm(F) < tol:
            return x, True

        J = jac(x, f)
        dx =  np.linalg.solve(J, F)  #solveLU(J, F)
        x=armijo(dx, x, F, 40, f)
      

    return x, False



#-------------------------------------------------------------------------------
# Test
#-------------------------------------------------------------------------------
if __name__ == '__main__':
    from math import exp

    def test_f(x):
        return np.array([
            x[0] * x[2] - 7,
            x[0] * x[1] - 4,
            x[2] * x[1] - exp(x[3]),
            x[3]**2 - x[2],
            x[4]**2 - x[1]
        ])

    x0 = [2, 1, 1, 0, 0]
    sol, ok = solveNewtonNumPy(x0, test_f)
    if ok:
        print("Nonlinear solution:", sol)
    else:
        print("Failed to converge")
