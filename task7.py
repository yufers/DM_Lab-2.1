import time
import matplotlib.pyplot as plt
import task6

if __name__ == "__main__":
    plt.figure(figsize=(8, 6))

    l = []
    for n in range(5, 10):
        x = []
        y = []
        l.append(f'n = {n}')
        for k in range(0, n+1):
            startTime = time.time_ns() // 1000000
            C = task6.createCombination(k)
            R = []
            if (k != 0):
                task6.makeCombination(1,1, k, n, C, R, printResult = False)

            endTime = time.time_ns() // 1000000
            duration = (endTime - startTime)
            x.append(len(R))
            y.append(k)
            print(f'n = {n}, k = {k}, = {len(R)} : {duration}')
        plt.plot(y, x)

    plt.xlabel('значение k')
    plt.ylabel('количество сочетаний')
    plt.title('графики зависимости количества всех сочетаний из n по k от k')
    plt.grid(True)
    plt.legend(l)
    plt.show()
