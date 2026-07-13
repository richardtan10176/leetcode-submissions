class WordDictionary:
    class trieNode:
        def __init__(self, is_end = False):
            self.children = {}
            self.is_end = False
    def __init__(self):
        self.root = self.trieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.trieNode()
            node = node.children[char]
        node.is_end = True
        return


    def search(self, word: str) -> bool:
            def dfs(node, curWord):
                # Base case: string exhausted, check if current node marks end of word
                if not curWord:
                    return node.is_end 
                
                char = curWord[0]
                if char == '.':
                    # Return True if ANY child path leads to success
                    for child in node.children.values():
                        if dfs(child, curWord[1:]):
                            return True
                    return False
                
                elif char in node.children:
                    # Continue traversal
                    return dfs(node.children[char], curWord[1:])
                
                return False
                
            return dfs(self.root, word)
                
        

