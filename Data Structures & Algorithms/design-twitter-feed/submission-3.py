class Twitter:

    def __init__(self):
        self.following_map = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.timestamps = defaultdict(int)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(tweetId)
        self.timestamps[tweetId] = self.timestamp
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = [(self.timestamps[tweet], tweet) for tweet in self.tweets[userId]]

        heapq.heapify(tweets)
        
        for followee in self.following_map[userId]:
            for tweet in self.tweets[followee]:
                heapq.heappush(tweets, (self.timestamps[tweet], tweet))

                while len(tweets) > 10:
                    heapq.heappop(tweets)
        
        while len(tweets) > 10:
            heapq.heappop(tweets)

        res = []
        while len(tweets) > 0:
            res.append(heapq.heappop(tweets)[1])
        
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following_map[followerId]:
            self.following_map[followerId].remove(followeeId)