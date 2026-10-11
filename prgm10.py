import numpy as np
import matplotlib.pyplot as plt

def plot_curves():
    x = np.linspace(-10, 10, 400)

    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_poly = x**3 - 4*x**2 + x + 5
    y_exp = np.exp(x)

    plt.figure(figsize=(12, 8))

    # Sine curve
    plt.subplot(2, 2, 1)
    plt.plot(x, y_sin, color='blue')
    plt.title("Sine Curve")
    plt.grid(True)

    # Cosine curve
    plt.subplot(2, 2, 2)
    plt.plot(x, y_cos, color='green')
    plt.title("Cosine Curve")
    plt.grid(True)

    # Polynomial curve
    plt.subplot(2, 2, 3)
    plt.plot(x, y_poly, color='red')
    plt.title("Polynomial Curve")
    plt.grid(True)

    # Exponential curve
    plt.subplot(2, 2, 4)
    plt.plot(x, y_exp, color='purple')
    plt.title("Exponential Curve")
    plt.ylim(0, 1000)
    plt.grid(True)

    plt.tight_layout()
    plt.show()

plot_curves()
