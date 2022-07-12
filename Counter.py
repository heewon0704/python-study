class Counter:
    def __init__(self, stop):
        self.current = 0 #현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop #반복을 끝낼 숫자
    def __iter__(self):
        return self #현재 인스턴스를 반환
    def __next__(self):
        if self.current < self.stop: #현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration #예외 발생

for i in Counter(3):
    print(i, end=' ')