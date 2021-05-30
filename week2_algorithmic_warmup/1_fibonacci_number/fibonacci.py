# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_fast(n):
    numbers = [0, 1]
    for i in range(2, n+1):
        num = numbers[i-1] + numbers[i-2]
        numbers.append(num)
    return numbers[n]


if __name__ == '__main__':
    n = int(input())
    print(calc_fib_fast(n))
