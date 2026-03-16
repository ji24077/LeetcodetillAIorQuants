class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # result:
        # 나선형으로 방문한 값을 순서대로 담을 리스트
        result = []

        # 경계 4개를 둔다.
        # top    : 아직 안 본 맨 위 행
        # bottom : 아직 안 본 맨 아래 행
        # left   : 아직 안 본 맨 왼쪽 열
        # right  : 아직 안 본 맨 오른쪽 열
        #
        # 예를 들어
        # 1 2 3
        # 4 5 6
        # 7 8 9
        #
        # 시작할 때
        # top = 0, bottom = 2, left = 0, right = 2
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        # 아직 방문하지 않은 사각형 구간이 남아 있는 동안 반복
        # 즉, 위쪽 경계가 아래쪽 경계를 넘지 않고
        # 왼쪽 경계가 오른쪽 경계를 넘지 않으면 계속 진행
        while top <= bottom and left <= right:
            # 1) 맨 위 행을 왼쪽 -> 오른쪽으로 방문
            #
            # 예:
            # 1 2 3
            # 4 5 6
            # 7 8 9
            # 여기서는 1, 2, 3 방문
            for c in range(left, right + 1):
                result.append(matrix[top][c])

            # 맨 위 행은 다 봤으니 아래로 한 칸 내린다
            # 이제 top 행은 다시 볼 필요가 없음
            top += 1

            # 2) 맨 오른쪽 열을 위 -> 아래로 방문
            #
            # 위 행은 이미 봤으므로 top부터 시작
            #
            # 예:
            # 1 2 3
            # 4 5 6
            # 7 8 9
            # 여기서는 6, 9 방문
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])

            # 맨 오른쪽 열도 다 봤으니 왼쪽으로 한 칸 줄인다
            right -= 1

            # 3) 맨 아래 행을 오른쪽 -> 왼쪽으로 방문
            #
            # 그런데 이 단계는 아직 위/아래 경계가 유효할 때만 해야 한다.
            # 왜냐하면 한 줄짜리 행렬 같은 경우,
            # 이미 top이 bottom을 넘어갔을 수 있기 때문.
            if top <= bottom:
                # 예:
                # 1 2 3
                # 4 5 6
                # 7 8 9
                # 여기서는 8, 7 방문
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])

                # 맨 아래 행도 다 봤으니 위로 한 칸 줄인다
                bottom -= 1

            # 4) 맨 왼쪽 열을 아래 -> 위로 방문
            #
            # 이 단계도 아직 좌/우 경계가 유효할 때만 해야 한다.
            # 왜냐하면 세로 한 줄만 남은 경우,
            # 이미 left가 right를 넘어갔을 수 있기 때문.
            if left <= right:
                # 예:
                # 1 2 3
                # 4 5 6
                # 7 8 9
                # 여기서는 4 방문
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])

                # 맨 왼쪽 열도 다 봤으니 오른쪽으로 한 칸 줄인다
                left += 1

        # 모든 원소를 나선형으로 방문한 결과 반환
        return result