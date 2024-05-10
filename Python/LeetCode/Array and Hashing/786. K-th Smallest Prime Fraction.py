from collections import defaultdict
class Solution:
    def kthSmallestPrimeFraction(self, arr, k: int) :
        myDict = defaultdict(list)
        s = len(arr)
        i,j =0,1
        while True:
    
            if j == s:
                i += 1
                j = i+1
            if i == s - 1:
                break    
            myDict[arr[i]/arr[j]].extend([arr[i],arr[j]])
            j +=1    
        
        return sorted(myDict.items())[k-1][1]