class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        b = count['b'] // 1    # b는 1개 필요
        a = count['a'] // 1    # a는 1개 필요
        l = count['l'] // 2    # l은 2개 필요
        o = count['o'] // 2    # o는 2개 필요
        n = count['n'] // 1    # n은 1개 필요
        return min(b, a, l, o, n)