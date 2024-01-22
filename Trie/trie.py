# demonstration of a Trie or also known as prefix tree
# Trie is a tree-like data structure that is used to store a collection of strings.
# Tries are used for efficient retrieval of a key in a dataset of strings.
# Problem:
# Implement Trie Insertion method - Inserts the string word into the trie.
# Implement Search method - Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# Implement Trie StartsWith method - eturns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
# Example:
# Input :
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output :
# [null, null, true, false, true, null, true]


class Node:
    def __init__(self):
        self.children = {}
        self.is_endOfWord = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        # initialize Trie instance
        current = self.root
        for char in word:
            if char not in current.children:
                # initialize a new Node() data structure to the new char
                current.children[char] = Node()
            # move to the next char inside the instance children dictionary
            current = current.children[char]
        current.is_endOfWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.startsWith("bot"))
    print(trie.startsWith("apple"))
