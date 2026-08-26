class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()

        def recurse(i, combo, running_sum):
            if running_sum > target:
                return
            
            if running_sum == target:
                self.res.append(combo)
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                combo.append(candidates[j])
                running_sum += candidates[j]
                recurse(j + 1, combo[::], running_sum)
                combo.remove(candidates[j])
                running_sum -= candidates[j]
        
        recurse(0, [], 0)
        return self.res