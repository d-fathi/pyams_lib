import numpy as np
from scipy.sparse.linalg import gmres, LinearOperator

def jacobian_vector_product(F, x, v, eps=1e-8):
    return (F(x + eps * v) - F(x)) / eps

def trust_region_newton_krylov(F, x0, delta0=1.0, tol=1e-8, max_iter=150):
    x = np.array(x0, dtype=float)
    delta = delta0

    for k in range(max_iter):
        Fx = F(x)
        normFx = np.linalg.norm(Fx)
        #print(f"Iter {k}: ||F(x)|| = {normFx:.2e}, Δ = {delta:.2e}")
        
        if normFx < tol:
            print("✅ Converged!")
            return x

        # Build linear operator for J(x)
        def J_mv(v):
            return jacobian_vector_product(F, x, v)
        n = len(x)
        J_op = LinearOperator((n, n), matvec=J_mv)

        # Solve J dx = -F(x) using GMRES (unpreconditioned for simplicity)
        dx_full, info = gmres(J_op, -Fx, rtol=1e-6, maxiter=min(100, n))

        # If GMRES failed, use a scaled Cauchy point (fallback)
        if info != 0:
           # print("⚠️ GMRES failed; using Cauchy point approximation.")
            # Approximate gradient g = J^T F
            g = np.zeros(n)
            for i in range(n):
                ei = np.zeros(n); ei[i] = 1.0
                Jei = jacobian_vector_product(F, x, ei)
                g[i] = np.dot(Jei, Fx)
            g_norm_sq = np.dot(g, g)
            if g_norm_sq == 0:
                dx = np.zeros(n)
            else:
                # Cauchy point: p = - (g^T F / ||J g||^2) * g, but simplified
                dx = - (np.dot(g, Fx) / (g_norm_sq + 1e-12)) * g
        else:
            dx = dx_full

        # Enforce trust-region: if ||dx|| > Δ, scale it
        dx_norm = np.linalg.norm(dx)
        if dx_norm > delta:
            dx = (delta / dx_norm) * dx

        # Evaluate trial point
        x_trial = x + dx
        Fx_trial = F(x_trial)
        actual_reduction = normFx - np.linalg.norm(Fx_trial)

        # Predicted reduction ≈ ||F(x)|| - ||F(x) + J dx|| ≈ - (F^T J dx) / ||F|| (linear approx)
        # Simpler: use ||F||^2 model
        pred_reduction = normFx - np.linalg.norm(Fx + jacobian_vector_product(F, x, dx))

        if pred_reduction <= 0:
            rho = 0.0
        else:
            rho = actual_reduction / pred_reduction

        # Update trust region
        if rho < 0.25:
            delta *= 0.25
        elif rho > 0.75:
            delta = min(2.0 * delta, 10.0)

        # Accept step if improvement
        if rho > 0.1:  # η = 0.1
            x = x_trial

        # Early stop if delta too small
        if delta < 1e-14:
            print("⚠️ Trust region too small. Stopping.")
            break

    print("⚠️ Maximum iterations reached.")
    return x







def solven(x, y,option):
    def F(v):
      return np.array(y(v.tolist()))
    solution = trust_region_newton_krylov(F, x)
    return   solution.tolist(), False