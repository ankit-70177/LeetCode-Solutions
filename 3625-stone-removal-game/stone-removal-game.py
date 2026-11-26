class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        val=10
        alice=True
        while True:
            if n>=val:
                if alice:
                    n-=val
                    val-=1
                    alice=False
                else:
                    n-=val
                    val-=1
                    alice=True
            else:
                break
        if alice:
            return False
        else:
            return True
        