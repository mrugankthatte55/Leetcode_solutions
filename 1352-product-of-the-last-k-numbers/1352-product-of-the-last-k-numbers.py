class ProductOfNumbers:

    def __init__(self):
        self.arr=[]
        self.pre=[]
        # self.len=0
    def add(self, num: int) -> None:
        self.arr.append(num)
        if len(self.pre)<1:
            self.pre.append(num)
        else:
            self.pre.append(1)
            for i in range(len(self.pre)):
                self.pre[i]*=num
    def getProduct(self, k: int) -> int:
        # p=1
        # for i in range(len(self.arr)-k,len(self.arr)):
        #     p*=self.arr[i]
        # return p
        return self.pre[len(self.pre)-k]
        
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

