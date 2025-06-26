public class Solution {
    public string ReverseWords(string s) {
      // 1. 문자열 양 끝의 공백 제거
        s = s.Trim();

        // 2. 공백 기준으로 단어 분리
        // StringSplitOptions.RemoveEmptyEntries → 연속된 공백 무시
        string[] words = s.Split(' ', StringSplitOptions.RemoveEmptyEntries);

        // 3. 단어 순서 뒤집기
        Array.Reverse(words);

        // 4. 단어들을 하나의 문자열로 연결 (공백으로 join)
        return string.Join(" ", words);
        
    }
}