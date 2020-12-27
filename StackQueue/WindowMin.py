# UNCOMPLETED
# 3
# 5 1 3 2 4 6 1 7 3 2 8
# 1 1 2 2 1 1 3 2 2
#             ^


def window_min(array: list, window_size: int) -> list:
    stack_min: list = []
    stack_queue_in: list = []
    stack_queue_out: list = []
    result: list = []
    minimum: int = array[0]
    for i in range(window_size - 1):
        stack_queue_in.append(array.pop(0))
    while array:
        if not stack_queue_out:
            while stack_queue_in:
                element: int = stack_queue_in.pop()
                stack_queue_out.append(element)
                if stack_min:
                    stack_min.append(stack_min[-1])
                else:
                    stack_min.append(element)
            element: int = array.pop(0)
            stack_queue_in.append(element)
            minimum = element
            result.append(min(minimum, stack_min.pop()))
            stack_queue_out.pop()
        else:
            element: int = array.pop(0)
            stack_queue_in.append(element)
            minimum = min(minimum, element)
            stack_queue_out.pop()
            result.append(min(minimum, stack_min.pop()))
    return result


if __name__ == '__main__':
    m = int(input())
    ns = list(map(int, input().split()))
    print(' '.join(map(str, window_min(ns, m))))
