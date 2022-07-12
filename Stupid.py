class Stupid:
    def __init__(self, name):
        self.name = name

    def __int__(self):
        return 8

s = Stupid('aaa')
# int() 를 지원하기 위해 Stupid는 __int__ 메소드를 지원한다.
print(int(s))

# 숫자 10이 클래스라는 것을 확인해보자
# 클래스이기 때문에 함수(메소드)를 지원한다.
# 숫자 10을 서비스라고 생각하고 메소드를 API로 보면 이해하기 쉽다.
# 더블 언더바로 시작하고 끝나는 메소드는 스페셜 메소드, 그 외에는 그냥 메소드
print(dir(10))