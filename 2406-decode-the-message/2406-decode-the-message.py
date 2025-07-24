class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}

        next_char = 'a' # a+1=b

        for ch in key:
          if ch == ' ':
            continue

          if ch not in mapping:
            mapping[ch] = next_char

            next_char = chr(ord(next_char) +1)

            if next_char > 'z':
              break

          decoded = []

        for ch in message:
            if ch == ' ':
              decoded.append(' ')
            else:
              decoded.append(mapping[ch])

        return ''.join(decoded)
