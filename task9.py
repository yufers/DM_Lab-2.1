import time
import matplotlib.pyplot as plt
import task8

if __name__ == "__main__":
    x = []
    y = []
    for i in range(1, 12):
        startTime = time.time_ns() // 1000000
        M = set(range(1, i + 1))
        P = task8.createPermutation(i)
        R = []
        task8.makePermutation(1, i, M, P, R, printResult = False)
        endTime = time.time_ns() // 1000000
        duration = (endTime - startTime)
        x.append(len(R))
        y.append(i)
        print(f'{i} = {len(R)} : {duration}')

    plt.figure(figsize=(8, 6))
    plt.plot(y, x, color = 'b')
    plt.xlabel('мощность')
    plt.ylabel('количество перестановок')
    plt.title('график зависимости количества всех перестановок от мощности множества')
    plt.grid(True)
    plt.legend()
    plt.show()