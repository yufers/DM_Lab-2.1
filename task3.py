import time
import matplotlib.pyplot as plt
import task1

if __name__ == "__main__":
    x = []
    y = []
    for i in range(1, 22):
        startTime = time.time_ns() // 1000000
        D = task1.createSubset(i)
        R = []
        task1.makeSubsets(1, i, D, R, printResult=False)
        endTime = time.time_ns() // 1000000
        duration = (endTime - startTime)
        x.append(duration / 1000)
        y.append(i)
        print(f'{i} = {len(R)} : {duration}')

    plt.figure(figsize=(8, 6))
    plt.plot(y, x, color = 'b')
    plt.xlabel('Мощность множества, N')
    plt.ylabel('время выполнения, t (сек)')
    plt.title('График зависимости времени выполнения от мощности множества')
    plt.grid(True)
    plt.legend()
    plt.show()