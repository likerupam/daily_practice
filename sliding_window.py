#User function Template for python3

from collections import deque

class Solution:
    def firstNegInt(self, arr, k): 
        n = len(arr)
        q = deque()
        result = []
        
        # Process first window
        for i in range(k):
            if arr[i] < 0:
                q.append(i)
        
        # Process rest of the array
        for i in range(k, n):
            
            # Append result for previous window
            if q:
                result.append(arr[q[0]])
            else:
                result.append(0)
            
            # Remove elements out of this window
            while q and q[0] <= i - k:
                q.popleft()
            
            # Add current element if negative
            if arr[i] < 0:
                q.append(i)
        
        # Add result for last window
        if q:
            result.append(arr[q[0]])
        else:
            result.append(0)
        
        return result
