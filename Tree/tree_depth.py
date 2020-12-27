def find_tree_length(parent_list: list):
    depths: dict = {}

    def rec_find(node: int) -> int:
        if node == -1:
            return 0
        elif node in depths:
            return depths[node]
        else:
            depths[node] = rec_find(parent_list[node]) + 1
            return depths[node]

    max_depth = 0
    for i in range(len(parent_list)):
        if i not in depths:
            parent_depth = rec_find(parent_list[i])
            depths[i] = parent_depth + 1
            max_depth = max(max_depth, parent_depth + 1)
    return max_depth


if __name__ == '__main__':
    input()
    print(find_tree_length(list(map(int, input().split()))))
