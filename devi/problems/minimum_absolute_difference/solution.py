class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        smallest=float('inf')
        for i in range(len(arr)-1):
            current=arr[i+1]-arr[i]
            if current<smallest:
                smallest=current
    
        dif=[]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==smallest:
                dif.append([arr[i],arr[i+1]])
        return dif
        