class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        length = 0

        groups = {}

        # "cc" "cc" - [0, 2]

        for i, word in enumerate(words):
            if word[::-1] in groups and len(groups[word[::-1]]) > 0:
                length += 4
                groups[word[::-1]].pop()
            else:
                if word not in groups:
                    groups[word] = [i]
                else:
                    groups[word].append(i)
        
        for key in groups:
            if key == key[::-1] and groups[key]:
                length += 2
                break
        
        return length