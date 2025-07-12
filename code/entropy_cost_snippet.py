# entropy_cost_snippet.py

import numpy as np
import matplotlib.pyplot as plt

# Boltzmann constant in joules per kelvin
BOLTZMANN_CONSTANT = 1.380649e-23

def landauer_limit(temp_kelvin):
    """
    Calculates the minimum energy cost (in joules) to erase one bit of information
    based on Landauer's Principle.

    Args:
        temp_kelvin (float or np.ndarray): Temperature in Kelvin

    Returns:
        float or np.ndarray: Minimum energy cost in joules
    """
    return BOLTZMANN_CONSTANT * temp_kelvin * np.log(2)

def plot_erasure_cost():
    """
    Generates a plot showing the minimum energy cost to erase a bit
    over a range of temperatures using Landauer's Principle.
    """
    temps = np.linspace(1, 600, 500)
    costs = landauer_limit(temps)

    plt.figure(figsize=(10, 6))
    plt.plot(temps, costs, color='black', linewidth=2, label=r'$E_{\min} = kT \ln(2)$')
    plt.title('Minimum Energy Cost of Erasing One Bit (Landauer Limit)')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Energy (Joules)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("assets/entropy_erasure_plot.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    plot_erasure_cost()

