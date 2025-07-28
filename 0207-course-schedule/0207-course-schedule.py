class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 논리: 각 노드의 진입 차수(in-degree)를 저장
        indegree = [0] * numCourses

        # 논리: 인접 리스트로 그래프 구성 (key: 과목, value: 이 과목을 듣고 다음으로 갈 수 있는 과목들)
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1  # 논리: course를 듣기 위해 prereq 필요 → 진입차수 증가

        # 논리: 진입 차수가 0인 과목들을 큐에 넣음 (즉, 먼저 들을 수 있는 과목)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        # 논리: 순서대로 과목을 듣고, 해당 과목이 선행 과목인 다른 과목들의 진입 차수를 줄임
        count = 0
        while queue:
            curr = queue.popleft()
            count += 1  # 논리: 과목을 수강 완료 처리

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1  # 논리: 선행 과목 하나 줄었으니 in-degree 감소
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # 논리: 모든 과목을 들었다면 True, 일부 과목을 못 들었다면(사이클) False
        return count == numCourses