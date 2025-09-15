    
# Given two binary strings a and b, return their sum as a binary string.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2)+int(b, 2))[2:]
    
    # Power of Two
    class Solution:
        def isPowerOfTwo(self, n: int) -> bool:
            if n<=0:
                return False
            elif n%2==0:
                return True
            elif n==1:
                return True
            else:
                return False
        
        