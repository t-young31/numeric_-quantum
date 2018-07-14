import numpy as np
import matplotlib.pyplot as plt


def v(x_val):
    infinity = 1E10

    if x_val < l_min or x_val > l_max:
        return infinity                                                 # If the particle is outside the box V=infinity
    else:
        return 0                                                        # If it's in the box V=0


if __name__ == '__main__':

    n_iterations = int(1E4)                                             # Number of iterations to use. Accuracy vs speed
    l_min, l_max, length = -1.0, 3.0, 4.0                               # Size of the well
    h = (l_max - l_min)/float(n_iterations)                             # Step size for the finite difference approx
    x_vals, psi_vals = np.zeros(n_iterations), np.zeros(n_iterations)   # Initialise lists so values can be plotted

    n = 10.0
    eigenvalue = (np.pi**2 / (2.0 * length**2)) * n**2                  # Analytic eigenvalues, with mass = 1

    psi = 0.01                                                          # Finite difference requires two initial values
    psi_plus1h = 0.02                                                   # What changes if psi_plus1h < psi?
    x = l_min
    energy = eigenvalue                                                 # Set as an eigenvalue. What changes if its not?

    for i in range(n_iterations):                                       # Propagate psi using the finite difference

        psi_plus2h = (-2.0 * h**2 * (energy - v(x)) * psi) + 2.0 * psi_plus1h - psi
        x += h                                                          # Equivalent to x = x + h
        psi = psi_plus1h
        psi_plus1h = psi_plus2h

        x_vals[i] = x                                                   # Populate the lists with values of x
        psi_vals[i] = psi                                               # and psi, at that x

    plt.plot(x_vals[1:-1], psi_vals[1:-1])                              # Plot the results using matplotlib
    max_psi = max(psi_vals[1:-1])
    plt.plot([l_min, l_min, l_max, l_max],
             [max_psi*2.0, 0, 0, max_psi*2], color='r')                 # Plot the potential in red
    plt.show()
