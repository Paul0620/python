class User:
    count = 0
    # __init__ 는 인스턴스가 생성될 때 자동으로 호출
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        User.count += 1

    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다!")

    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}, 비밀번호: ******"

        @classmethod
        def number_of_users(cls):
            print(f"총 유저 수는: {cls.count}입니다.")

User.number_of_users()

"""
__init__ 메소드를 사용하지 않는다면
1. 인스턴스 생성
2. 인스턴스 변수 초기값 설정을 나눠서 해야함
user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")
"""

# __init__을 사용한다면 인스턴스 생성을 자동으로 해주기 때문에 한줄 코딩이 가능함
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Park", "park@codeit.kr", "192847")
user3 = User("Lee", "leeg@codeit.kr", "098346")
user4 = User("Kon", "kon@codeit.kr", "987235")

"""print(user1)
print(user2)"""

"""print(User.count)
print(user1.count)
print(user2.count)"""


