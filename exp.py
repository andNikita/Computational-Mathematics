def factorial(x):
    res = 1
    for i in range(1, x + 1):
        res = res * i
    return res


def _main():
    print("input number")
    x = float(input())

    res_sum = float(1)
    i = 1

    while True:
        last_sum = res_sum
        res_sum = res_sum + x**i / factorial(i)
        if last_sum == res_sum:
            break
        else:
            i = i + 1
            continue

    print(res_sum)


if __name__ == '__main__':
    _main()
