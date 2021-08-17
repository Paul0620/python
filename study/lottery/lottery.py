from random import randint

#내가 뽑은 번호
def generate_numbers(n):
  numbers = []
  for _ in range(n):
    new_number = randint(1, 45)
    if new_number not in numbers:
      numbers.append(new_number)
      
  return numbers

# 당첨 번호
def draw_winning_numbers():
  winning_numbers = generate_numbers(7)
  return sorted(winning_numbers[:6]) + winning_numbers[6:]

# 당첨 개수
def count_matching_numbers(list_1, list_2):
  result = list(set(list_1).intersection(list_2))
  cnt = len(result)
  return cnt

# 당첨 금액
def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    cnt = count_matching_numbers(numbers, winning_numbers)
    if cnt == 6:
        result = 1000000000
    elif cnt == 5 and winning_numbers[-1] in numbers:
        result = 50000000
    elif cnt == 5:
        result = 1000000
    elif cnt == 4:
        result = 50000
    elif cnt == 3:
        result = 5000
    else:
        result = 0
    return result