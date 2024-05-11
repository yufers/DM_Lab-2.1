import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    y = np.linspace(0.1, 5, 500)
    x = 2**y

    plt.figure(figsize=(8, 6))
    plt.plot(y, x, label = 'x = 2^y', color = 'b')
    plt.xlabel('мощность')
    plt.ylabel('время')
    plt.title('График зависимости всех подмножеств от мощности множества')
    plt.grid(True)
    plt.legend()
    plt.show()