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
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.is_end

        return dfs(0, self.root)
        

