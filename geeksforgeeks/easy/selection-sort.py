class Solution: 
    def select(self, arr, i):
        curr = i
        n = len(arr)
        for j in range(i+1, n):
            if (arr[j] < arr[i]) and (arr[j] < arr[curr]):
                curr = j
        return curr
        
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            selected = self.select(arr, i)
            arr[i], arr[selected] = arr[selected], arr[i]