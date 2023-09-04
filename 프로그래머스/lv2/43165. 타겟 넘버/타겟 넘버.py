def solution(numbers, target):
    answer = cal(numbers,target,0)
    return answer

def cal(numbers, target,index):
    answer = 0
    if index == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += cal(numbers,target,index+1)
        numbers[index] *= -1
        answer += cal(numbers,target,index+1)
        return answer
            