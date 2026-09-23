class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        n = len(security)

        non_inc = [0] * n
        
        for i in range(1, len(security)):
            if security[i] <= security[i - 1]:
                non_inc[i] = non_inc[i - 1] + 1
        
        non_dec = [0] * n
        
        for i in range(len(security) - 2, -1, -1):
            if security[i] <= security[i + 1]:
                non_dec[i] = non_dec[i + 1] + 1
        
        res = []
        for i in range(time, n - time):
            if non_inc[i] >= time and non_dec[i] >= time:
                res.append(i)
        
        return res