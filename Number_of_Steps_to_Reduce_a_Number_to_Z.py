class Solution(object):
    def numberOfSteps(self, num):
        c=0
        while num>0:
            if num%2==0:
                num=num/2
                c=c+1
            elif num%2!=0:
                num=num-1
                c=c+1
            if num==0:
                break
        return(c)
        