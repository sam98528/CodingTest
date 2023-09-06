from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [0] * len(words)
    
    if target not in words:
        answer = 0
    else:
        answer = bfs(begin,target,words,visited)
    return answer

def bfs(cur,target,words,visited):
    answer = 0
    cnt = 0
    queue = deque()
    queue.append([cur,0])
    while(queue):
        word,cnt = queue.popleft()
        if word == target:
            answer = cnt
            return answer
        cnt += 1
        for temp in range(len(words)):
            if compare(words[temp],word) and visited[temp] == 0:
                queue.append([words[temp],cnt])
                visited[temp] = 1
    return answer            
                
def compare(a,b):
    dif = 0
    for x, y in zip (a,b):
        if x != y:
            dif += 1
    if dif == 1:
        return True
    else:
        return False