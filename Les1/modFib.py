def fib_mod(n, m):
    period = [0, 1]
    if m == 1:
        return 0
    if n == 1:
        return 1
    n0 = 0
    n1 = 1
    for __ in range(m * 6):
        n0, n1 = n1, (n0 + n1) % m
        period.append(n1 % m)
        if period[-1] == 1 and period[-2] == 0:
            break
    period = period[:-2]
    if n < len(period):
        return period[n]
    return period[n % len(period)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()