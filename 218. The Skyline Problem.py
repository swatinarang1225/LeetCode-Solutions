class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort(key=lambda x:[x[0],-x[2]])    #Sort elements according to x-axis (ascending) and height(descending)
        new_b=[]
        max_r=-float('inf')
        min_l=float('inf')
        for i in buildings:
            new_b.append([-i[2],i[0],i[1]])    #Create new array for priority queue with [-1*height, left,right], as we are creating max heap
            max_r=max(max_r,i[1])
            min_l=min(min_l,i[0])
            
        ans=[[0,0,max_r+1]]              #for default when the buildings at a specific point is over
        f_ans=[]
        heapq.heapify(ans)
        while min_l<=max_r:
            while new_b and min_l>=new_b[0][1]: 
                temp=new_b.pop(0)
                heapq.heappush(ans,temp)
            while ans and ans[0][2]<=min_l:
                heapq.heappop(ans)
                
            if not f_ans or f_ans[-1][1]!=(-ans[0][0]):
                f_ans.append([min_l,-ans[0][0]])
            if new_b:
                min_l=min(ans[0][2],new_b[0][1])     #To update the min_l according to the next element and the element itself
            else:
                min_l=ans[0][2]
            
        return f_ans
        
