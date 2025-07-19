class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {'}' : '{', ')':'(', ']':'['}

        for ch in s:
          if ch in '([{':
            stack.append(ch)
          else:
            if not stack:
              ## its a closed blacket.
              return False
            recent_bracket = stack.pop()
            if pairs[ch] != recent_bracket:
              return False
        return not stack
