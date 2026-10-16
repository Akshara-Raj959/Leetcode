class Solution(object):
    def maximumWealth(self, accounts):
        max = sum = 0 
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                sum=sum + accounts[i][j]
            if sum>max:
                max=sum
            sum=0
        return(max)
        