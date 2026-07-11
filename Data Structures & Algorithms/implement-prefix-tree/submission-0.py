class PrefixTree:

    def __init__(self):
        self.root = self.TrieNode()

    class TrieNode:
        def __init__(self, char: str = "", is_end: bool = False):
            self.char = char
            self.is_end = is_end
            self.children = {}
    def insert(self, word: str) -> None:
        ptr = self.root
        for i, char in enumerate(word):
            if char not in ptr.children:
                ptr.children[char] = self.TrieNode(char, False)
            ptr = ptr.children[char]
        ptr.is_end = True
        return
                

    def search(self, word: str) -> bool:
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                return False
            ptr = ptr.children[char]
        return True if ptr.is_end else False
        

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for char in prefix:
            if char not in ptr.children:
                return False
            ptr = ptr.children[char]
        return True
        
        
        