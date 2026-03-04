class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result= [];
        for i in range(numRows):
            row= [1]*(i+1)#since 1 at the start and end of each row
            for j in range(1,i):
                row[j]= result[i-1][j-1]+ result[i-1][j]#for middle elements
            result.append(row)
        return result
        