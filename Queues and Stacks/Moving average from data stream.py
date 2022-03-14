from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window_sum = 0
        self.queue = deque()

    def next(self, val: int) -> float:
        count = len(self.queue)
        if count >= self.size:
            self.window_sum -= self.queue.popleft()

        self.queue.append(val)
        self.window_sum += val

        return self.window_sum / len(self.queue)

movingAverage= MovingAverage(3)
print (movingAverage.next(1))
print (movingAverage.next(10))
print (movingAverage.next(3))
print (movingAverage.next(5))