class User:
    count = 0

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
