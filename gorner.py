import matplotlib.pyplot as plt


VAL = 2
DEGR = 9


def gorner(odds, x):
    p = float(1)
    i = 1
    while i <= DEGR:
        p = p * x + odds[i] * VAL**i
        i = i + 1

    print(x, ': ', p)
    return p


def _main():
    # interval [1.92, 2.08], step = 10**(-4)
    # given (x - 2)**9

    odds = [1, -9, 36, -84, 126, -126, 84, -36, 9, -1]
    step = 10**(-4)
    print(step)
    start = 1.92
    end = 2.08

    p = []
    x = start
    while(x <= end):
        plt.scatter(x, gorner(odds, x), s=1, c='black')
        x = x + step

    plt.plot(p)
    plt.show()


if __name__ == '__main__':
    _main()
