class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = { "2": "abc", 
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
         "9": "wxyz"
        }
        if not digits:
            return []


        result = []

        def backtracking(index : int, path: str):
          #index = currnet index of digits we need to process.
          #path = combinations  of we selected path.
          if index == len(digits):
            result.append(path)
            return
          possible_letters = phone[digits[index]]
          for letter in possible_letters:
            backtracking(index + 1, path + letter)


        backtracking(0,"")
        return result