# 사전 자료형은 키(Key) 와 값 (Value)의 쌍을 데이터로 가지는 자료형
# 순차적으로 저장하는 리스트와 튜프과는 다르다.
# 키는 변경 불가능한 (Immutable) 자료형을 사용 할 수 있다.
# 파이썬의 사전 자료형은 해시 테이블을 이용하므로, 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리 할 수 있다.


# 선언
data = dict()
data['사과'] = "Apple"
data['바나나'] = "Banana"
data['코코넛'] = "Coconut"
print(data)

if "사과" in data:
    print("'사과'를 키 값으로 가지는 데이터가 존재한다.")

# 키 데이터만 뽑을때
for key in data.keys():
    print(key)

for values in data.values():
    print(values)
