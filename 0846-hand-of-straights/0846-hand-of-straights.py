class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand))%groupSize != 0:
            return False
        d={}
        for i in range(len(hand)):
            if hand[i] in d:
                d[hand[i]]+=1
            else:
                d[hand[i]]=1
        i=0
        hand.sort()
        
        for i in hand:
            if d[i]>=1:
                for j in range(i,i+groupSize):
                    if j in d:
                        d[j]-=1
                        if d[j]<0:
                            return False
                    else:
                        return False
        return True
        
        # while i<len(hand):
        #     if d[hand[i]]>=1:
        #         for j in range(hand[i],hand[i+groupSize]):
        #             d[hand[j]]-=1
        #             if d[hand[j]]<0:
        #                 return False
        #     i+=groupSize
        # return True
            #     if d[hand[i+1]]>=1:
            #         if d[hand[i+2]]>=1:
            #             d[hand[i]]-=1
            #             d[hand[i+1]]-=1
            #             d[hand[i+2]]-=1
            # i+=groupSize
#         a=[]
#         hand.sort()
#         i=0
#         while i<len(hand):
            # 1 2 2 3 3 4 6 7 8
#             i+=groupSize