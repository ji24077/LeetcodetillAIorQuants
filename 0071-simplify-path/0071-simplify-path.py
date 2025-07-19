class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')

        stack=[]

        for part in parts:
          if part == '' or part =='.':
            continue
          elif part == "..":
            if stack:
              stack.pop()
          else:
            stack.append(part)
        result = '/' + '/'.join(stack) # / + a/b..
        return result

          

