class Solution:
    def calculate(self, s: str) -> int:
        stack = []  # 논리: 각 숫자를 담아둘 리스트. +는 그대로, -는 음수로, * / 는 즉시 계산
        num = 0     # 논리: 현재 읽고 있는 숫자를 누적. 예: '1','2'를 만나면 1→12
        op = '+'    # 논리: 직전에 나온 연산자를 기억. 초기값은 '+'로 시작
        
        for i, ch in enumerate(s):  # 논리: 문자열의 각 글자를 인덱스와 함께 순회
            if ch.isdigit():        # 논리: 숫자면 num에 누적 (다자리 수 처리)
                num = num * 10 + int(ch)
                # 예: ch='3'이면 num=3, 다음 ch='4'면 num=3*10+4=34
            
            # 논리: 연산자나 마지막 문자일 때, 지금까지의 num과 op를 스택에 반영
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
                if op == '+':       # 논리: 이전 연산자가 '+'라면 그대로 push
                    stack.append(num)
                elif op == '-':     # 논리: 이전 연산자가 '-'라면 음수로 push
                    stack.append(-num)
                elif op == '*':     # 논리: 이전 연산자가 '*'라면 직전 값을 pop하여 곱한 뒤 push
                    stack.append(stack.pop() * num)
                elif op == '/':     # 논리: 이전 연산자가 '/'라면 직전 값을 pop하여 나눈 뒤 push
                    top = stack.pop()
                    stack.append(int(top / num))  # int()로 0쪽 버림
                op = ch  # 논리: 현재 연산자를 다음 처리를 위해 저장
                num = 0  # 논리: 다음 숫자를 새로 읽기 위해 초기화
        
        return sum(stack)  # 논리: 스택에 남은 값들을 모두 더한 결과가 최종 답