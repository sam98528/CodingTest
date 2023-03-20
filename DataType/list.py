# 리스트 자료형
# 여러개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형
# Java에서의 Array와 비슷함.

# 리스트 초기화

# 직접 데이터를 넣어 초기화
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 크기가 N이고, 모든값이 0인 1차원 리스트 초기화
# 많이 사용 될듯.
n = 10
a = [0] * n
print(a)


# 리스트의 인덱싱과 슬라이싱

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# n번째 원소 출력
# Index는 0 부터
print(b[1])

# 뒤에서 첫 번째 원소 출력
print(b[-1])

# 두번째 원소부터 네번째 원소까지
# 시작 인덱스 : 끝 인덱스 + 1
print(b[1:4])

# 총 10개의 원소를 0으로 초기화 시키는 작업
b = [0 for i in range(10)]
print(b)

# 0 부터 19까지 짝수만 포함하는 리스트 만들기
b = [i for i in range(20) if i % 2 == 1]
print(b)


# N X M 크기의 2차원 리스트 한번에 초기화 해야 할 때
# _ (언더바)는 변수의 값을 무시하고자 하고 오직 반복을 위해서는 사용한다.
m = 5
n = 3
array = [[0] * m for _ in range(n)]
print(array)


# 리스트 관련 자주 사용되는 함수
array = [4, 2, 1, 3, 5]

# append()
# 리스트에 원소를 하나 삽입
# 시간 복잡도 O(1)
array.append(6)
print(array)

# sort()
# 오름차순으로 정렬
# 시간 복잡도 O(NlogN)
array.sort()
print(array)

# 내림차순으로 할때는 변수명.sort(reverse = True) 하면 된다.
# 시간 복잡도 O(NlogN)
array.sort(reverse=True)
print(array)

# reverse()
# 리스트의 원소의 순서를 모두 뒤집어 놓는다. (내림차순 오름차순 상관없이 말그대로 reverse)
# 시간 복잡도 O(N)
array.reverse()
print(array)

# insert()
# 특정한 인덱스 위치에 원소를 삽입
# 시간 복잡도 O(N)
array.insert(0, 7)
print(array)

# count()
# 리스트에 특정한 값을 가지는 데이터의 개수를 셀때 사용한다.
# 시간 복잡도 O(N)
print(array.count(2))

# remove()
# 특정한 값을 갖고 있는 원소를 제거, 값을 가진 원소가 여러개면 하나만 제거

array.remove(2)
print(array)

# len()
# 리스트의 사이즈 반환
print(len(array))

# 리스트에서 특정값을 가지는 원소를 모두 제거하기
array = [1, 1, 1, 3, 3, 3, 4, 5, 5, 6]
remove_set = {1, 3, 5}

# for loop으로 array의 모든값을 확인하고, i 가 만약 remove_set에 포함되어 있지 않다면 result에 저장
result = [i for i in array if i not in remove_set]
print(result)
