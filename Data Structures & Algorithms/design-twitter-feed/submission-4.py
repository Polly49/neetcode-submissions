class Twitter:

    def __init__(self):
        self.stack=[]
        self.foll={}
        self.time=0
        heapq.heapify(self.stack)
        self.temp=0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        heapq.heappush(self.stack,(-self.time,[userId,tweetId]))   
        if userId not in self.foll:
            self.foll[userId]=set()
            self.foll[userId].add(userId)
        return
    def getNewsFeed(self, userId: int) -> List[int]:
        self.foll.setdefault(userId, {userId})
        ans=[]
        self.temp = self.stack.copy()
        while self.temp and len(ans) < 10:
            time, (uid, tid) = heapq.heappop(self.temp)
            if uid in self.foll[userId]:
                ans.append(tid)

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.foll:
            self.foll[followerId] = {followerId}
        self.foll[followerId].add(followeeId)
        return
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.foll:
            return
        if followerId!=followeeId:
            self.foll[followerId].discard(followeeId)
        return
