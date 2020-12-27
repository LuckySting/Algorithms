def fib_digit(n):
    if n == 0:
        return 0
    fn_1 = 0
    fn = 1
    for i in range(1, n):
        fn_1, fn = fn, (fn_1 + fn) % 10
    return fn


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()