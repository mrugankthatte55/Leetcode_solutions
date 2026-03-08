class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # print(bin(1)[2:])
        # print(bin(3)[2:])
        # print(bin(7)[2:])
        # print(bin(8)[2:])
        # print(bin(15)[2:])
        n=len(nums)
        if nums[0]=="1":
            return "0"
        if nums[0]=="0":
            return "1"
        if nums[0]=="10" or nums[0]=="01":
            return "00"
        if nums[0]=="00":
            return "10"
        s=set()
        for num in nums:
            s.add(int(num,2))
        for i in range(2**(n-1),2**n):
            b=bin(i)[2:]
            if b not in s:
                return b
        return ""
        
        