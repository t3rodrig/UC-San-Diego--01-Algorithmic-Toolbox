# Uses python3

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_euclid(a, b):
    if b == 0:
        return a

    a %= b

    return gcd_euclid(b, a)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_euclid(a, b))
