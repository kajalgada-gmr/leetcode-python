class Solution:
    
    def computeStrn(self, row, row_len):
        
        start = 0
        end = row_len - 1
        
        if row[start] is 0:
            return 0
        elif row[end] is 1:
            return row_len
        
        else:
            while start < end:
                mid = start + ((end-start)//2)
                if row[mid] is 0:
                    end = mid
                else:
                    start = mid+1
    
        return start
    
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        strn_list = []
        row_len = len(mat[0])
        
        for row_ind, each_row in enumerate(mat):
            strn = self.computeStrn(each_row, row_len)
            strn_list.append([strn, row_ind])
            
        print(strn_list)
        strn_list.sort()
        print(strn_list)
        
        weak_row = []
        for ind in range(k):
            weak_row.append(strn_list[ind][1])
        
        return weak_row
