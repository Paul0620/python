"""def plus(a, b, *args, **kwargs): 
  #position args - 함수 () 안에 선언된 변수를 이르는 말 
  #args - 축약어 튜플로 담아줌
  #keyword argument - hello, asd, aa, ss, dd, ee 같은 것들
  print(args) #변수 선언시 앞에 * 붙여줘야함
  print(kwargs) #변수 선언시 앞에 ** 붙여줘야함
  return a + b

plus(1,2,1,1,1,1,1,1,1,1,1,1,1, hello=True,asd=True,aa=True,ss=True,dd=True,ee=True)"""


def plus(*args):
  result = 0
  for number in args:
    result += number
  print(result)

plus(1,2,2,12,3,12,3,3,54,6,4,1,2,3,5)