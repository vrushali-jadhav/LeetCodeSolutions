class Solution():
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        i,j = 0,0
        k = len(matrix)-1
        
        #[[1,2,3],     ->    [[7,8,9],      ->      [[7,4,1],
        # [4,5,6],            [4,5,6],               [8,5,2],
        # [7,8,9]]            [1,2,3]]               [9,6,3]]
        
        while i <= k:
            while j <= len(matrix[0])-1:
                tmp = matrix[i][j]
                matrix[i][j] = matrix[k][j]
                matrix[k][j] = tmp
                j = j+1
            i = i+1
            k = k-1
            j=0
        
        i,j=0,0

        while i<=len(matrix)-2:
            while j<=len(matrix[0])-1:
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
                j = j+1
            i = i+1
            j =  i

        return matrix       

s = Solution()

#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(s.rotate(matrix))
