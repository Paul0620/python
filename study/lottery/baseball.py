from random import randint

# 무작위 번호 3개 뽑기
def generate_numbers():
  numbers = []
  
  while len(numbers) < 3:
    new_number = randint(0, 9)
    if new_number not in numbers:
      numbers.append(new_number)
  
  print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
  return numbers

# 내가 직접 입력한 번호 3개
def take_guess():
  print("숫자 3개를 하나씩 차례대로 입력하세요.")
  new_guess = []
  
  while len(new_guess) < 3:
    new_number = int(input(f"{len(new_guess)+1}번째 숫자를 입력하세요: "))
    if 0 > new_number or new_number > 9:
      print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
    elif new_number in new_guess:
      print("중복되는 숫자입니다. 다시 입력하세요.")
    else:
      new_guess.append(new_number)
  
  return new_guess

# 무작위 번호와 직접 입력한 번호 매칭
def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    for i in range(len(guess)):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1
    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

# 코드를 작성하세요.
while True:
  guess = take_guess()
  s, b = get_score(guess, ANSWER)
  print(f"{s}S {b}B")
  tries += 1
  if s == 3:
    break    

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
