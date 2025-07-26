class MyCircularQueue:

    def __init__(self, k: int):
        # 큐의 최대 크기(용량)를 저장
        self.size = k
        # 고정 크기의 배열로 큐를 구현 (초기값 0)
        self.data = [0] * k
        # 현재 큐에 들어있는 원소 개수
        self.count = 0
        # 큐의 맨 앞을 가리키는 포인터(인덱스)
        self.first = 0
        # 큐의 맨 뒤를 가리키는 포인터(인덱스)
        # 초기에는 아무것도 없으니 -1로 설정
        self.last = -1

        # 예시: k=3
        # data = [0,0,0], count=0, first=0, last=-1 (비어있는 상태)


    def enQueue(self, value: int) -> bool:
        # 큐가 꽉 차있으면 더 넣을 수 없으니 False
        if self.isFull():
            return False

        # 넣기 전에 개수를 +1 (원소가 하나 더 들어감)
        self.count += 1

        # last 포인터를 한 칸 앞으로 이동
        # 원형으로 돌아가기 위해 모듈로 연산 사용
        self.last = (self.last + 1) % self.size
        # 새로운 값을 큐의 끝(last 위치)에 저장
        self.data[self.last] = value

        # 예시:
        # 초기: last=-1 → (last+1)%3=0 → data[0]=10 → count=1
        # data = [10,0,0], first=0, last=0
        return True


    def deQueue(self) -> bool:
        # 큐가 비어있다면 꺼낼 값이 없으므로 False
        if self.isEmpty():
            return False

        # 맨 앞의 값은 따로 삭제하지 않아도 됨 (덮어쓸 예정)
        # first 포인터를 한 칸 앞으로 이동 (원형으로 돌아감)
        self.first = (self.first + 1) % self.size
        # 하나를 꺼냈으니 count -1
        self.count -= 1

        # 예시:
        # data=[10,20,0], first=0 → deQueue() →
        # first=(0+1)%3=1, count=1
        # 논리적 상태: front는 data[1]=20, 큐 안에는 [20]
        return True


    def Front(self) -> int:
        # 큐가 비어있으면 맨 앞 값이 없으니 -1 리턴
        if self.isEmpty():
            return -1
        # 비어있지 않으면 first 포인터가 가리키는 값 반환
        return self.data[self.first]

        # 예시:
        # data=[10,20,0], first=0 → Front()=data[0]=10


    def Rear(self) -> int:
        # 큐가 비어있으면 맨 뒤 값이 없으니 -1 리턴
        if self.isEmpty():
            return -1
        # 비어있지 않으면 last 포인터가 가리키는 값 반환
        return self.data[self.last]

        # 예시:
        # data=[10,20,0], last=1 → Rear()=data[1]=20


    def isEmpty(self) -> bool:
        # count가 0이면 비어있는 상태
        return self.count == 0

        # 예시:
        # count=0 → True, count=2 → False


    def isFull(self) -> bool:
        # count가 size와 같으면 가득 찬 상태
        return self.count == self.size

        # 예시:
        # size=3, count=3 → True, count=2 → False