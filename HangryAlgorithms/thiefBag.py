def pack(items, max_w):
    value = 0
    w = 0
    items = sorted(items, key=lambda x: -x[0] / x[1])
    i = 0
    while i < len(items):
        if w + items[i][1] > max_w:
            value += (max_w - w) * (items[i][0] / items[i][1])
            break
        value += items[i][0]
        w += items[i][1]
        i += 1
    return value


def main():
    n, max_w = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(n)]
    value = pack(items, max_w)
    print('{0:0.3f}'.format(value))


if __name__ == "__main__":
    main()
