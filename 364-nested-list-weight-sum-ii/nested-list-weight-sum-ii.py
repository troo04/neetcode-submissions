# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: list[NestedInteger]) -> int:
        self.maxDepth = 0

        def dfs(lst, depth):
            self.maxDepth = max(self.maxDepth, depth)
            
            if not lst.isInteger():
                for ele in lst.getList():
                    dfs(ele, depth + 1)
        
        for ele in nestedList:
            dfs(ele, 1)

        def dfs(lst, depth):
            if lst.isInteger():
                return (self.maxDepth - depth + 1) * lst.getInteger()
            
            res = 0
            for ele in lst.getList():
                res += dfs(ele, depth + 1)
            
            return res

        res = 0

        for ele in nestedList:
            res += dfs(ele, 1)
        
        return res