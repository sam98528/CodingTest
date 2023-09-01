def solution(players, callings):
    answer = []
    playersMap = dict()
    index = 0
    
    for player in players:
        playersMap[player]= int(index)
        index += 1
    
    for call in callings:
        index = int(playersMap[call])
        playersMap[call] -= 1
        playersMap[players[index-1]] += 1
        players[index-1] ,players[index] = players[index],players[index-1]
    return players