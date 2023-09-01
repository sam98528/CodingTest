def solution(id_list, report, k):
    answer = []
    
    report = list(set(report))
    id = {string : 0 for string in id_list}
    result = {string : 0 for string in id_list}
    
    
    for re in report:
        name1, name2 = map(str, re.split())
        id[name2] += 1
    
    
    for ids in id_list:
        if id[ids] >= k:
            id[ids] = -1
    
    
    for re in report:
        name1, name2 = map(str, re.split())
        if id[name2] == -1:
            result[name1] += 1

    
    for ids in id_list:
        answer.append(result[ids]) 
        
        
    return answer