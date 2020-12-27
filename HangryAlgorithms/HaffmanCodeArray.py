from typing import List, Dict


def generate_queue(string: str) -> Dict[str, int]:
    queue = {}
    for s in string:
        if s not in queue:
            queue.update({
                s: 1
            })
        else:
            queue[s] += 1
    return queue


def generate_tree(queue: Dict[str, int]) -> Dict[str, str]:
    tree = {}
    if len(queue) == 1:
        return {
            list(queue.keys())[0]: '0'
        }
    while len(queue) > 1:
        letter1 = min(queue, key=queue.get)
        f_letter1 = queue[letter1]
        queue.pop(letter1)
        letter2 = min(queue, key=queue.get)
        f_letter2 = queue[letter2]
        queue.pop(letter2)
        word1 = '0'
        word2 = '1'
        for letter in tree:
            if letter in letter1:
                tree[letter] = word1 + tree[letter]
            if letter in letter2:
                tree[letter] = word2 + tree[letter]
        queue.update({
            letter1 + letter2: f_letter1 + f_letter2
        })
        tree.update({
            letter1: word1,
            letter2: word2
        })
    return tree


def main():
    string: str = input()
    queue: Dict[str, int] = generate_queue(string)
    print(len(queue), end=' ')
    tree: Dict[str, str] = generate_tree(queue)
    code = ''
    for letter in string:
        code += tree[letter]
    print(len(code))
    for letter in tree:
        if len(letter) == 1:
            print(f'{letter}: {tree[letter]}')
    print(code)


if __name__ == "__main__":
    main()
