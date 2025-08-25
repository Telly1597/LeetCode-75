class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        dic = self.trie

        for c in word:
            if c not in dic:
                dic[c] = {}
            dic = dic[c]
        dic['.'] = '.'
        

    def search(self, word: str) -> bool:
        dic = self.trie

        for c in word:
            if c not in dic:
                return False
            dic = dic[c]
        return '.' in dic

    def startsWith(self, prefix: str) -> bool:
        dic = self.trie
        for c in prefix:
            if c not in dic:
                return False
            dic = dic[c]

        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)