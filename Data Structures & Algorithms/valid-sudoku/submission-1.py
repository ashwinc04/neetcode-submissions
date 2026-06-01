class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            cols=[]
            for j in range(9):
                cols.append(board[j][i])
            if self.rowcheck(board[i]) != True:
                return False
            if self.rowcheck(cols) != True:
                return False

        for k in range(0, 9, 3):
            for l in range(0, 9, 3):
                m=[]
                for i in range(3):
                    for j in range(3):
                        m.append(board[i+k][j+l])
                if self.rowcheck(m) != True:
                    return False
        


        
        return True

    def rowcheck(self, checks) -> bool:
        kk=['1','2','3','4','5','6','7','8','9']
        k=[]
        for i in checks:
            if i in kk:
                k.append(i)
            else:
                pass
        if len(k)==len(set(k)):
            return True
        else:
            return False