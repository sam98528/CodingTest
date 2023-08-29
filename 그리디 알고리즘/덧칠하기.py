def solution(n, m, section):
    answer = 0
    start = section[0]
    answer += 1

    for item in section:
        if (start + m > item):
            continue

        start = item
        answer += 1
    return answer
