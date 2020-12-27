from typing import Dict


def decode_string(tree: Dict[str, str], coded_string: str) -> str:
    left: int = 0
    right: int = 1
    string: str = ''
    while right <= len(coded_string) and left <= len(coded_string):
        word: str = coded_string[left:right]
        if word in tree:
            string += tree[word]
            left = right
        right += 1
    return string


def main():
    tree_length, string_len = map(int, input().split())
    tree: Dict[str, str] = {}
    for i in range(tree_length):
        letter, code = input().replace(' ', '').split(':')
        tree.update({
            code: letter
        })
    coded_string: str = input()
    print(decode_string(tree, coded_string))


if __name__ == "__main__":
    main()
