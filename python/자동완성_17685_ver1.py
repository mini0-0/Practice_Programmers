class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def count_prefix(self, word: str):
        node = self.root
        for i, char in enumerate(word):
            node = node.children[char]
            if node.count == 1:
                return i + 1
        return len(word)


def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    answer = 0

    for word in words:
        answer += trie.count_prefix(word)

    return answer