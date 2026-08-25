class Twitter:

    def __init__(self):
        self.following_map = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.timestamp, tweetId])
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.following_map[userId].add(userId)
        for followee in self.following_map[userId]:
            if self.tweets[followee]:
                index = len(self.tweets[followee]) - 1
                timestamp, ID = self.tweets[followee][-1]
                heapq.heappush(minHeap, [-timestamp, ID, followee, index - 1])
        
        while minHeap and len(res) < 10:
            time, ID, followee, index = heapq.heappop(minHeap)
            res.append(ID)

            if index >= 0:
                time, ID = self.tweets[followee][index]
                heapq.heappush(minHeap, [-time, ID, followee, index - 1])
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following_map[followerId]:
            self.following_map[followerId].remove(followeeId)