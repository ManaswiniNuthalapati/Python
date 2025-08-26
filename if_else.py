#1
''' Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.'''
class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if ((a > 0 and b < 0) or (a < 0 and b > 0)) and flag == False:
            return True
        elif ((a<0 and b<0) and flag==True):
            return True
        else:
            return False
        
#2 
'''You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets.'''
def cat_hat(str):
    count_cat = str.count("cat")
    count_hat = str.count("hat")
    if count_cat == count_hat:
        return True
    else:
        return False


