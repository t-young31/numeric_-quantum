import numpy as np
import matplotlib.pyplot as plt


def v(x_val):
    return 0.5 * mass * omega**2 * x_val**2                                  # V = (m ω^2 x^2) / 2


if __name__ == '__main__':

    n_iterations = int(1E5)
    x_min, x_max,  = -5.0, 5.0                                               # Where does the numerical sol break down
    h = (x_max - x_min) / float(n_iterations)
    x_vals, psi_vals = np.zeros(n_iterations), np.zeros(n_iterations)

    omega = 1.0                                                              # Properties of oscillator
    mass = 1.0

    n = 0
    eigenvalue = omega * (n + 0.5)                                           # In atomic units hbar = 1

    psi = 0.01                                                               # Initial values of the WF
    psi_plus1h = 0.02                                                        # What happens when these vals are altered
    x = x_min
    energy = eigenvalue

    for i in range(n_iterations):

        psi_plus2h = (-2.0 * mass * h**2 * (energy - v(x)) * psi) + 2.0 * psi_plus1h - psi
        x += h
        psi = psi_plus1h
        psi_plus1h = psi_plus2h

        x_vals[i], psi_vals[i] = x, psi                                      # Populate array to plot

    plt.plot(x_vals, psi_vals / max(psi_vals))                               # Plot x vs psi normalised to max(psi)=1
    v_vals = np.array([v(x) for x in x_vals])                                # Populate values of the potential
    plt.plot(x_vals, 5.0 * v_vals / max(v_vals) - 3.0, color='r')            # Plot the normed and shifted potential
    plt.show()
