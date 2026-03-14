class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
      need = {}

      for word in words:
        need[word] = need.get(word, 0) + 1

      word_len = len(words[0])
      word_count = len(words)
      total_count = word_len * word_count
      left = 0
      result = []
      for start in range(word_len):
        left = start
        seen = {}
        matching = 0
        

        for right in range(start, len(s) - word_len + 1, word_len):
          word = s[right: right+ word_len]

          if word in need:
            seen[word] = seen.get(word, 0) + 1
            matching +=1
            # so this is match

            while seen[word] >need[word]:
              #then we have to minus it
              left_word = s[left: left + word_len]
              seen[left_word] -= 1
              matching -= 1

              left += word_len
            if matching  == word_count:
              left_word = s[left: left + word_len]
              result.append(left)
              seen[left_word] -= 1
              matching -= 1
              left += word_len

          else:
              matching =0
              seen = {}

              left = right + word_len
              
              
      return result

              





