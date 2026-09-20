class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def diff(a, b):
            a_ptr, b_ptr = 0, 0

            diff = 0
            while a_ptr < len(a) and b_ptr < len(b):
                if a[a_ptr] != b[b_ptr]:
                    diff += 1
                a_ptr += 1
                b_ptr += 1
            
            return diff

        ## construct adj map
        adj_map = defaultdict(list)

        for i in range(len(wordList)):
            if diff(wordList[i], beginWord) == 1:
                adj_map[beginWord].append(wordList[i])
                adj_map[wordList[i]].append(beginWord)
            
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if diff(wordList[i], wordList[j]) == 1:
                    adj_map[wordList[i]].append(wordList[j])
                    adj_map[wordList[j]].append(wordList[i])
        
        queue = deque([beginWord])
        path_size = 1
        visited = set()

        while queue:
            # print(queue)
            level_size = len(queue)

            for _ in range(level_size):
                word = queue.popleft()

                if word in visited:
                    continue
                
                visited.add(word)

                if word == endWord:
                    return path_size
                
                for neighbor in adj_map[word]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            
            path_size += 1
        
        return 0