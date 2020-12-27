def cover(dashes):
    dots = []
    dashes = sorted(dashes, key=lambda d: d[1])
    i = 0
    while i < len(dashes):
        dots.append(dashes[i][1])
        i += 1
        while i < len(dashes) and dots[-1] >= dashes[i][0]:
            i += 1
    return dots


def main():
    n = int(input())
    dashes = [list(map(int, input().split())) for _ in range(n)]
    dots = cover(dashes)
    print(len(dots))
    print(' '.join(map(str, dots)))


if __name__ == "__main__":
    main()
