class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mappings = {2: "abc", 3: "def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        self.output = []

        def findCombination(i, combination):
            if i == len(digits):
                self.output.append("".join(combination))
                return

            for character in mappings[int(digits[i])]:
                combination.append(character)
                findCombination(i + 1, combination[::])
                combination.pop()
        
        findCombination(0, [])
        return self.output