class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        m = Counter(hand)

        for num in hand:
            start = num
            while start in m:
                start -= 1

            while start <= num:
                while m[start]:
                    for i in range(start, start + groupSize):
                        if not m[i]:
                            return False
                        m[i] -= 1
                start += 1
            
        return True