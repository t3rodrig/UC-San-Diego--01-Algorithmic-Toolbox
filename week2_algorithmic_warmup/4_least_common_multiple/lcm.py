# Uses python3

def gcd_euclid(a, b):
    if b == 0:
        return a

    a %= b

    return gcd_euclid(b, a)


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def lcm_efficient(a, b):
    number = int((a * b) / gcd_euclid(a, b))
    return number


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_efficient(a, b))
