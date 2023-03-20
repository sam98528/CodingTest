# 파이썬에서는 문자열을 초기화 할때는 큰 따옴표("") 작은 따옴표 ('')를 이용한다.
# 문자열 안에 따옴표를 사용할려면 백슬래시 (/)를 사용하면 된다.

data = 'Hello world'
data2 = "Hello world"

if data == data2:
    print("True")

# 문자열 합치기
data = "Hello"
data2 = "World"
print(data + " " + data2)

# 문자열 복사
print(data * 2)

# 문자열 슬라이싱
print(data[0:3])

# 문자열은 인덱스를 통해 한 char에 접근은 할 수 있지만, 변경은 할 수 없다.
# data[0] = "F" -> TypeError
