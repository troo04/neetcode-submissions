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
        tweets = [tweet for tweet in self.tweets[userId]]
        
        for followee in self.following_map[userId]:
            for tweet in self.tweets[followee]:
                tweets.append(tweet)
        
        tweets.sort(key=lambda x: -self.timestamps[x])

        return tweets[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following_map[followerId]:
            self.following_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)