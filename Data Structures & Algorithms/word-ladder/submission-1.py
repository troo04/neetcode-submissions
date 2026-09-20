class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ## O(n)
        if endWord not in wordList:
            return 0
        
        queue = deque([beginWord])
        path_size = 1
        visited = set()

        wordSet = set(wordList)

        ## O(n)
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                word = queue.popleft()

                if word == endWord:
                    return path_size
                
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue
                        
                        new_word = word[:i] + c + word[i+1:]

                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            queue.append(new_word)
            
            path_size += 1
        
        return 0