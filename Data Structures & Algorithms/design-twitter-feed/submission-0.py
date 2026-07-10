class Twitter:

    def __init__(self):
        self.stack=[]
        self.foll={}
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.stack.append([tweetId,userId])    
        if userId not in self.foll:
            self.foll[userId]=set()
            self.foll[userId].add(userId)
        return
    def getNewsFeed(self, userId: int) -> List[int]:
        self.foll.setdefault(userId, {userId})
        ans=[]
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i][1] in self.foll[userId]:
                ans.append(self.stack[i][0])
            if len(ans)==10:
                break
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
