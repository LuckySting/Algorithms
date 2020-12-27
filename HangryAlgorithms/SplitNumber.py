def split(number):
    if number == 1:
        return [1]
    if number == 2:
        return [2]
    nums = []
    s = 0
    i = 1
    while True:
        nums.append(i)
        s += i
        i += 1
        if s + 2*i + 1 > number:
            nums.append(number - s)
            break
    return nums


def main():
    number = int(input())
    nums = split(number)
    print(len(nums))
    print(' '.join(map(str, nums)))


if __name__ == "__main__":
    main()
