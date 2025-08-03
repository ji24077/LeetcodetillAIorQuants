from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        self.h_sema = Semaphore(2)           # 수소는 동시에 2개까지만
        self.o_sema = Semaphore(1)           # 산소는 1개만
        self.barrier = Barrier(3)            # HHO가 모여야 실행

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_sema.acquire()
        self.barrier.wait()                  # H 2명 + O 1명이 모일 때까지 대기
        releaseHydrogen()
        self.h_sema.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_sema.acquire()
        self.barrier.wait()                  # H 2명 + O 1명이 모일 때까지 대기
        releaseOxygen()
        self.o_sema.release()
