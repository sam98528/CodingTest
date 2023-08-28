# 자주 사용되는 표준 입력 방법
# input() , map() , readline()

import sys


# input()
# 한줄의 문자열을 입력 받는 함수

# Input in a line
a = input()
print(a)

# map()
# 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

# "1 2 3 4 5 6 7 8" 입력
# input().split()를 통해 공백을 기준으로 나눈다.
listA = list(map(int, input().split()))
print(listA)

# 만약 구분된 데이터의 개수가 많지 않고,
# 해당 데이터를 list로 관리 할 필요가 없다면,
# 굳이 List를 쓰지 않고
# 각 변수를 만들어서 사용할 수 있다.
testA, testB, testC = map(int, input().split())


# 더 빠르게 큰 데이터를 받아올 때는
# sys.stdin.readline()을 사용하는것이 더 효율적이다.
# 다만 readline 함수는 마지막 '\n' (엔터) 도 포함을 하기 때문에
# .restrip을 같이 사용한다.

data = sys.stdin.readline().rstrip()
print(data)

# -------------------------------

# 자주 사용되는 표준 입력 방법
# print()

# 한개 이상의 데이터를 출력하려면 ( , ) 를 사용하면 된다.
b = 1
c = 2
print(b, c)

# print() 함수는 마지막에 '\n'를 자동으로 출력 하는데,
# 다른 print() 함수를 연속적으로 쓰고 싶으면
# end 속성을 사용하면 된다.

# print(b)
# print(c)
# 결과 :
# 1
# 2

print(b, end=" ")
print(c, end=" ")
# 결과 :
# 1 2
