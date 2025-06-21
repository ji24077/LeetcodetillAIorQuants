public class Solution {
    public string MergeAlternately(string word1, string word2) {
        int n1 = word1.Length, n2 = word2.Length;
        int n = Math.Max(n1, n2);
        StringBuilder result = new StringBuilder(n1 + n2);

        for (int i = 0; i < n; i++) {
            if (i < n1) result.Append(word1[i]);
            if (i < n2) result.Append(word2[i]);
        }

        return result.ToString();
    }
}