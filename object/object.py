class User:
    # 인스턴스 메소드의 특별한 규칙 - 첫 번째 파라미터의 이름은 꼭! self로 쓰기
    def say_hello(self):
        # 인사 메세지 출력 메소드
        print(f"안녕하세요! 저는 {self.name}입니다!")

    def login(self, my_email, my_password):
        # 로그인
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디거나 잘못된 비밀번호입니다.")

    def check_name(self, name):
        # 파라미터로 받는 name이 유저의 이름과 같은지 불린으로 리턴하는 메소드
        return self.name == name

user1 = User()
user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

print(user1.check_name("김대위"))
print(user1.check_name("강영훈"))

"""
# 두번째가 정답 - user1을 또 받을 수 없음 앞에서 user1.login으로 인스턴스를 불러왔기 때문
user1.login(user1, "captain@codeit.kr", "12345")
user1.login("captain@codeit.kr", "12345")
"""

"""user1 = User()
user2 = User()
user3 = User()

user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

user2.name = "강영훈"
user2.email = "younghoon@codeit.kr"
user2.password = "98765"

user3.name = "최지웅"
user3.email = "jiwoong@codeit.kr"
user3.password = "78901"

# 인스탠스를 부르는 두가지 방법
User.say_hello(user1)
user1.say_hello()"""
