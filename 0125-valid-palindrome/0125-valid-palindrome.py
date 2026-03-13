class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s.strip()
        s = s.lower()
        temp = ''.join(char for char in s if char.isalnum()) 
        temp2 = ''.join(temp[i] for i in range(len(temp)-1, -1, -1))
        print(temp)
        print(temp2)
        return temp == temp2







































    #   filtered = []

    #   for ch in s:
    #     if ch.isalnum():
    #       filtered.append(ch.lower())
      
    #   left = 0
    #   right = len(filtered) -1

    #   while left < right:
    #     if filtered[left] != filtered[right]:
    #       return False
    #     left+=1
    #     right-=1
    #   return True


        