"""

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 """

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addNode(self, words):
        cur = self
        for c in words:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True



class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        
        ROWS = len(board)
        COLS = len(board[0])

        res = set()
        visitForWord = set ()
        trie = TrieNode()
        for word in words:       
            trie.addNode(word)


        def dfs(r,c,node,word):

            if (r<0 or c<0 or r==ROWS or c==COLS or board[r][c] not in node.children or (r,c) in visitForWord):
                return 

            visitForWord.add((r,c))
            node = node.children[board[r][c]]
            word = word + board[r][c]
            if node.isWord:
                res.add(word)
            

            dfs(r - 1,c,node,word)
            dfs(r + 1,c,node,word)
            dfs(r,c - 1,node,word)
            dfs(r,c + 1,node,word)

            visitForWord.remove((r,c))

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,trie, "")
        return(list(res))

