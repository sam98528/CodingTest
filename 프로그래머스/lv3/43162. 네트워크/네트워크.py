def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if visited[i] != 1:
            dfs(i,computers,visited)
            answer+=1
    return answer

def dfs(pc, computers,visited):
    visited[pc] = 1
    for i in range(len(computers[pc])):
        if computers[pc][i] == 1 and visited[i] == 0:
            dfs(i,computers,visited)
        