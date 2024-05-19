import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    y = np.linspace(0, 5, 500)
    x = 2**y

    plt.figure(figsize=(8, 6))
    plt.plot(y, x, color = 'b')
    plt.xlabel('Мощность множества, N')
    plt.ylabel('время выполнения, t (сек)')
    plt.title('График зависимости всех подмножеств от мощности множества')
    plt.grid(True)
    plt.legend()
    plt.show()